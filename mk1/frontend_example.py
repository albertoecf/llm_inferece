import requests
import json

url = "https://albertoecf--mk1-chat-endpoint-dev.modal.run/generate"
headers = {
    "Content-Type": "application/json"
}

data = {
    "text": "What is the difference between a llama and an alpaca?",
    "max_tokens": 512,
    "eos_token_ids": [1, 2],
    "temperature": 0.8,
    "top_k": 50,
    "top_p": 1.0
}

try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()  # Raise an exception for bad status codes
    print(response.json())
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")