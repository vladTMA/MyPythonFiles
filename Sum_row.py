# Создаем функцию
def sum_row():
    start = float(input ("Введите первое число "))
    end = float(input ("Введите второе число "))

    # Проводим расчет суммы числового ряда
    if start > end:
        return 0.0
    total = 0.0
    current = start
    while current <= end:
        total += current
        current += 1.0

    return total

# Выводим результат
print("Сумма числового ряда", sum_row())

