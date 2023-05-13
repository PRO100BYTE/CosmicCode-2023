distance = float(input("Введите расстояние в км: "))
speed = float(input("Введите скорость Лунохода-1 в км/земной день: "))
phase = int(input("Введите фазу Луны (1 - полнолуние, 2 - новолуние, 3 - первая четверть, 4 - последняя четверть): "))

if phase == 1:
    lunar_day_length = 14.75
elif phase == 2:
    lunar_day_length = 0
elif phase == 3 or phase == 4:
    lunar_day_length = 7.375

lunar_period_length = 29.5 # длительность лунного периода в земных сутках
lunar_day_start = 0 # начало светлой части лунного дня в земных сутках
earth_day_length = lunar_day_length / lunar_period_length # длительность земного дня в земных сутках
distance_traveled = 0 # пройденное расстояние в км
earth_days_passed = 0 # количество земных дней, прошедших с начала движения

while distance_traveled < distance:
    if earth_days_passed % earth_day_length == lunar_day_start:
        distance_traveled += speed
    earth_days_passed += 1

print(f"Луноход-1 проедет {distance} км за {earth_days_passed} земных дней.")