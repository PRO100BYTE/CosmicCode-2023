M, V = map(int, input().split())
N = int(input())
satellites = []
for _ in range(N):
    m, v = map(int, input().split())
    satellites.append((m, v))

satellites.sort(key=lambda x: (x[0], x[1]))

count = 0
for satellite in satellites:
    if M - satellite[0] >= 0 and V - satellite[1] >= 0:
        count += 1
        M -= satellite[0]
        V -= satellite[1]
    else:
        break

print(count)