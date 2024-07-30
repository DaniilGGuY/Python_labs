# Тузов Даниил ИУ7-12Б
# Гномья сортировка в бинарном файле

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

    # Сортируем числа в файле
    f = open(filename, "rb+")
    i_, j_ = 1, 2
    while i_ < n:
        f.seek(4 * (i_ - 1))
        a = s.unpack("i", f.read(4))[0]
        b = s.unpack("i", f.read(4))[0]
        if b < a:
            f.seek(4 * (i_ - 1))
            temp1 = f.read(4)
            temp2 = f.read(4)
            f.seek(4 * (i_ - 1))
            f.write(temp2)
            f.write(temp1)
            i_ -= 1
            if i_ == 0:
                i_ = j_
                j_ += 1
        else:
            i_ = j_
            j_ += 1
    f.close()

    # Выводим файл
    print("\nИзмененный файл: ")
    f = open(filename, "rb")
    for i in range(n):
        print(s.unpack("i", f.read(4))[0], end=' ')
    f.close()
    print()
