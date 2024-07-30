# Тузов Даниил ИУ7-12Б
# Повороты матрицы по часовой и против часовой стрелки

while True:
    # Ввод размера матрицы
    n = int(input("Введите размер матрицы: "))
    while n <= 0:
        n = int(input("Введите корректный размер: "))

    # Ввод матрицы
    data = [] * n
    for i in range(n):
        a = [] * n
        for j in range(n):
            a.append(int(input(f'Введите {j + 1}-й элемент {i + 1}-й строки: ')))
        data.append(a)

    # Печать исходной матрицы
    print("Исходная матрица\n")
    for i in range(n):
        for j in range(n):
            print("{:<10}".format(data[i][j]), end=' ')
        print()

    # Поворот по часовой
    for i in range((n + 1) // 2):
        for j in range(n // 2):
            data[i][j], data[n - 1 - j][i], data[j][n - 1 - i], data[n - 1 - i][n - 1 - j] = \
                data[n - 1 - j][i], data[n - 1 - i][n - 1 - j], data[i][j], data[j][n - 1 - i]

    # Печать повернутой матрицы
    print("Поворот на 90 градусов по часовой стрелке\n")
    for i in range(n):
        for j in range(n):
            print("{:<10}".format(data[i][j]), end=' ')
        print()

    # Поворот против часовой
    for i in range((n + 1) // 2):
        for j in range(n // 2):
            data[i][j], data[n - 1 - j][i], data[j][n - 1 - i], data[n - 1 - i][n - 1 - j] = \
                data[j][n - 1 - i], data[i][j], data[n - 1 - i][n - 1 - j], data[n - 1 - j][i]

    # Печать повернутой матрицы
    print("Поворот на 90 градусов против часовой стрелки\n")
    for i in range(n):
        for j in range(n):
            print("{:<10}".format(data[i][j]), end=' ')
        print()
    print()
    