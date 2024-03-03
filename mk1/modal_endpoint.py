import modal
from typing import List
from pydantic import BaseModel


class GenerationRequest(BaseModel):
    """Represents a request for text generation.

    Attributes:
        text (str): The input text prompt for text generation.
        max_tokens (int): The maximum number of tokens to generate.
        eos_token_ids (List[int]): List of token IDs that indicate the end of a generation sequence.
        max_input_tokens (int): The maximum number of input tokens to consider.
        num_samples (int): The number of samples to generate.
        stop (List[str]): List of stop sequences to prevent generation beyond.
        temperature (float): The temperature parameter for generation.
        top_k (int): The top-k parameter for nucleus sampling.
        top_p (float): The top-p parameter for nucleus sampling.
        presence_penalty (float): The presence penalty for generation.
        frequency_penalty (float): The frequency penalty for generation.
    """
    text: str
    max_tokens: int
    eos_token_ids: List[int] = []
    max_input_tokens: int = 0
    num_samples: int = 1
    stop: List[str] = []
    temperature: float = 1.0
    top_k: int = 50
    top_p: float = 1.0
    presence_penalty: float = 0.0
    frequency_penalty: float = 0.0


class GenerationResponseSample(BaseModel):
    """Represents a single sample of generated text in a generation response.

    Attributes:
        text (str): The generated text.
        generated_tokens (int): The number of tokens generated.
        finished (float): The timestamp when generation finished.
        finish_reason (str): The reason for generation completion.
    """
    text: str
    generated_tokens: int
    finished: float
    finish_reason: str


class GenerationResponse(BaseModel):
    """Represents a response containing generated text.

    Attributes:
        created (float): The timestamp when the response was created.
        finished (float): The timestamp when generation finished.
        num_samples (int): The number of samples generated.
        prompt (str): The input prompt for generation.
        prompt_tokens (int): The number of tokens in the input prompt.
        responses (List[GenerationResponseSample]): List of generated text samples.
    """
    created: float
    finished: float
    num_samples: int
    prompt: str
    prompt_tokens: int
    responses: List[GenerationResponseSample]


stub = modal.Stub(
    "mk1-endpoint-backend",
    image=modal.Image.debian_slim(),
)


@stub.function(
    keep_warm=1,
    allow_concurrent_inputs=1024,
    timeout=600,
)
@modal.asgi_app(label="mk1-chat-endpoint")
def app():
    """Creates a FastAPI application for text generation using MK1 Flywheel.

    Returns:
        fastapi.FastAPI: The FastAPI application for text generation.
    """
    import modal
    import fastapi
    import fastapi.staticfiles

    web_app = fastapi.FastAPI()
    Model = modal.Cls.lookup(
        "mk1-flywheel-latest-mistral-7b-instruct", "Model", workspace="mk1"
    ).with_options(
        gpu=modal.gpu.A10G(),
        timeout=600,
    )
    model = Model()

    @web_app.get("/health")
    async def health():
        """Endpoint for health status of the generation model.

        Returns:
            fastapi.Response: The health status response.
        """
        stats = await model.generate.get_current_stats.aio()
        if stats.num_total_runners == 0:
            status_code = fastapi.status.HTTP_503_SERVICE_UNAVAILABLE
        else:
            status_code = fastapi.status.HTTP_200_OK

        response = fastapi.Response(
            content="",
            status_code=status_code,
            media_type="text/plain",
        )
        return response

    @web_app.get("/stats")
    async def stats():
        """Endpoint for retrieving statistics of the generation model.

        Returns:
            dict: The statistics of the generation model.
        """
        stats = await model.generate.get_current_stats.aio()
        stats = {
            "backlog": stats.backlog,
            "num_total_runners": stats.num_total_runners,
        }
        return stats

    @web_app.post("/generate")
    async def generate(request: fastapi.Request) -> fastapi.Response:
        """Endpoint for generating text based on the request payload.

        Args:
            request (fastapi.Request): The request containing generation parameters.

        Returns:
            fastapi.Response: The response containing generated text.
        """
        content_type = request.headers.get("Content-Type")
        if content_type != "application/json":
            return fastapi.Response(
                content="",
                status_code=fastapi.status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
                media_type="text/plain",
            )

        request_data = await request.json()
        generation_request = GenerationRequest(**request_data)
        response = model.generate.remote(**generation_request.dict())
        return GenerationResponse(**response)

    return web_app
