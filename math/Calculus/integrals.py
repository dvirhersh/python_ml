import scipy.integrate as integrate


# define function f(x) = x
def f(x):
    return x


# Calculate integral from 0 to 2 (Area of traingle: 0.5 * base * height = 2)
result, error = integrate.quad(f, 0, 2)
print(f"Integral result: {result}")
print(f"Integral error: {error}")

result = integrate.quad(lambda x: x, 0, 2)
print(result)
