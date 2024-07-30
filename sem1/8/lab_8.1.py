# Тузов Даниил ИУ7-12Б
# Поиск строки матрицы с наибольшим количеством нулевых элементов

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

    # Поиск искомой строки
    ind = mx_col = -1
    for i in range(n):
        col = 0
        for j in range(m):
            if data[i][j] == 0:
                col += 1

        if ind == -1 or col > mx_col:
            mx_col = col
            ind = i

    # Вывод искомой строки
    if ind == -1:
        print("Строка не была найдена", end='\n\n')
    else:
        print("Искомая строка:", *data[ind], end='\n\n')
