# Тузов Даниил ИУ7-12Б
# Поиск наиболее длинной возрастающей последовательности отрицательных чисел,
# модуль которых является простым числом

while True:
    # Ввод данных
    n = int(input("Введите размер списка: "))
    a = [0] * n
    for i in range(n):
        a[i] = int(input(f'Введите {i+1}-ый элемент: '))

    # Ищем индекс первого отрицуательного элемента, модуль которого является простым числом
    ind = -1
    for i in range(n):
        if a[i] < -1:
            dels = 0
            for j in range(2, int(abs(a[i]) ** 0.5) + 1):
                if abs(a[i]) % j == 0:
                    dels += 1
                    break

            if dels == 0:
                ind = i
                break

    # Если мы не нашли искомый элемент
    if ind == -1:
        print("Такой последовательности нет\n\n")
        continue

    col = mx_col = 1
    i = ind + 1
    # Алгоритм поиска наибольшей последовательности
    while i < n:
        dels = 0
        for j in range(2, int(abs(a[i])**0.5) + 1):
            if abs(a[i]) % j == 0:
                dels += 1
                break
        if a[i] > a[i - 1] and dels == 0 and a[i] < -1:
            col += 1
        else:
            if mx_col < col:
                mx_col = col
                ind = i - col
            if a[i] < -1 and dels == 0:
                col = 1
            else:
                col = 0

        i += 1

    # Условие для последней операции
    if mx_col < col:
        mx_col = col
        ind = i - col

    # Вывод последовательности
    print("Искомая последовательность: ", a[ind:ind + mx_col:1])
    print()

