from scipy.optimize import minimize

# a simple convex loss function : L(w) = (w-3)^2


def loss_function(w):
    return (w[0] - 3) ** 2


# start guessing at w=0

init_guess = [0.0]
result = minimize(loss_function, init_guess)

print(f"optimal weigth to minimize loss : {result.x[0]:.2f}\n")

###
w = 0.0
lr = 0.2
for _ in range(10):
    grad = 2 * (w - 3)
    w -= lr * grad
    print(f"current w = {w}")

print(f"final w = {w}")  # ~3
