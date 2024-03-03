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
