import numpy as np

A = np.array([[1,2]]) # shape (1,2)
B = np.array([[3],[4]]) # shape (2,1)

print(A @ B,"\n")

######
X = np.array([[1, 2], [3, 4]]) # e.g., 2 samples, 2 features
W = np.array([[0.1, 0.2], [0.3, 0.4]]) # e.g., weight matrix

# Matrix multiplication
output = X @ W # or np.matmul(X, W)
print(output)
