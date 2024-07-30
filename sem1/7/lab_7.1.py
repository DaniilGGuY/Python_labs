# Тузов Даниил ИУ7-12Б
# За O(n) удаляет все отрицательные элементы из списка

while True:
    # Ввод данных
    n = int(input("Введите размер списка: "))
    a = [0] * n
    for i in range(n):
        a[i] = int(input(f'Введите {i + 1}-й элемент: '))

    # Проверка размера списка на корректность
    if n <= 0:
        print("Список неправильной длины\n")
        continue

    # Методом двух указателей "прогоняем" все отрицательные элементы в конец
    i = j = 0
    while i < n and j < n:
        if a[i] >= 0:
            i += 1
            j += 1
        else:
            if a[j] < 0:
                j += 1
            else:
                a[i], a[j] = a[j], a[i]
                j = i

    # Удаляем отрицательные элементы, которые находятся в конце списка
    i = n - 1
    while a[i] < 0:
        a.pop()
        i -= 1
        if i == -1:
            break

    # Вывод списка
    for i in range(len(a)):
        print(f'{i + 1}-й элемент списка:', a[i])

    print()