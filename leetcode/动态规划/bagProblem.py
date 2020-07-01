# value
v = [3, 4, 5, 8, 10]
# weight
w = [2, 3, 4, 5, 9]
# total weight
W = 20

dp = [[0 for i in range(len(v) + 1)] for _ in range(W + 1)]

for i in range(1, len(v) + 1):
    for j in range(W + 1):
        if j >= w[i - 1]:
            dp[j][i] = max(dp[j - w[i - 1]][i - 1] + v[i - 1], dp[j][i - 1])
        else:
            dp[j][i] = dp[j][i - 1]
p = dp[W][len(v)]
print(p)
