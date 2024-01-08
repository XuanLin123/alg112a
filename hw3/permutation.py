def perm(n):
    p = []
    return permNext(n, p)

def permNext(n, p):
    i = len(p)
    if i == n:
        print(p) 
        return
    for x in range(n):
        if not x in p:
            p.append(x)
            permNext(n, p)
            p.pop()

# 自行輸入個數
n = int(input("請輸入排列個數："))
perm(n)
