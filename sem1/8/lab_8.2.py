# Тузов Даниил ИУ7-12Б
# Переставляет местами строки с наибольшим и наименьшим количеством
# отрицательных элементов

while True:
    # Ввод данных
    n = int(input("Введите количество строк: "))
    m = int(input("Введите количество столбцов: "))
    data = [] * n
    for i in range(n):
        a = [0] * m
        for j in range(m):
            a[j] = int(input(f'Введите {j + 1}-й элемент {i + 1}-й строки: '))
        data.append(a)

    print("Искомая матрица:")
    # Подсчет отступа для элемента
    size = 0
    for i in range(n):
        for j in range(m):
            size = max(size, len(str(data[i][j])))

    # Вывод исходной матрицы
    for i in range(n):
        for j in range(m):
            print(f'{data[i][j]:<{size}}', end=' ')
        print()
    print()

    # Поиск индексов строк с наибольшим и наименьшим количеством отрицательных элементов
    ind1 = ind2 = mx = -1
    mn = m + 1
    for i in range(n):
        col = 0
        for j in range(m):
            if data[i][j] < 0:
                col += 1

        if ind2 == -1 or col > mx:
            mx = col
            ind2 = i
        if ind1 == -1 or col < mn:
            mn = col
            ind1 = i

    # Меняем строки местами
    data[ind1], data[ind2] = data[ind2], data[ind1]

    # Выводим измененную матрицу
    print("Матрица: ")
    for i in range(n):
        for j in range(m):
            print(f'{data[i][j]:<{size}}', end=' ')
        print()
    print()

