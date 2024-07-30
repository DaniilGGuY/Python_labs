# Тузов Даниил ИУ7-12Б
# Удаление всех отрицательных чисел из бинарного файла

import struct as s

filename = "test.bin"
s_len = 4

while True:
    # Вводим данные и записываем в файл
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

    # Удаляем все отрицательные числа
    f = open(filename, "rb+")
    i_ = j_ = col = 0
    while i_ < n and j_ < n:
        f.seek(4 * i_)
        a = s.unpack("i", f.read(4))[0]
        f.seek(4 * j_)
        b = s.unpack("i", f.read(4))[0]
        if a >= 0:
            col += 1
            i_ += 1
            j_ += 1
        else:
            if b < 0:
                j_ += 1
            else:
                f.seek(4 * i_)
                temp1 = f.read(4)
                f.seek(4 * j_)
                temp2 = f.read(4)
                f.seek(4 * i_)
                f.write(temp2)
                f.seek(4 * j_)
                f.write(temp1)
                j_ = i_
    f.seek(col * 4)
    f.truncate(f.tell())
    f.close()

    # Выводим файл
    print("\nИзмененный файл: ")
    f = open(filename, "rb")
    for i in range(col):
        print(s.unpack("i", f.read(4))[0], end=' ')
    f.close()
    print()
