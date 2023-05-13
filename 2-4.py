n = int(input())
launches = {}
for i in range(n):
    y, s = map(int, input().split())
    if y not in launches:
        launches[y] = [s, 1]
    else:
        launches[y][0] += s
        launches[y][1] += 1

max_avg_success = 0
best_year = None
for y in launches:
    avg_success = launches[y][0] / launches[y][1]
    if avg_success > max_avg_success:
        max_avg_success = avg_success
        best_year = y
    elif avg_success == max_avg_success:
        best_year = min(best_year, y)

print(best_year)