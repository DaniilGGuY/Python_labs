# Тузов Даниил ИУ7-12Б
# База данных в бинарном файле

from struct import *
import os

s_format = '20s20s20sQ20s'  # формат строки
s_len = 92  # байтов в строке


# добавляет запись в файл
def add_line(filename):
    surname = input("Введите фамилию: ")
    while surname.isspace():
        surname = input("Введите фамилию: ")

    name = input("Введите имя: ")
    while name.isspace():
        name = input("Введите имя: ")

    fname = input("Введите отчество: ")
    while fname.isspace():
        fname = input("Введите отчество: ")

    while True:
        try:
            age = int(input("Введите возраст: "))
        except ValueError:
            print("\nОжидалось целое число\n")
            continue
        break

    mail = input("Введите адрес электронной почты: ")
    while mail.isspace():
        mail = input("Введите адрес электронной почты: ")

    s_ = pack(s_format, surname.encode('utf-8'), name.encode('utf-8'), fname.encode('utf-8'),
              age, mail.encode('utf-8'))

    file = open(filename, 'ab')
    file.write(s_)
    file.close()


# инициализация базы данных
def init(filename):
    try:
        file = open(filename, 'wb')
        try:
            n = int(input("Введите количеcтво запиcей: "))
        except ValueError:
            print("\nКоличество записей - целое число")

        for i in range(n):
            add_line(filename)
        file.close()
        return filename
    except Exception:
        print("\nВозникли проблемы с открытием или добавлением записей в файл\n")
        return None


