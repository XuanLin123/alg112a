from datetime import datetime
fib = [None]*10000
fib[0] = 0
fib[1] = 1

# 改用迴圈
def fibonacci(n):
    if n < 0: raise
    if not fib[n] is None: return fib[n]
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

n = int(input("enter index: "))
startTime = datetime.now()
print(f'fibonacci({n})={fibonacci(n)}')
endTime = datetime.now()
seconds = endTime - startTime
print(f'time:{seconds}')