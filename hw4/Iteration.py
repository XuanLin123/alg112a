def f(x):
    return x**2 - 3*x + 1

def g(x):
    return x - f(x) / (2*x - 3)  # 對應方程式的導數，這裡使用 f'(x) = 2*x - 3

def isolve(g, x):
    print("x=", x)
    for _ in range(100000):
        if abs(x - g(x)) < 0.001:
            return x
        x = g(x)
        print("x=", x)
    return x

x = isolve(g, 1)
print(f"x={x} f(x)={f(x)}")
