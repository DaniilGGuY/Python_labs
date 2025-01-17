# Тузов Даниил ИУ7-12Б
# Удаление элемента из списка с помощью любых средств

# Ввод данных
n = int(input("Введите размер списка: "))
a = [0] * n
for i in range(n):
    a[i] = int(input(f'Введите {i+1}-ый элемент: '))

while len(a) > 0:
    # Откуда удаляем
    ind = int(input("Введите индекс: "))
    while ind < 1 or ind > n:
        ind = int(input("Введите корректный индекс: "))

    # Удаление
    a.pop(ind - 1)
    n -= 1

    # Вывод списка
    print("Обновленный список: ", a)
    print("\n")
