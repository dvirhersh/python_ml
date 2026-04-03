import sympy as sp

x, y = sp.symbols('x y')

f = x**2 + y**2

H = sp.hessian(f, (x, y))
print(H)