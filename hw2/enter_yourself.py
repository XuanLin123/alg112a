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


n = int(input("算指數(遞迴+查表): "))
print(f'2 的 {n} 次方: {power2n_3(n)}')
