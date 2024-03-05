import modal
from models import GenerationRequest, GenerationResponse

MODEL_TO_USE = "mk1-flywheel-latest-mistral-7b-instruct"
IMAGE_TO_USE = modal.Image.debian_slim()
GPU_CONFIG = modal.gpu.A10G()


stub = modal.Stub(
    "mk1-endpoint-backend",
    image=IMAGE_TO_USE,
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
    #todo extraer model 
    Model = modal.Cls.lookup(
        MODEL_TO_USE, "Model", workspace="mk1"
    ).with_options(
        gpu=GPU_CONFIG,
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
