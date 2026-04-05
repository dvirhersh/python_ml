import numpy as np

def softmax(x):
    e = np.exp(x - np.max(x))  # stability trick (when values in x are large)
    # e = np.exp(x)
    return e / e.sum()

print(softmax(np.array([1,2,3])))