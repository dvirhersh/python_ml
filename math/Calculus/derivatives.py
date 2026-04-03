import torch

# Define a tensor with gradient tracking enabled (weight)
x = torch.tensor([2.0], requires_grad=True)

# Define a simple function: y = x^2
y = x ** 2

# Compute the derivative dy/dx
y.backward()

# The derivative of x^2 at x=2 is 2*x = 4
print(f"derivative dy / dx at x = 2 : {x.grad.item()}")

import numpy as np

def f(x):
    return x **2

def numerical_derivative(f, x, h = 1e-5):
    return (f(x+h) - f(x)) / h

print ( numerical_derivative(f , 3)) # ~6