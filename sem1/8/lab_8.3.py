# Тузов Даниил ИУ7-12Б
# Поиск столбца с наибольшим количеством чисел, являющихся степенями двойки

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

    # Поиск искомого столбца
    ind = mx = -1
    for i in range(m):
        col = 0
        for j in range(n):
            el = data[j][i]
            flag = True
            if el > 0:
                while el != 1:
                    if el % 2 == 1:
                        flag = False
                        break
                    el /= 2

                if flag:
                    col += 1

        if ind == -1 or col > mx:
            mx = col
            ind = i

    # Вывод искомого столбца
    if mx == 0:
        print("Ни в одном столбце нет элемента, являющегося степенью двойки", end='\n\n')
    else:
        print("Искомый столбец:", end=' ')
        for i in range(n):
            print(data[i][ind], end=' ')
        print("\n")
