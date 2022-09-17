# 练习 20
# import sympy
from sympy import *
# Use sympy.symbols() method
x, y, a, b, c = symbols('x, y, a, b, c')
# Solve symbolic equation
f = a*x**2+b*x+c
sol = solve(f, x)
print(sol)

# Solve symbolic matrix
M = Matrix([[1, c], [c, 1]])
print(M)
Eigen=M.eigenvects()
print('#1: (Eigenvalues, Number, Eigenvector)=', Eigen[0])
print('#2: (Eigenvalues, Number, Eigenvector)=', Eigen[1])