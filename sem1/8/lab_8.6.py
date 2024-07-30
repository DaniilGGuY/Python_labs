# Тузов Даниил ИУ7-12Б
# Транспонирование квадратной матрицы

while True:
    # Ввод данных
    n = int(input("Введите размер квадратной матрицы: "))
    data = [] * n
    for i in range(n):
        a = [0] * n
        for j in range(n):
            a[j] = int(input(f'Введите {j + 1}-й элемент {i + 1}-й строки: '))
        data.append(a)

    print("Искомая матрица:")
    # Подсчет отступа для элемента
    size = 0
    for i in range(n):
        for j in range(n):
            size = max(size, len(str(data[i][j])))

    # Вывод исходной матрицы
    for i in range(n):
        for j in range(n):
            print(f'{data[i][j]:<{size}}', end=' ')
        print()
    print()

    # Транспонирование
    for i in range(n):
        for j in range(i + 1, n):
            data[i][j], data[j][i] = data[j][i], data[i][j]

    # Выводим измененную матрицу
    print("Матрица: ")
    for i in range(n):
        for j in range(n):
            print(f'{data[i][j]:<{size}}', end=' ')
        print()
    print()