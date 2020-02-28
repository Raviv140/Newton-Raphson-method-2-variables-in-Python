import sympy as sy
import numpy as np
import matplotlib.pyplot as plt

# Created by Raviv Herrera #

x = sy.Symbol('x')
y = sy.Symbol('y')
# Split function of 2 variables #

f1 = x**2 + y
f2 = 5*x + 4 * y + 7

FM = sy.Matrix(2, 1, (f1, f2))
xx = np.linspace(0, 10, 200, dtype=np.float64)
yy = np.linspace(0, 10, 200, dtype=np.float64)
zz1 = np.ndarray(xx.size or yy.size, dtype=np.float64)
zz2 = np.ndarray(xx.size or yy.size, dtype=np.float64)
first_guess = sy.Matrix(2, 1, [1, -1])
for i in range(zz1.size):
    zz1[i] = f1.subs({x: xx[i], y: yy[i]})
    zz2[i] = f2.subs({x: xx[i], y: yy[i]})


def newton_r_2var(Iter, func, x0):
    print(FM)
    for i in range(Iter):
        jac = sy.Matrix.jacobian(func, (x, y))
        rev_jac = jac.subs({x: x0[0], y: x0[1]})
        rev_jac = rev_jac.inv()
        next_x0 = x0 - rev_jac * func.subs({x: x0[0], y: x0[1]})
        x0 = next_x0
        print(f"The next Iteration : {next_x0.evalf()}")
    print(f"The Root of function {func} is  : {x0.evalf()}")


newton_r_2var(6, FM, first_guess)