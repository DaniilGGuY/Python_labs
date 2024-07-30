# Тузов Даниил ИУ7-12Б
# Сформировать матрицу C путём построчного перемножения матриц A и B
# одинаковой размерности (элементы в i-й строке матрицы A умножаются на
# соответствующие элементы в i-й строке матрицы B), потом сложить все
# элементы в столбцах матрицы C и записать их в массив V. Напечатать матрицы
# A, B, C и массив V

while True:
    # Ввод матриц A и B одинаковой размерности
    n = int(input("Введите количество строк: "))
    while n <= 0:
        n = int(input("Введите корректное значение: "))
    m = int(input("Введите количество столбцов: "))
    while m <= 0:
        m = int(input("Введите корректное значение: "))

    A = [] * n
    for i in range(n):
        a = [] * m
        for j in range(m):
            a.append(int(input(f'Введите {j + 1}-й элемент {i + 1}-й строки матрицы A: ')))
        A.append(a)

    B = [] * n
    for i in range(n):
        b = [] * m
        for j in range(m):
            b.append(int(input(f'Введите {j + 1}-й элемент {i + 1}-й строки матрицы B: ')))
        B.append(b)

    # Заполнение матрицы C
    C = [] * n
    for i in range(n):
        c = [] * m
        for j in range(m):
            c.append(A[i][j] * B[i][j])
        C.append(c)

    # Заполнение массива V
    V = [0] * m
    for i in range(n):
        for j in range(m):
            V[j] += C[i][j]

    # Вывод матрицы A
    print("\nМатрица A:")
    for i in range(n):
        for j in range(m):
            print("{:<10}".format(A[i][j]), end=' ')
        print()

    # Вывод матрицы B
    print("\nМатрица B:")
    for i in range(n):
        for j in range(m):
            print("{:<10}".format(B[i][j]), end=' ')
        print()

    # Вывод матрицы C
    print("\nМатрица C:")
    for i in range(n):
        for j in range(m):
            print("{:<10}".format(C[i][j]), end=' ')
        print()

    # Вывод массива V
    print("\nМассив V:\n", *V, "\n\n")
    