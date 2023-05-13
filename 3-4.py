n, T = map(int, input().split())

satellites = []
for i in range(n):
    m, max_m, t, dt = map(int, input().split())
    satellites.append((m, max_m, t, dt, i + 1))

satellites.sort(key=lambda s: s[2])

orbits = [[] for _ in range(n)]
total_mass = 0

for s in satellites:
    for i, orbit in enumerate(orbits):
        if s[0] <= s[1] and sum(m for m, _, _, _, _ in orbit) + s[0] <= s[1]:
            if s[2] + s[3] * len(orbit) <= T:
                orbit.append(s)
                total_mass += s[0]
                break

launch_order = [s[4] for orbit in orbits for s in orbit]

print(*launch_order)
print(total_mass)