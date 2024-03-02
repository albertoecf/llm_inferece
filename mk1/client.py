import requests
import json
from typing import Dict, Any
import requests
from utils.time_decorator import timing_decorator

# URL and payload
# set modal's url
url = "https://albertoecf--mk1-chat-endpoint-dev.modal.run/generate"
headers = {"Content-Type": "application/json"}
data = {
    "text": "What is the difference between a llama and an alpaca?",
    "max_tokens": 512,
    "eos_token_ids": [1, 2],
    "temperature": 0.8,
    "top_k": 50,
    "top_p": 1.0,
}


# Function to make the POST request
@timing_decorator
def make_post_request(
    url: str, headers: Dict[str, str], data: Dict[str, Any]
) -> Dict[str, Any]:
    """Make a POST request to the specified URL."""
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()  # Raise an exception for bad status codes

    return response.json()


# Making the POST request
try:
    response_data = make_post_request(url, headers, data)
    print(response_data)
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
