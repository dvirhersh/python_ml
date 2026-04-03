import numpy as np

a = np.array([1,2,3])
w  = np.array([0.5, 0.5, 0.5])

dot_product = np.dot(a, w)
print(f"dot_product = {dot_product}") # 1*.5 + 2*.5 +3*.5
print(f"a@w = {a@w}") # 1*.5 + 2*.5 +3*.5
print(f"w@a = {w@a}") # 1*.5 + 2*.5 +3*.5

print(f"np.dot([1,2], [3,4]) = {np.dot([1,2], [3,4]) }")