# вывод базы данных
def print_(filename):
    print('-' * 156)
    print("|{:^30}|{:^30}|{:^30}|{:^30}|{:^30}|".format('Фамилия', 'Имя', 'Отчество', 'Возраст',
                                                        'Почта'))
    print('-' * 156)

    file = open(filename, 'rb')

    file.seek(0, 2)
    size = file.tell()
    file.seek(0)

    for i in range(size // s_len):
        s_ = file.read(s_len)
        s_ = list(unpack(s_format, s_))
        for j in range(5):
            if j != 3:
                s_[j] = s_[j].decode('utf-8')
                s_[0] = s_[0].replace('\x00', '')

        print("|{:^30}|{:^30}|{:^30}|{:^30}|{:^30}|".format(s_[0], s_[1], s_[2], s_[3], s_[4]))
        print('-' * 156)

    file.close()


# удаление cтроки из базы данных
def del_line(filename):
    try:
        n = int(input("Введите номер нужной cтроки: "))
        file = open(filename, 'rb+')

        file.seek(0, 2)
        size = file.tell()

        while n > (size // s_len) or n < 1:
            print("\nВ файле нет строки с таким номером\n")
            n = int(input("Введите номер нужной cтроки: "))
    except ValueError:
        print("\nОжидалось целое число\n")
        return

    n -= 1
    file.seek(0, 2)
    size = file.tell()
    pointer = n * s_len

    while pointer + s_len < size:
        file.seek(pointer + s_len)
        temp = file.read(s_len)
        file.seek(pointer)
        file.write(temp)
        pointer += s_len
    file.truncate(size - s_len)
    file.close()


# поиcк по одному полю
def find_1par(filename, ind, par):
    print('-' * 156)
    print("|{:^30}|{:^30}|{:^30}|{:^30}|{:^30}|".format('Фамилия', 'Имя', 'Отчество', 'Возраст',
                                                        'Почта'))
    print('-' * 156)

    file = open(filename, 'rb')

    file.seek(0, 2)
    size = file.tell()
    file.seek(0)

    for i in range(size // s_len):
        s_ = file.read(s_len)
        s_ = list(unpack(s_format, s_))
        for j in range(5):
            if j != 3:
                s_[j] = s_[j].decode('utf-8')
                s_[j] = s_[j].replace('\x00', '')

        if str(s_[ind]) == par:
            print("|{:^30}|{:^30}|{:^30}|{:^30}|{:^30}|".format(s_[0], s_[1], s_[2], s_[3], s_[4]))
            print('-' * 156)
    file.close()


# поиcк по двум полям
def find_2pars(filename, ind1, par1, ind2, par2):
    print('-' * 156)
    print("|{:^30}|{:^30}|{:^30}|{:^30}|{:^30}|".format('Фамилия', 'Имя', 'Отчество', 'Возраст',
                                                        'Почта'))
    print('-' * 156)

    file = open(filename, 'rb')

    file.seek(0, 2)
    size = file.tell()
    file.seek(0)

    for i in range(size // s_len):
        s_ = file.read(s_len)
        s_ = list(unpack(s_format, s_))
        for j in range(5):
            if j != 3:
                s_[j] = s_[j].decode('utf-8')
                s_[j] = s_[j].replace('\x00', '')

        if str(s_[ind1]) == par1 and str(s_[ind2]) == par2:
            print("|{:^30}|{:^30}|{:^30}|{:^30}|{:^30}|".format(s_[0], s_[1], s_[2], s_[3], s_[4]))
            print('-' * 156)
    file.close()


filename = None

# основной цикл с менюшкой
while True:
    try:
        state = int(input('''0 - Завершение программы
1 - Выбрать файл для работы
2 - Инициализировать базу данных
3 - Вывеcти cодержимое базы данных
4 - Добавить запиcь в базу данных
5 - Удалить запиcь из базы данных
6 - Поиcк по одному полю
7 - Поиcк по двум полям
Введите номер команды: '''))
    except ValueError:
        print("\nНомер команды - целое число\n")
        continue

    if state == 0:
        break
    elif state == 1:
        filename = input("\nВведите путь к файлу: ")
        if not (os.path.exists(filename)):
            print("\nТакого пути не существет\n")
            filename = None
            continue

        try:
            file = open(filename, "r")
            file.close()
        except Exception:
            print("\nФайл поврежден или не существует\n")
            filename = None
            continue
    elif state == 2:
        filename = input("\nВведите путь к файлу: ")
        filename = init(filename)
    elif state == 3:
        if filename is None:
            print("\nФайл не выбран\n")
            continue
        print_(filename)
    elif state == 4:
        if filename is None:
            print("\nФайл не выбран\n")
            continue
        add_line(filename)
    elif state == 5:
        if filename is None:
            print("\nФайл не выбран\n")
            continue
        del_line(filename)
    elif state == 6:
        if filename is None:
            print("\nФайл не выбран\n")
            continue

        while True:
            try:
                state2 = int(input('''По какому параметру искать:
0 - назад
1 - фамилия
2 - имя
3 - отчество
4 - возраст
5 - адрес электронной почты
Введите номер команды: 
'''))
            except ValueError:
                print("\nНомер команды - целое число\n")
                continue

            ind = -1
            par = ""
            if state2 == 0:
                break
            elif state2 == 1:
                ind = 0
                par = input("Введите фамилию: ")
            elif state2 == 2:
                ind = 1
                par = input("Введите имя: ")
            elif state2 == 3:
                ind = 2
                par = input("Введите отчество: ")
            elif state2 == 4:
                ind = 3
                try:
                    par = str(int(input("Введите возраст: ")))
                except ValueError:
                    print("\nВозраст - число\n")
                    continue
            elif state2 == 5:
                ind = 4
                par = input("Введите адрес электронной почты: ")
            else:
                print("\nНомер должен лежать в отрезке от 0 до 4\n")
                continue
            find_1par(filename, ind, par)
    elif state == 7:
        if filename is None:
            print("\nФайл не выбран\n")
            continue

        while True:
            try:
                state2 = int(input('''По какому первому параметру искать:
0 - назад
1 - фамилия
2 - имя
3 - отчество
4 - возраст
5 - адрес электронной почты
Введите номер команды: 
'''))
            except ValueError:
                print("\nНомер команды - целое число\n")
                continue

            ind1 = -1
            par1 = ""
            if state2 == 0:
                break
            elif state2 == 1:
                ind1 = 0
                par1 = input("Введите фамилию: ")
            elif state2 == 2:
                ind1 = 1
                par1 = input("Введите имя: ")
            elif state2 == 3:
                ind1 = 2
                par1 = input("Введите отчество: ")
            elif state2 == 4:
                ind1 = 3
                try:
                    par1 = str(int(input("Введите возраст: ")))
                except ValueError:
                    print("\nВозраст - число\n")
                    continue
            elif state2 == 5:
                ind1 = 4
                par1 = input("Введите адрес электронной почты: ")
            else:
                print("\nНомер должен лежать в отрезке от 0 до 4\n")
                continue

            try:
                state3 = int(input('''По какому второму параметру искать:
0 - назад
1 - фамилия
2 - имя
3 - отчество
4 - возраст
5 - адрес электронной почты
Введите номер команды: 
'''))
            except ValueError:
                print("\nНомер команды - целое число\n")
                continue

            ind2 = -1
            par2 = ""
            if state3 == 0:
                break
            elif state3 == 1:
                ind2 = 0
                par2 = input("Введите фамилию: ")
            elif state3 == 2:
                ind2 = 1
                par2 = input("Введите имя: ")
            elif state3 == 3:
                ind2 = 2
                par2 = input("Введите отчество: ")
            elif state3 == 4:
                ind2 = 3
                try:
                    par2 = str(int(input("Введите возраст: ")))
                except ValueError:
                    print("\nВозраст - число\n")
                    continue
            elif state3 == 5:
                ind2 = 4
                par2 = input("Введите адрес электронной почты: ")
            else:
                print("\nНомер должен лежать в отрезке от 0 до 4\n")
                continue
            find_2pars(filename, ind1, par1, ind2, par2)
    else:
        print("\nНомер должен лежать в отрезке от 0 до 7\n")
        continue
