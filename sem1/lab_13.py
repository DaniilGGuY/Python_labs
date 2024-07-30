# Тузов Даниил ИУ7-12Б
# База данных в текстовом файле

import os.path

filename = None


# Функция поиска максимального размера каждого поля для вывода БД
def lens_fields():
    lens = [0, 0, 0, 0]
    with open(filename, "r", encoding="cp1251") as f:
        while True:
            line = f.readline().split()
            if len(line) == 0:
                break

            lens[0] = max(lens[0], len(line[0]))
            lens[1] = max(lens[1], len(line[1]))
            lens[2] = max(lens[2], len(line[2]))
            lens[3] = max(lens[3], len(line[3]))
        f.close()
    return lens


# Проверка файла на соответствие шаблону БД
def check_temp():
    with open(filename, "r", encoding="cp1251") as f:
        while True:
            line = f.readline().split()
            if len(line) == 0:
                break
            if (len(line) != 4 or not(line[2].isdigit())) and line[len(line) - 1] != "\n":
                f.close()
                return False

    f.close()
    return True


# Добавить несколько записей в файл
def fill_data(col_, atr):
    with open(filename, atr, encoding="cp1251") as f:
        for i in range(col_):
            new_line = []
            surname = input("Введите фамилию: ")
            while surname.isspace():
                surname = input("Введите фамилию: ")
            new_line.append(surname)

            name = input("Введите имя: ")
            while name.isspace():
                name = input("Введите имя: ")
            new_line.append(name)

            while True:
                try:
                    age = int(input("Введите возраст: "))
                except ValueError:
                    print("\nОжидалось целое число\n")
                    continue
                new_line.append(str(age))
                break

            mail = input("Введите адрес электронной почты: ")
            while mail.isspace():
                mail = input("Введите адрес электронной почты: ")
            new_line.append(mail)

            f.write(" ".join(new_line))
            f.write("\n")

        f.close()


# Вывод БД
def printbase(lens):
    print("\nБаза данных в формате Фамилия|Имя|Возраст|Адрес электронной почты")
    print((sum(lens) + 13) * "-")
    with open(filename, "r", encoding='cp1251') as f:
        while True:
            line = f.readline().split()
            if len(line) == 0:
                break

            print(f'| {line[0]:^{lens[0]}} | {line[1]:^{lens[1]}} | {line[2]:^{lens[2]}} | {line[3]:^{lens[3]}} |')
        f.close()
    print((sum(lens) + 13) * "-")


# Поиск по 1 параметру
def find_1par(ind, par):
    print("\nРезультаты поиска:")
    with open(filename, "r", encoding="cp1251") as f:
        while True:
            line = f.readline().split()
            if len(line) == 0:
                break

            if line[ind] == par:
                print(*line)
    print()


# Поиск по 2 параметрам
def find_2par(ind1, ind2, par1, par2):
    print("\nРезультаты поиска:")
    with open(filename, "r", encoding="cp1251") as f:
        while True:
            line = f.readline().split()
            if len(line) == 0:
                break

            if line[ind1] == par1 and line[ind2] == par2:
                print(*line)
    print()


while True:
    try:
        state = int(input('''0 - Завершение программы
1 - Выбрать файл для работы
2 - Инициализировать базу данных
3 - Вывести содержимое базы данных
4 - Добавить запись в конец базы данных
5 - Поиск в базе данных по одному полю
6 - Поиск в базе данных по двум полям
Введите номер команды: '''))
    except ValueError:
        print("\nНомер команды - целое число\n")
        continue

    if state == 0:
        break
    elif state == 1:
        filename = input("\nВведите путь к файлу: ")
        if not(os.path.exists(filename)):
            print("\nТакого пути не существет\n")
            filename = None
            continue

        if not(check_temp()):
            print("\nФайл не соответствует шаблону базы данных\n")
            filename = None
            continue
    elif state == 2:
        try:
            filename = input("\nВведите путь к файлу: ")

            try:
                col = int(input("Введите количество строк в базе данных: "))
            except ValueError:
                print("Количество строк - целое число")
                continue

            fill_data(col, "w")
        except Exception:
            print("\nНекорректный путь к файлу\n")
            filename = None
            continue
    elif state == 3:
        if filename is None:
            print("\nФайл не выбран\n")
            continue

        lens_ = lens_fields()
        printbase(lens_)
    elif state == 4:
        if filename is None:
            print("\nФайл не выбран\n")
            continue

        fill_data(1, "a")
    elif state == 5:
        if filename is None:
            print("\nФайл не выбран\n")
            continue

        while True:
            try:
                state2 = int(input('''По какому параметру искать:
0 - назад
1 - фамилия
2 - имя
3 - возраст
4 - адрес электронной почты
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
                try:
                    par = str(int(input("Введите возраст: ")))
                except ValueError:
                    print("\nВозраст - число\n")
                    continue
            elif state == 4:
                ind = 3
                par = input("Введите адрес электронной почты: ")
            else:
                print("\nНомер должен лежать в отрезке от 0 до 4\n")
                continue

            find_1par(ind, par)
    elif state == 6:
        if filename is None:
            print("\nФайл не выбран\n")
            continue

        while True:
            try:
                state2 = int(input('''По какому первому параметру искать:
0 - назад
1 - фамилия
2 - имя
3 - возраст1
4 - адрес электронной почты
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
                try:
                    par1 = str(int(input("Введите возраст: ")))
                except ValueError:
                    print("\nВозраст - число\n")
                    continue
            elif state2 == 4:
                ind1 = 3
                par1 = input("Введите адрес электронной почты: ")
            else:
                print("\nНомер должен лежать в отрезке от 0 до 4\n")
                continue

            try:
                state3 = int(input('''По какому второму параметру искать:
0 - назад
1 - фамилия
2 - имя
3 - возраст
4 - адрес электронной почты
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
                try:
                    par2 = str(int(input("Введите возраст: ")))
                except ValueError:
                    print("\nВозраст - число\n")
                    continue
            elif state3 == 4:
                ind2 = 3
                par2 = input("Введите адрес электронной почты: ")
            else:
                print("\nНомер должен лежать в отрезке от 0 до 4\n")
                continue

            find_2par(ind1, ind2, par1, par2)
    else:
        print("\nНомер должен лежать в отрезке от 0 до 6\n")
        continue
