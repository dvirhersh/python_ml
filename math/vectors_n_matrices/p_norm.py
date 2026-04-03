import numpy as np
from numpy import linalg as LA

x = np.array([3,4])

l1 = LA.norm(x, ord=1)
l2 = LA.norm(x, ord=2)

print(l1, l2)  # 7, 5

#########
weights = np.array([8, -7])

# L2 Norm (Euclidean length): sqrt(3^2 + (-4)^2) = 5.0
l2_norm = np.linalg.norm(weights, ord=2)
print(f"\nL2 Norm: {l2_norm}")