import numpy as np

probabilities = np.array([0.1, 0.7, 0.2])
predicted_class = np.argmax(probabilities)  # Returns 1
print(predicted_class)

#######
arr = np.array([1, 5, 2, 7, -2])
print(np.argmin(arr))  # 1
