# Импортируем модуль math
import math

# Проводим рассчеты
def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = side * math.sqrt(2)
    return perimeter, area, diagonal

# Вводим длину стороны квадрата
side_length = float(input("Введите длину стороны квадрата "))
perim, sq_area, diag = square(side_length)

# Выводим результат
print("Периметр:", perim)
print("Площадь:", sq_area)
print("Диагональ:", diag)

# Проверяем кортеж
result = square(side_length)
print(type(result))  # <class 'tuple'>
