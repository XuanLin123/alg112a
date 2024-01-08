import random

def hillClimbing(f, p, h=0.01):
    failCount = 0
    while failCount < 10000:
        fnow = f(*p) 
        p1, f1 = neighbor(f, p, h)
        if f1 >= fnow:
            fnow = f1
            p = p1
            print('p=', p, 'f(p)=', fnow)
            failCount = 0
        else:
            failCount += 1
    return p, fnow

def neighbor(f, p, h=0.01):
    # 產生 p 附近的隨機點
    p1 = [p_i + random.uniform(-h, h) for p_i in p]
    f1 = f(*p1)
    return p1, f1

def f(x, y, z):
    return -1 * (x**2 + y**2 + z**2)

result = hillClimbing(f, [2, 1, 3])
print("result: ", result)
