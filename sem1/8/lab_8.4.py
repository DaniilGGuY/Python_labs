# Тузов Даниил ИУ7-12Б
# Меняет местами столбцы с максимальной и минимальной суммой элементов

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

    # Поиск индексов столбцов с наибольшей и наименьшей суммой элементов
    ind1 = ind2 = -1
    mx = mn = 0
    for i in range(m):
        sum_ = 0
        for j in range(n):
            sum_ += data[j][i]

        if ind2 == -1 or mn > sum_:
            ind2 = i
            mn = sum_

        if ind1 == -1 or mx < sum_:
            ind1 = i
            mx = sum_

    # Меняем местами столбцы
    for i in range(n):
        data[i][ind1], data[i][ind2] = data[i][ind2], data[i][ind1]

    # Вывод исходной матрицы
    print("Матрица:")
    for i in range(n):
        for j in range(m):
            print(f'{data[i][j]:<{size}}', end=' ')
        print()
    print()
