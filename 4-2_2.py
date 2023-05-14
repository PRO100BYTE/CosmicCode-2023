n = int(input())
m = int(input())

# Считываем ограничения
constraints = []
for i in range(m):
    t1, t2, k = map(int, input().split())
    constraints.append((t1, t2, k))

# Считываем времена запуска ракет
launch_times = []
for i in range(n):
    t = int(input())
    launch_times.append(t)

# Сортируем времена запуска ракет
launch_times.sort()

# Подсчитываем количество запусков в соответствии с каждым ограничением
count = 0
for constraint in constraints:
    t1, t2, k = constraint
    launches_in_constraint = 0
    for launch_time in launch_times:
        if t1 <= launch_time <= t2:
            launches_in_constraint += 1
        if launches_in_constraint == k:
            break
    count += launches_in_constraint

# Выводим результат
print(count)