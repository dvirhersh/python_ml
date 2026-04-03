import numpy as np

w = np.array([1.0, 2.0])
x = np.array([3.0, 4.0])
y = 10

pred = w.dot(x)
print("pred = ", pred)
grad = 2 * (pred - y) * x

print("grad = ", grad)