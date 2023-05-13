from math import gcd

n = int(input())
satellites = []
for i in range(n):
    t, f = map(int, input().split())
    satellites.append((t, f))

result = []
for i in range(n):
    for j in range(i+1, n):
        if (satellites[i][0] - satellites[j][0]) % gcd(satellites[i][1], satellites[j][1]) == 0:
            result.append((i+1, j+1))

print(len(result))
for pair in result:
    print(pair[0], pair[1])