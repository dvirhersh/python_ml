import numpy as np

a = np.array([1, 2])
b = np.array([3, 4])

print(a * b)  # [3, 8]

####
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Hadamard product
hadamard = A * B  # Output: [[5, 12], [21, 32]]
print("\n", hadamard)
