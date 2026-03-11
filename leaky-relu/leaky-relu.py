import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    for idx, num in enumerate(x):
        if num < 0:
            x[idx] = num * alpha
    return np.array(x)
            