What is an inference in a Large Language Model?
[Basic LLM inferece](https://medium.com/@andrew_johnson_4/understanding-inference-in-large-language-models-f4a4a4a736a5)
[LLM Inference Optimizations](https://www.linkedin.com/pulse/llm-inference-hwsw-optimizations-sharada-yeluri-wfdyc/)
[What is an inference server?](https://www.titanml.co/resources/what-is-an-inference-server-10-characteristics-of-an-effective-inference-server-for-generative-ai-deployments#:~:text=Inference%20servers%20are%20the%20%E2%80%9Cworkhorse,executes%20these%20crucial%20inference%20tasks)


In the context of a large language model, an inference refers to the model’s ability to generate predictions or responses based on the context and input it has been given or simply defined as "the process of getting a response from the trained LLM model for the user's query or prompts". 

For example, if a user types in “I am feeling hungry, maybe I should order some…” and the LLM generates the completion “pizza,” it has made an inference based on the context of the input text

Inference is a critical step in deploying LLMs. **But a lot goes before the model is deployed for production.**



### Inferece Steps: 
- Trained model goes through several optimizations to reduce the memory footprint and computational intensity of the model.
- The optimized model is compiled for the specific hardware (GPUs or inference accelerators)
- The compiled models are stored in file servers of the inference serving systems

## Inference serving system 

Entire infrastructure and software ecosystem designed to manage and serve AI/ML models for inference.
    - Inference servers are the “workhorse” of AI applications, they are the bridge between the trained AI model and real-world, useful applications.
    - Inference servers are responsible for copying the compiled models from the file system to accelerator memories. Also handles requests to process data, running the model, and returning results
    - Inferece servers are software applications hosted on the CPUs
    - The load balancers, software applications, distribute the user requests among many inference servers
    - A cluster of GPUs or inference accelerators is associated with each inference server






