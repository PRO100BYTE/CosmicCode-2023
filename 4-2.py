n = int(input())
m = int(input())
limits = []
for i in range(m):
    t1, t2, k = map(int, input().split())
    limits.append((t1, t2, k))
times = []
for i in range(n):
    t = int(input())
    times.append(t)
times.sort()

def can_launch(num, t1, t2):
    cnt = 0
    for l in limits:
        if l[0] <= t2 and l[1] >= t1:
            cnt += min(num, l[2])
    return cnt >= num

left = 0
right = n
while left < right:
    mid = (left + right + 1) // 2
    ok = True
    for i in range(n - mid + 1):
        if not can_launch(mid, times[i], times[i + mid - 1]):
            ok = False
            break
    if ok:
        left = mid
    else:
        right = mid - 1

print(left)