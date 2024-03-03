# Inference the Right Way with MK1

Discover the power of MK1 for seamless inference with the highest possible performance and zero configuration. [More info](https://mk1.ai/blog/flywheel-launch?_gl=1*1r6qzwz*_ga*NDc3OTE1NjY4LjE3MDkyMzUxMzc.*_ga_G1XWZE50S3*MTcwOTQ2ODYyMy40LjEuMTcwOTQ2OTMxOS4wLjAuMA..)

## What is Inference?

Inference in the context of large language models refers to their ability to generate predictions or responses based on given input, essentially deriving meaningful insights from provided context or queries.

## What are Inference Systems?

Inference serving systems constitute the entire infrastructure and software ecosystem designed to manage and serve AI/ML models for inference. These systems act as the bridge between trained AI models and real-world applications, ensuring availability and scalability.

## Inference Components

- **Inference Servers**: Host and serve ML models for inference tasks.
- **Model Storage**: Manages ML models and metadata efficiently.
- **Hardware Accelerators**: Boost performance using GPUs or specialized chips.
- **Load Balancers**: Distribute requests across servers for efficient processing.
- **Monitoring & Management Tools**: Essential for system reliability and quick issue resolution.

## Why MK1?

Unlike other inference frameworks, MK1's Flywheel was designed to work right out of the box with the highest possible performance without any configuration.

### Regarding the MK1 Flywheel engine:

- **Core Component**: Executes machine learning models, particularly large language models, for text generation tasks.
- **Inference Server**: Handles text generation requests and returns responses, acting as a core component within an inference serving system.
- **Utilizes Hardware Accelerators**: May leverage GPUs to accelerate model inference, enhancing performance and scalability.

Overall, the MK1 Flywheel engine enables efficient and scalable text generation capabilities within an inference serving system, facilitating the deployment of large language models for various applications.


# How to Use? Building our First App with Modal & Mk1

## Stack and Tools
We will use Poetry to install and manage Python packages:

- **Modal**
  - Flask
- **MK1**
  - Inference API
- **Requests**

## App on Modal

### Create an Endpoint 
We will build a Modal app to serve our MK1-Inference API in `views.py`. **Modal** provides various ways to expose functions as web endpoints. 
Read more info [here](https://modal.com/docs/guide/webhooks#serving-asgi-and-wsgi-apps)


### Modal Serve

To run this app locally, simply execute the following command:

```bash
modal serve views.py
```

Deploying a Web Server
For deploying our application and creating a persistent web endpoint in the cloud, execute the following command:

```bash
modal deploy
```


## Deploying a web server

We could also deploy our app and create a persistent web endpoint in the cloud by running 

`modal deploy`

# views.py

Implements FastAPI and modal for text generation using the MK1 Flywheel. It starts by initializing the FastAPI application and defining the necessary routes: for health status, statistics, and text generation. The `/generate` endpoint processes requests for text generation based on the provided payload.

---

### Client for MK1 Flywheel Endpoint

The `client.py` file interacts with the MK1 Flywheel endpoint for text generation. It sends a POST request with input parameters and retrieves generated text. Key features include:

- Imports libraries for HTTP requests and JSON handling.
- Defines endpoint URL and payload.
- Implements a function for making POST requests.
- Handles potential request exceptions.

This script simplifies interaction with the MK1 Flywheel endpoint to retrieve generated text.

---

# Defining Models to Interact with MK1 

### GenerationRequest

Represents a request for text generation. Attributes:

- **text** (*str*): The initial input text provided to the model.
- **max_tokens** (*int*): The maximum number of tokens generated in response.
- **eos_token_ids** (*List[int]*): Token IDs signifying the end of a sequence.
- **max_input_tokens** (*int*, default: 0): Maximum tokens allowed in input text.
- **num_samples** (*int*, default: 1): Number of completions to generate.
- **stop** (*List[str]*): Strings to stop generation.
- **temperature** (*float*, default: 1.0): Controls output randomness.

### GenerationResponse

Represents a response containing generated text. Attributes:

- **created** (*float*): Timestamp indicating request creation.
- **finished** (*float*): Timestamp showing response completion.
- **num_samples** (*int*): Number of text completions generated.
- **prompt** (*str*): Input text snippet for text generation.
- **prompt_tokens** (*int*): Number of word-tokens in input prompt.
- **responses** (*List[GenerationResponseSample]*): List of generated responses.
