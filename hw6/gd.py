import random

# 函數 f 對變數 p[k] 的偏微分: df / dp[k]
def df(f, p, k, h=0.0001):
    p1 = p.copy()
    p1[k] = p[k] + h
    return (f(*p1) - f(*p)) / h

# 梯度：函數 f 在點 p 上的梯度
def grad(f, p):
    gp = p.copy()
    for k in range(len(p)):
        gp[k] = df(f, p, k)
    return gp

# 梯度下降法
def gradientDescent(f, p, lr=0.01, epochs=1000):
    for epoch in range(epochs):
        gradient = grad(f, p)
        p = [p_i - lr * g_i for p_i, g_i in zip(p, gradient)]
        print('Epoch:', epoch, ' p=', p, ' f(p)=', f(*p))
    return p, f(*p)

def f(x, y, z):
    # 這裡的函數 f 為 x, y, z 的三變數函數
    return x**2 + y**2 + z**2

# 隨機初始點
initial_point = [random.uniform(-10, 10) for _ in range(3)]

result = gradientDescent(f, initial_point)
print("最終結果:", result)
