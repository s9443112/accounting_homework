from sympy import Symbol, symbols, solve, Eq, diff
from numpy import linspace
import matplotlib.pyplot as plt
import numpy as np

x_max = 5
x_min = -5

x = linspace(x_min,x_max,100)

y1 = x**2
y2 = 5*x - 1


X = Symbol('X')
f = X**2 - 5*X + 1
print(solve(f,X))
xmin,xmax = solve(f,X)

plt.figure(figsize=(12,6),dpi=100)
idx = np.argwhere(np.diff(np.sign(y1 - y2)) != 0)
plt.text(x[idx[0]],y1[idx[0]],str(xmin)+str(xmin**2))
plt.text(x[idx[1]],y1[idx[1]],str(xmax)+str(xmax**2))
plt.plot(x[idx], y1[idx], '*')


plt.xlim(x_min, x_max)


plt.plot(x, y1, 'k')
plt.plot(x, y2, 'k')
plt.show()


