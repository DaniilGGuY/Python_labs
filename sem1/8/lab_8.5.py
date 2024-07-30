# Тузов Даниил ИУ7-12Б
# Находит максимум над главной диагональю и минимум под побочной

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

    # Поиск максимума над главной диагональю и минимума под побочной диагональю
    mx = mn = None
    for i in range(n):
        for j in range(i + 1, n):
            if mx is None or mx < data[i][j]:
                mx = data[i][j]

            if mn is None or mn < data[n - 1 - i][j]:
                mn = data[n - 1 - i][j]

    # Вывод максимума и минимума
    if mx is None:
        print("Максимума не существует")
    else:
        print("Максимум над главной диагональю:", mx)

    if mn is None:
        print("Минимума не существует", '\n')
    else:
        print("Минимум под побочной диагональю:", mn, '\n')

    