### MK1 FastAPI Endpoint and Client

This repository contains a FastAPI endpoint implemented using MK1 for inference with Flywheel, as well as a client script to interact with the endpoint.

Useful docs

* [MK1 HTTP endpoint on modal](https://docs.mk1.ai/applications/modal/endpoint.html)
* [Modal Getting Started](https://modal.com/docs/examples/hello_world)


---

#### `views.py`

`views.py` defines a FastAPI endpoint that accepts HTTP requests for inference and returns responses using MK1. The endpoint supports the following functionalities:

- `/health`: A health check endpoint that returns a 503 status code if there are no runners available, and a 200 status code otherwise.
- `/stats`: An endpoint that returns the current stats of the MK1 Flywheel container.
- `/generate`: An endpoint that accepts a JSON payload with the generation request and returns the generation response.

The endpoint utilizes a pre-baked Mistral-7b-instruct model, but can be modified to use other supported models. Additionally, the script includes a decorator to calculate the execution time of requests.

To run the endpoint, use the command `modal serve views.py`. Note that the URL may need to be adjusted based on the deployment environment.


#### `client.py`

`client.py` contains a Python script to make HTTP POST requests to the MK1 FastAPI endpoint defined in `views.py`. The script sends a JSON payload with a generation request and prints the response received from the endpoint.

The script includes a decorator to calculate the execution time of requests. To execute the client script, simply run `python client.py` or `poetry run python client.py`. Remember to adjust the URL based on the deployment environment.

## Setting base_url

🚧 We are currently exploring ways to streamline this step.
In `views.py`, we define a URL that corresponds to our endpoint. After executing `modal serve`, we expect to see the following message in the terminal:
 ```Created app => https://albertoecf--mk1-chat-endpoint-dev.modal.run```. This URL represents the direction of our running app, and the `base_url` variable should be assigned this value.

#### `utils/time_decorator.py` (Bonus)

`time_decorator.py` defines a decorator function to calculate the execution time of a function based on MK1 response. This decorator is used in the `client.py` script to measure the time taken for the HTTP POST request.



## Next Steps
- Investigate https://modal.com/docs/guide/trigger-deployed-functions 