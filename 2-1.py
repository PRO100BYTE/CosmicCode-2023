N = int(input())
x = y = m = 0
for _ in range(N):
    xi, yi, mi = map(int, input().split())
    x += xi * mi
    y += yi * mi
    m += mi
print(f'{x/m:.2f} {y/m:.2f}')