from numpy import arange

def f(x):
    return x**2 - 3*x + 1

solutions = []

for x in arange(-100, 100, 0.001):
    if abs(f(x)) < 0.001:
        solutions.append(x)

if solutions:
    print("方程式的解為:", solutions)
else:
    print("未找到解")
