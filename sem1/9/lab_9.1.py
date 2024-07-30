# Тузов Даниил ИУ7-12Б
# Заполняет матрицу по формуле. Определяет среднее арифметическое чисел каждой строки и количество элементов
# меньших среднего арифметического

import math

while True:
    # Ввод списка D
    n = int(input("Введите размер списка D: "))
    while n <= 0:
        n = int(input("Введите корректное значение размера: "))

    d = [0] * n
    for i in range(n):
        d[i] = float(input(f'Введите {i + 1}-й элемент списка D: '))

    # Ввод списка F
    m = int(input("Введите размер списка F: "))
    while m <= 0:
        m = int(input("Введите корректное значение размера: "))

    f = [0] * m
    for i in range(m):
        f[i] = float(input(f'Введите {i + 1}-й элемент списка F: '))

    # Формирование матрицы
    data = [] * n
    for i in range(n):
        a = [] * m
        for j in range(m):
            a.append(math.sin(d[i] + f[j]))
        data.append(a)

    # Вычисление среднего арифметического для каждой строки
    av = [0] * n
    for i in range(n):
        sum = col = 0
        for j in range(m):
            if data[i][j] > 0:
                sum += data[i][j]
                col += 1
        if col != 0:
            sum /= col
        av[i] = sum

    # Подсчет количества элементов меньших среднего арифметического в каждой строке
    l = [0] * n
    for i in range(n):
        for j in range(m):
            if data[i][j] < av[i]:
                l[i] += 1

    # Вывод всех данных
    for i in range(n):
        for j in range(m):
            print("{:<10.5g}".format(data[i][j]), end=' ')
        print("{:<10.5g} {:<10}".format(av[i], l[i]))
    print()
