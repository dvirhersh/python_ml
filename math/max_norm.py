import numpy as np

w = np.array([1.0, 1.0])
x = np.array([2.0, 2.0])

# L-infinity attack
epsilon = 1.0
delta = -epsilon * np.sign(w)

x_adv = x + delta

print("Original:", np.dot(w, x))
print("Adversarial:", np.dot(w, x_adv))