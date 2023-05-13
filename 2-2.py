n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if data[i][0] > data[j][0] and data[i][1] > data[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))