# Тузов Даниил ИУ7-12Б
# Вывод таблички и построение примитивного графика функции по значению аргумента

import math

while True:
    # Ввод данных

    t0 = float(input("Введите начальное значение аргумента: "))
    tn = float(input("Введите конечное значение аргумента: "))
    while t0 == tn:
        tn = float(input("Введите конечное значение не равное начальному: "))

    h = float(input("Введите шаг: "))
    while t0 < tn and h < 0:
        h = float(input("Введите положительный шаг: "))

    while t0 > tn and h > 0:
        h = float(input("Введите отрицательный шаг: "))

    if t0 > tn:
        t0, tn = tn, t0
        h = -h

    # Переменная для доп задания
    col = 0
    # Максимум и минимум функции
    p1_max = math.sin(t0) + 0.6 * t0 * math.cos(t0)
    p1_min = p1_max

    # Вывод таблички
    print("-------------------------------------")
    print("|     t     |     p1    |     p2    |")
    print("-------------------------------------")
    col_step = int((tn - t0) / h + 1)
    for i in range(col_step):
        t = t0 + i * h
        p1 = math.sin(t) + 0.6 * t * math.cos(t)
        p2 = t ** 3 - 5.09 * t ** 2 + 4.57 * t + 3.2

        p1_min = min(p1_min, p1)
        p1_max = max(p1_max, p1)

        if p1 - 0.2 >= 10**(-6) and 1.6 - p1 >= 10**(-6):
            col += 1

        print("|  {:<9.5g}|{:<11.5g}|{:<11.5g}|".format(t, p1, p2))
    print("-------------------------------------\n\n")

    # Ввод количества засечек
    x = int(input("Введите количество засечек (от 4 до 8) для построения графика p1: "))
    while not(4 <= x <= 8):
        x = int(input("Введите корректное количество засечек (от 4 до 8): "))
    print(' ' * 10, end='')
    # Шаг вывода засечки по OY
    step = (p1_max - p1_min) / (x - 1)
    # Полуинтервал. Окрестность точки
    interval = (p1_max - p1_min) / 80
    # Вывод текущего числа на OY
    printed = p1_min

    # Вывод первой строки графика
    for i in range(x):
        print(f'{printed:<{80 // (x - 1)}.{5}g}', end='')
        printed += step
    print()

    # Вывод графика
    for i in range(col_step):
        y = t0 + i * h
        print("{:<9.5g}".format(y), end='')
        d = math.sin(y) + 0.6 * y * math.cos(y)

        for j in range(81):
            if p1_min + interval * j <= d < p1_min + interval * (j + 1):
                print('*', end='')
            elif p1_min + interval * j <= 0 < p1_min + interval * (j + 1):
                print('|', end='')
            else:
                print(end='.')
        print()

    # Дополнительное задание
    print("\n{} значений p1 попавших в [0.2; 1.6]\n\n".format(col))
