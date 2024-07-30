# Тузов Даниил ИУ7-12Б
# Подсчитать в каждой строке матрицы D количество элементов, превышающих
# суммы элементов соответствующих строк матрицы Z. Разместить эти
# количества в массиве G, умножить матрицу D на максимальный элемент
# массива G. Напечатать матрицу Z, матрицу D до и после преобразования, а
# также массив G.

while True:
    # Ввод матрицы D
    nd = int(input("Введите количество строк матриц D и Z: "))
    while  nd <= 0:
        nd = int(input("Введите корректное значение: "))
    md = int(input("Введите количество столбцов матрицы D: "))
    while  md <= 0:
        md = int(input("Введите корректное значение: "))

    d = [] * nd
    for i in range(nd):
        a = [] * md
        for j in range(md):
            a.append(int(input(f'Введите {j + 1}-й элемент {i + 1}-й строки матрицы D: ')))
        d.append(a)

    # Ввод матрицы Z
    nz = nd
    mz = int(input("\nВведите количество столбцов матрицы Z: "))
    while mz <= 0:
        mz = int(input("Введите корректное значение: "))

    z = [] * nz
    for i in range(nz):
        b = [] * mz
        for j in range(mz):
            b.append(int(input(f'Введите {j + 1}-й элемент {i + 1}-й строки матрицы Z: ')))
        z.append(b)

    # Заполнение списка G
    g = [0] * nz
    for i in range(nz):
        sum_els = 0
        for j in range(mz):
            sum_els += z[i][j]
        col_els = 0
        for j in range(md):
            if sum_els < d[i][j]:
                col_els += 1
        g[i] = col_els

    # Вывод матрицы Z
    print("\nМатрица Z:")
    for i in range(nz):
        for j in range(mz):
            print("{:<10}".format(z[i][j]), end=' ')
        print()

    # Вывод матрицы D
    print("\nМатрица D:")
    for i in range(nd):
        for j in range(md):
            print("{:<10}".format(d[i][j]), end=' ')
        print()

    # Поиск максимума в списке G
    max_el = g[0]
    for i in g:
        max_el = max(max_el, i)

    # Вывод измененной матрицы D
    print("\nИзмененная матрица D:")
    for i in range(nd):
        for j in range(md):
            d[i][j] *= max_el
            print("{:<10}".format(d[i][j]), end=' ')
        print()

    # Вывод списка G
    print("\nСписок G:\n", *g, "\n\n")
