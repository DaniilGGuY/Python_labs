# Тузов Даниил ИУ7-12Б
# Добавление в бинарный файл удвоеного значения отрицательных элементов после самих отрицательных элементов

import struct as s

filename = "test.bin"
s_len = 4

while True:
    # Вводим данные
    try:
        n = int(input("Введите количество чисел в бинарном файле: "))
    except ValueError:
        print("\nОжидалось целое число\n")
        continue

    f = open(filename, "wb")
    for i in range(n):
        while True:
            try:
                el = int(input(f'Введите {i + 1}-й элемент: '))
            except ValueError:
                print("\nОжидалось целое число\n")
                continue
            f.write(s.pack("i", el))
            break
    f.close()

    # Выводим файл
    print("\nИсходный файл: ")
    f = open(filename, "rb")
    for i in range(n):
        print(s.unpack("i", f.read(4))[0], end=' ')
    f.close()

    # Добавляем удвоенные значения
    f = open(filename, "rb+")
    i_ = 0
    while i_ < n:
        f.seek(4 * i_)
        a = s.unpack("i", f.read(4))[0]
        if a >= 0:
            i_ += 1
        else:
            temp = f.read()
            f.seek(4 * (i_ + 1))
            f.write(s.pack("i", 2 * a))
            f.write(temp)
            i_ += 2
            n += 1
    f.close()

    # Выводим файл
    print("\nИзмененный файл: ")
    f = open(filename, "rb")
    for i in range(n):
        print(s.unpack("i", f.read(4))[0], end=' ')
    f.close()
    print()
