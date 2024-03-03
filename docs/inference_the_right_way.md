Inference the right way with mk1. 


 * highest possible performance 
 * without any configuration.

[more info](https://mk1.ai/blog/flywheel-launch?_gl=1*1r6qzwz*_ga*NDc3OTE1NjY4LjE3MDkyMzUxMzc.*_ga_G1XWZE50S3*MTcwOTQ2ODYyMy40LjEuMTcwOTQ2OTMxOS4wLjAuMA..)

# What is inference 

In the context of a large language model, an inference refers to the model’s ability to generate predictions or responses based on the context and input it has been given or simply defined as "the process of getting a response from the trained LLM model for the user's query or prompts"

# What are inference system 

Inference serving system 

Entire infrastructure and software ecosystem designed to manage and serve AI/ML models for inference. Inference servers are the “workhorse” of AI applications, they are the bridge between the trained AI model and real-world, useful applications.

# Inference Components

- **Inference Servers**: Host and serve ML models for inference tasks, ensuring availability and scalability.
- **Model Storage**: Manages ML models and metadata, enabling efficient retrieval and loading.
- **Hardware Accelerators**: Boost performance using GPUs or specialized chips for complex models like large language models.
- **Load Balancers**: Distribute requests across servers for efficient processing within limits.  
- **Monitoring & Management Tools**: Essential for system reliability, offering insights for quick issue resolution.


# Why MK1?
Unlike other inference frameworks, Flywheel was designed to work right out of the box with the highest possible performance without any configuration

Regarding the MK1 Flywheel engine:

Core Component: Executes machine learning models, particularly large language models, for text generation tasks.

Inference Server: Handles text generation requests and returns responses, acting as a core component within an inference serving system.

Utilizes Hardware Accelerators: May leverage GPUs to accelerate model inference, enhancing performance and scalability.

Overall, the MK1 Flywheel engine enables efficient and scalable text generation capabilities within an inference serving system, facilitating the deployment of large language models for various applications.


# How to use? Building our first app with Modal & Mk1

# Stack and Tools
We will use poetry to install and manage python packages

- Modal
  - Flask (Modal decorator)
- MK1
  - Inference API
- Requests

# APP on Modal
# Modal is 

# Modal code

Create an endpoint 
    We will build modal app to serve our MK1-Inference API. Modal uses FastAPI to define its method of modal.asgi_app(label="mk1-chat-endpoint"). Modal gives you a few ways to expose functions as web endpoints. You can turn any Modal function into a web endpoint with a single line of code. The easiest way to create a web endpoint from an existing function is to use the @modal.web_endpoint decorator. 
    from modal import Stub, web_endpoint

stub = Stub()

@stub.function()
@web_endpoint()
def f():
    return "Hello world!"

This decorator wraps the Modal function in a FastAPI application.

Developing with modal serve
You can run this code as an ephemeral app, by running the command

modal serve server_script.py

Deploying a web server
You can also deploy your app and create a persistent web endpoint in the cloud by running modal deploy


Create a client
    Simply request to specific endpoint


# Defining Models to interact with MK1 

### GenerationRequest

Represents a request for text generation. Attributes:

- **text** (*str*) - The initial input text provided to the model.
- **max_tokens** (*int*) - The maximum number of tokens generated in response.
- **eos_token_ids** (*List[int]*) - Token IDs signifying the end of a sequence.
- **max_input_tokens** (*int*, default: 0) - Maximum tokens allowed in input text.
- **num_samples** (*int*, default: 1) - Number of completions to generate.
- **stop** (*List[str]*) - Strings to stop generation.
- **temperature** (*float*, default: 1.0) - Controls output randomness.


### GenerationResponse

Represents a response containing generated text. Attributes:

- **created** (*float*) - Timestamp indicating request creation.
- **finished** (*float*) - Timestamp showing response completion.
- **num_samples** (*int*) - Number of text completions generated.
- **prompt** (*str*) - Input text snippet for text generation.
- **prompt_tokens** (*int*) - Number of word-tokens in input prompt.
- **responses** (*List[GenerationResponseSample]*) - List of generated responses.


