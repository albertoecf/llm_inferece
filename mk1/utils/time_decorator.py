import time
from typing import Dict, Any


# Decorator function to calculate request execution time
def timing_decorator(func):
    """Decorator function to calculate request execution time."""

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Request took: {end_time - start_time:.2f} seconds")
        return result

    return wrapper
