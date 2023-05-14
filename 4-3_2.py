# Функция для проверки пересечения двух прямоугольников
def intersect(rect1, rect2):
    # Получить координаты вершин прямоугольников
    x1, y1, x2, y2 = rect1
    x3, y3, x4, y4 = rect2
    # Проверить условие отсутствия пересечения
    if x2 <= x3 or x4 <= x1 or y2 <= y3 or y4 <= y1:
        return False
    else:
        return True

# Функция для генерации всех возможных комбинаций петалов
def combinations(petals):
    # Импортировать модуль itertools для работы с итераторами
    import itertools
    # Создать список для хранения комбинаций
    result = []
    # Для каждого количества петалов от 1 до длины списка
    for n in range(1, len(petals) + 1):
        # Добавить в список все комбинации длины n из списка петалов
        result += list(itertools.combinations(petals, n))
    # Создать новый список для хранения допустимых комбинаций
    valid_result = []
    # Для каждой комбинации петалов в списке
    for combo in result:
        # Создать переменную для хранения флага допустимости
        valid_flag = True
        # Для каждой пары петалов в комбинации
        for i in range(len(combo)):
            for j in range(i + 1, len(combo)):
                # Получить координаты вершин прямоугольников петалов
                x1, y1, x2, y2 = combo[i]
                x3, y3, x4, y4 = combo[j]
                # Проверить условие допустимости: петалы должны располагаться горизонтально или вертикально относительно друг друга и иметь одинаковую длину или ширину
                if not ((x1 == x3 or x2 == x4) and (y2 - y1 == y4 - y3) or (y1 == y3 or y2 == y4) and (x2 - x1 == x4 - x3)):
                    # Установить флаг допустимости в False и выйти из цикла
                    valid_flag = False
                    break
            # Если флаг допустимости установлен в False
            if not valid_flag:
                # Выйти из цикла
                break
        # Если флаг допустимости установлен в True
        if valid_flag:
            # Добавить комбинацию в новый список допустимых комбинаций
            valid_result.append(combo)
    # Вернуть новый список допустимых комбинаций
    return valid_result

# Функция для подсчета количества конфигураций расположения петалов
def count_configurations(petals):
    # Получить все возможные комбинации петалов
    combos = combinations(petals)
    # Создать переменную для хранения количества конфигураций
    count = 0
    # Для каждой комбинации петалов
    for combo in combos:
        # Создать переменную для хранения флага пересечения
        intersect_flag = False
        # Для каждой пары петалов в комбинации
        for i in range(len(combo)):
            for j in range(i + 1, len(combo)):
                # Если петалы пересекаются
                if intersect(combo[i], combo[j]):
                    # Установить флаг пересечения в True и выйти из цикла
                    intersect_flag = True
                    break
            # Если флаг пересечения установлен в True
            if intersect_flag:
                # Выйти из цикла
                break
        # Если флаг пересечения не установлен в True
        if not intersect_flag:
            # Увеличить количество конфигураций на 1
            count += 1
    # Вернуть количество конфигураций
    return count

# Считать входные данные и вызвать функцию подсчета конфигураций для каждого тестового случая

# Считать количество тестовых случаев N
N = int(input())

# Для каждого тестового случая
for _ in range(N):
    # Считать количество петалов M и список координат противоположных вершин прямоугольников петалов petals
    M = int(input())
    petals = list(map(int, input().split()))
    # Преобразовать список координат в список кортежей по четыре элемента в каждом (x1, y1, x2, y2)
    petals = [tuple(petals[i:i+4]) for i in range(0, len(petals), 4)]
    # Вызвать функцию подсчета конфигураций расположения петалов и вывести результат на экран
    print(count_configurations(petals))
