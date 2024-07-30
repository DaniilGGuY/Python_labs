# Тузов Даниил ИУ7-12Б
# Заменяет все гласные английские буквы в матрицы символов на точки

while True:
    # Ввод матрицы D
    n = int(input("Введите количество строк матрицы D: "))
    while n <= 0:
        n = int(input("Введите корректное значение: "))
    m = int(input("Введите количество столбцов матрицы D: "))
    while m <= 0:
        m = int(input("Введите корректное значение: "))

    D = [] * n
    for i in range(n):
        a = [] * m
        for j in range(m):
            a.append(input(f'Введите {j + 1}-й элемент {i + 1}-й строки матрицы D: ')[0])
        D.append(a)

    # Вывод матрицы D
    print("\nИсходная матрица D:")
    for i in range(n):
        for j in range(m):
            print(D[i][j], end=' ')
        print()

    # Вспомогательная строка английских гласных
    help = "AEIOUYaeiouy"

    # Замена английских гласных на точки
    for i in range(n):
        for j in range(m):
            if D[i][j] in help:
                D[i][j] = "."

    # Вывод измененной матрицы
    print("\nИзмененная матрица D:")
    for i in range(n):
        for j in range(m):
            print(D[i][j], end=' ')
        print()
    print("\n")
    