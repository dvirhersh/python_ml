import numpy as np

x = np.array([1, 1])
T = np.array([[2, 0], [0, 2]])  # Scaling

print(T @ x)  # [2,2]
