import numpy as np

A = np.array([[2,0],[0,3]])

vals , vecs = np.linalg.eig(A)
print(vals)

############

A = np.array([[4, -2], [1, 1]])
eigenvalues, eigenvectors = np.linalg.eig(A)

print(f"Eigenvalues: {eigenvalues}")