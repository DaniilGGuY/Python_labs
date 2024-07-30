# Тузов Даниил ИУ7-12Б
# Реализация "Гномьей" сортировки

import random as r
import time as t


# Сортировка
def gnome(a, n):
    i, j, col = 1, 2, 0
    while i < n:
        if a[i] < a[i - 1]:
            col += 2
            a[i], a[i - 1] = a[i - 1], a[i]
            i = i - 1
            if i == 0:
                i = j
                j += 1
        else:
            i = j
            j = j + 1

    return col


while True:
    # Ввод и проверка на корректоность размеров массивов
    try:
        n1 = int(input("Введите размер массивов (N1): "))
    except ValueError:
        print("Ожидалось целое неотрицательное число\n")
        continue

    try:
        n2 = int(input("Введите размер массивов (N2): "))
    except ValueError:
        print("Ожидалось целое неотрицательное число\n")
        continue

    try:
        n3 = int(input("Введите размер массивов (N3): "))
    except ValueError:
        print("Ожидалось целое неотрицательное число\n")
        continue

    # Проверка на то, что размер больше нуля
    if n1 <= 0 or n2 <= 0 or n3 <= 0:
        print("Минимальный размер массивов 1!!!\n")
        continue

    # Создание и заполнение массивов для N1
    arr1 = list()
    arr2 = list()
    arr3 = list()
    for i in range(n1):
        arr1.append(i + 1)
        arr2.append(r.randint(0, n1 * 10))
        arr3.append(n1 - i)

    # Создание и заполнение массивов для N2
    arr4 = list()
    arr5 = list()
    arr6 = list()
    for i in range(n2):
        arr4.append(i + 1)
        arr5.append(r.randint(0, n2 * 10))
        arr6.append(n2 - i)

    # Создание и заполнение массивов для N3
    arr7 = list()
    arr8 = list()
    arr9 = list()
    for i in range(n3):
        arr7.append(i + 1)
        arr8.append(r.randint(0, n3 * 10))
        arr9.append(n3 - i)

    # Вычисление времени и подсчет количества перестановок для 1 массива
    t1 = t.time()
    k1 = gnome(arr1, n1)
    t1 = t.time() - t1

    # Вычисление времени и подсчет количества перестановок для 2 массива
    t2 = t.time()
    k2 = gnome(arr2, n1)
    t2 = t.time() - t2

    # Вычисление времени и подсчет количества перестановок для 3 массива
    t3 = t.time()
    k3 = gnome(arr3, n1)
    t3 = t.time() - t3

    # Вычисление времени и подсчет количества перестановок для 4 массива
    t4 = t.time()
    k4 = gnome(arr4, n2)
    t4 = t.time() - t4

    # Вычисление времени и подсчет количества перестановок для 5 массива
    t5 = t.time()
    k5 = gnome(arr5, n2)
    t5 = t.time() - t5

    # Вычисление времени и подсчет количества перестановок для 6 массива
    t6 = t.time()
    k6 = gnome(arr6, n2)
    t6 = t.time() - t6

    # Вычисление времени и подсчет количества перестановок для 7 массива
    t7 = t.time()
    k7 = gnome(arr7, n3)
    t7 = t.time() - t7

    # Вычисление времени и подсчет количества перестановок для 8 массива
    t8 = t.time()
    k8 = gnome(arr8, n3)
    t8 = t.time() - t8

    # Вычисление времени и подсчет количества перестановок для 9 массива
    t9 = t.time()
    k9 = gnome(arr9, n3)
    t9 = t.time() - t9

    # Вывод таблички
    print(123 * "-")
    print("|" + 34 * " " + "|" + "{:^28}|{:^28}|{:^28}|".format(n1, n2, n3))
    print(123 * "-")
    print("|" + 34 * " " + "|" + 3 * "    Время    | Перестановки |")
    print(123 * "-")
    print("|           Упорядоченный          |{:^13.5g}|{:^14}|{:^13.5g}|{:^14}|{:^13.5g}|{:^14}|".format(t1, k1, t4,
                                                                                                           k4, t7, k7))
    print(123 * "-")
    print("|             Случайный            |{:^13.5g}|{:^14}|{:^13.5g}|{:^14}|{:^13.5g}|{:^14}|".format(t2, k2, t5,
                                                                                                           k5, t8, k8))
    print(123 * "-")
    print("| Упорядоченный в обратном порядке |{:^13.5g}|{:^14}|{:^13.5g}|{:^14}|{:^13.5g}|{:^14}|".format(t3, k3, t6,
                                                                                                           k6, t9, k9))
    print(123 * "-")
