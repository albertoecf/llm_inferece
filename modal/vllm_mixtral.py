import os
import time

from modal import Image, Stub, enter, exit, gpu, method

MODEL_DIR = "/model"
BASE_MODEL = "mistralai/Mixtral-8x7B-Instruct-v0.1"
GPU_CONFIG = gpu.A100(memory=80, count=2)

