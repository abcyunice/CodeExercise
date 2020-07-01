from math import sqrt

def getsum2(n):
    return n * (n + 1) * (2 * n + 1) // 6

ans = 0
sqrt_N = int(sqrt(N))

for i in range(1, sqrt_N + 1):
    ans += getsum2(N // i) - getsum2(sqrt_N)
    ans += N // i * i ** 2

print(ans)