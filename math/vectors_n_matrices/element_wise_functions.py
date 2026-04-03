import numpy as np

x = np.array([-1, 0, 2])
relu = np.maximum(0, x)
print(relu)
#################
z = np.array([-1.5, 2.0, -0.5, 3.0])

# Element-wise ReLU activation function: max(0, z)
a = np.maximum(0, z)
print(f"\nReLU Output: {a}") # Output: [0.  2.  0.  3.]