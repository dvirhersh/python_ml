import numpy as np
from scipy.spatial.distance import cosine

v1 = np.array([1, 0.5])
v2 = np.array([2, 1])  # same direction, different magnitude

# scipy computes cosine *distance* (1 - similarity), so need to subtract from 1
similarity = 1 - cosine(v1, v2)
print(f"Cosine similarity : {similarity}")  # 1.0 (perfectly aligned)

#############
from numpy.linalg import norm

a = np.array([1, 2])
b = np.array([2, 3])

cos_sim = np.dot(a, b) / (norm(a) * norm(b))
print(f"cos_sim = {cos_sim:.4f}")
