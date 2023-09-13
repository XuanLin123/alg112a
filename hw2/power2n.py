# 方法 1
def power2n_1(n):
    return 2**n

print(f'method_1: {power2n_1(2)}')
print("------------")


# 方法 2a：用遞迴
def power2n_2a(n):
    m = 2
    for i in range(2, n + 1):
        m = power2n_2a(i-1)+power2n_2a(i-1)
    return m
print(f'method_2: {power2n_2a(3)}')
print("------------")


# 方法2b：用遞迴
def power2n_3b(n):
    h = 2
    for i in range(2, n + 1):
        h = 2*power2n_3b(i-1)
    return h
print(f'method_3: {power2n_3b(5)}')
print("------------")


# 方法 3：用遞迴+查表
def power2n_3(n, k={}):
    if n in k:
        return k[n]
    if n == 0:
        result = 1
    else:
        result = 2 * power2n_3(n - 1, k)
    k[n] = result
    return result

print(f'method_3: {power2n_3(7)}')
