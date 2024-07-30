# Тузов Даниил ИУ7-12Б
# Численные методы. Нахождение интеграла произвольной функции на произвольном заданном отрезке с произвольным
# разбиением двумя разными методами и сравнение результатов

import math as m


def func(x):  # Искомая функция
    return 3 * x ** 2 - m.sin(x)


def func_1(x):  # Первообразная искомой функции
    return x ** 3 + m.cos(x)


def isfloat(s):  # Проверка, что введенное число вещественное
    col_ = 0
    for i in range(len(s)):
        if s[i] == ".":
            col_ += 1
        if not (s[i].isdigit() or s[i] == "." and i != 0 and i != len(s) - 1 and col_ == 1):
            return 0
    return 1


def right_rect(a, b, n):  # Метод правых прямоугольников
    step = (b - a) / n
    sum_ = 0
    while a + step - b < 1e-5:
        sum_ += func(a + step) * step
        a += step

    return sum_


def trapezoid(a, b, n):  # Метод трапеций
    step = (b - a) / n
    sum_ = 0
    while a + step - b < 1e-5:
        sum_ += (func(a + step) + func(a)) * 0.5 * step
        a += step

    return sum_


def n_count(n, is_first, res_n, a, b):  # Итерационное увеличение количества участков разбиения для повышения точности
    eps = 10 ** (-3)
    if is_first:
        res_2n = right_rect(a, b, 2 * n)
        while not(abs(res_n - res_2n) < eps):
            res_n, n = res_2n, 2 * n
            res_2n = right_rect(a, b, 2 * n)
    else:
        res_2n = trapezoid(a, b, 2 * n)
        while not(abs(res_n - res_2n) < eps):
            res_n, n = res_2n, 2 * n
            res_2n = trapezoid(a, b, 2 * n)

    return n


def write_res(n1, n2, a, b, c, d):
    print(106 * "-")
    print("|                                  |   {:^28}   |   {:^28}   |".format(n1, n2))
    print(106 * "-")
    print("|   Метод правых прямоугольников   |  {:^30.6g}  |  {:^30.6g}  |".format(a, c))
    print(106 * "-")
    print("|          Метод трапеций          |  {:^30.6g}  |  {:^30.6g}  |".format(b, d))
    print(106 * "-", "\n")


while True:  # Основной цикл программы
    # Ввод начала участка интегрирования и проверка его на корректность
    try:
        a = float(input("Введите начало участка интегрирования: "))
    except ValueError:
        print("Ожидалось целое или вещественное число")
        continue

    # Ввод конца участка интегрирования и проверка его на корректность
    try:
        b = float(input("Введите конец участка интегрирования: "))
    except ValueError:
        print("Ожидалось целое или вещественное число")
        continue

    # Проверка, что конечный участок действительно больше начального
    if b <= a:
        print("Параметр начала интегрирования должен быть меньше параметра конца интегрирования\n")
        continue

    # Введение количества участков разбиения (N1) и проверка данных на корректность
    n1 = 1
    while True:
        s = input("Количество участков разбиения: ")
        while not (s.isdigit()):
            s = input("Введите целое положительное число: ")
        n1 = int(s)
        if n1 >= 1:
            break
        else:
            print("Количество участков разбиения должно быть больше нуля")

    # Находим значение площади двумя методами для N1 участков
    fst = right_rect(a, b, n1)
    sec = trapezoid(a, b, n1)

    # Введение количества участков разбиения (N2) и проверка данных на корректность
    n2 = 1
    while True:
        s = input("Количество участков разбиения: ")
        while not (s.isdigit()):
            s = input("Введите целое число: ")
        n2 = int(s)
        if n2 >= 1:
            break
        else:
            print("Количество участков разбиения должно быть больше нуля")

    # Находим значение площади двумя методами для N2 участков
    third = right_rect(a, b, n2)
    forth = trapezoid(a, b, n2)

    # Выводим табличку с результатами
    print("\nТабличка найденных площадей")
    write_res(n1, n2, fst, sec, third, forth)

    square = func_1(b) - func_1(a)  # Считаем значение интеграла по заданной первообразной

    # Находим абсолютную погрешность
    abs_1n1 = abs(fst - square)
    abs_1n2 = abs(third - square)
    abs_2n1 = abs(sec - square)
    abs_2n2 = abs(forth - square)

    # Выводим табличку с результатами
    print("\nАбсолютная погрешность")
    write_res(n1, n2, abs_1n1, abs_2n1, abs_1n2, abs_2n2)

    if square != 0:
        # Находим относительную погрешность для всех данных
        rel_1n1 = abs_1n1 / square * 100
        rel_1n2 = abs_1n2 / square * 100
        rel_2n1 = abs_2n1 / square * 100
        rel_2n2 = abs_2n2 / square * 100

        # Выводим табличку с результатами
        print("\nОтносительная погрешность в процентах")
        write_res(n1, n2, rel_1n1, rel_2n1, rel_1n2, rel_2n2)

    # Итерационное нахождения количества участков разбиения для менее точного метода
    if n2 > n1:
        if abs_2n2 < abs_1n2:
            new_n = n_count(n2, 1, third, a, b)
            print("\nДля метода правых прямоугольников количество участков разбиения:", new_n, "\n\n")
        else:
            new_n = n_count(n2, 0, forth, a, b)
            print("\nДля метода трапеций количество участков разбиения:", new_n, "\n\n")
    else:
        if abs_2n1 < abs_1n1:
            new_n = n_count(n1, 1, fst, a, b)
            print("\nДля метода правых прямоугольников количество участков разбиения:", new_n, "\n\n")
        else:
            new_n = n_count(n1, 0, sec, a, b)
            print("\nДля метода трапеций количество участков разбиения:", new_n, "\n\n")
