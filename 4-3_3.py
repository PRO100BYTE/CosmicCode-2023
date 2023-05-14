# Функция для проверки пересечения двух прямоугольников
def intersect(r1, r2):
  # r1 и r2 - это кортежи из четырех координат (x1, y1, x2, y2)
  # Возвращаем True, если есть пересечение, и False в противном случае
  # Добавляем проверку на вертикальное расположение петалов
  return r1[0] < r2[2] and r1[2] > r2[0] and r1[1] < r2[3] and r1[3] > r2[1] and \
         not (r1[0] == r2[0] and r1[2] == r2[2]) and not (r1[1] == r2[1] and r1[3] == r2[3])

# Функция для подсчета количества возможных конфигураций расположения петалов
def count_configurations(petals):
  # petals - это список кортежей из четырех координат (x1, y1, x2, y2)
  # Возвращаем целое число - количество конфигураций
  n = len(petals) # количество петалов
  if n == 1: # если петал один, то конфигурация одна
    return 1
  elif n == 2: # если петал два, то конфигурация одна, если они пересекаются, иначе ноль
    return int(intersect(petals[0], petals[1]))
  elif n == 3: # если петал три, то нужно проверить все комбинации по два петала и все три вместе
    return int(intersect(petals[0], petals[1]) and intersect(petals[0], petals [2]) or \
               intersect(petals[0], petals [1]) and intersect (petals [1], petals [2]) or \
               intersect(petals[0], petals [2]) and intersect (petals [1], petals [2]) or \
               intersect(petals[0], petals [1]) and intersect (petals [0], petals [2]) and intersect (petals [1], petals [2]))
  elif n == 4: # если петал четыре, то нужно проверить все комбинации по три петала и все четыре вместе
    return int(intersect(petals[0], petals [1]) and intersect (petals [0], petals [2]) and intersect (petals [0], petals [3]) or \
               intersect(petals[0], petals [1]) and intersect (petals [0], petals [2]) and intersect (petals [1], petals [3]) or \
               intersect(petals[0], petals [1]) and intersect (petals [0], petals [3]) and intersect (petals [1], petals [2]) or \
               intersect(petals[0], petals [2]) and intersect (petals [0], petals [3]) and intersect (petals [1], petals [3]) or \
               intersect(petals[0], petals [3]) and intersect (petals [1], petals [2]) and intersect (petals [1], petals [3]) or \
               intersect(petals[1], petals [2]) and intersect (petals [1], petals [3]) and intersect (petals [2], petals [3]) or \
               intersect(petals[0], petals [1]) and intersect (petals [0], petals [2]) and intersect (petals [0], petals [3]) and \
               intersect(petals [1], petals [2]) and intersect (petals [1], petals [3]) and intersect (petals [2], petals [3]))
  else: # если петал больше четырех или меньше одного, то возвращаем ноль
    return 0

# Функция для чтения входных данных и вывода ответа
def main():
  # Читаем количество тестовых случаев
  N = int(input())
  # Для каждого тестового случая
  for _ in range(N):
    # Читаем количество петалов
    M = int(input())
    # Читаем координаты петалов и преобразуем их в кортежи
    try:
      # Пытаемся прочитать строку из стандартного ввода
      line = input()
      # Если строка не пустая, то разбиваем ее на числа и создаем кортежи
      if line:
        # Добавляем квадратные скобки вокруг генератора списка
        # Исправляем ошибку с лишними квадратными скобками вокруг списка кортежей
        petals = tuple(map(int, line.split())) for _ in range(M)
        # Подсчитываем количество конфигураций и выводим его
        print(count_configurations(petals))
      else:
        # Если строка пустая, то выводим сообщение об ошибке
        print("Недостаточно данных для тестового случая")
    except EOFError:
      # Если достигнут конец ввода, то выводим сообщение об ошибке
      print("Недостаточно данных для тестового случая")

# Вызываем главную функцию
if __name__ == "__main__":
  main()
