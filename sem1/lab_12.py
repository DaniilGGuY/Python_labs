# Тузов Даниил ИУ7-12Б
# Текстовый процессор

# Выравнивание по левому краю
def left_way(arr):
    for i in range(len(arr)):
        while arr[i].find("  ") != -1:
            arr[i] = arr[i].replace("  ", " ")

    for i in range(len(arr)):
        if arr[i][0] == " ":
            arr[i] = arr[i].replace(" ", "", 1)

    for i in range(len(arr)):
        if arr[i][len(arr[i]) - 1] == " ":
            arr[i] = arr[i][:len(arr[i])-1]


# Выравнивание по правому краю
def right_way(arr):
    left_way(arr)
    mx = 0
    for i in range(len(arr)):
        mx = max(mx, len(arr[i]))

    for i in range(len(arr)):
        arr[i] = (mx - len(arr[i])) * " " + arr[i]


# Выравнивание по ширине
def mid_way(arr):
    left_way(arr)
    mx = 0
    for i in range(len(arr)):
        mx = max(mx, len(arr[i]))

    for i in range(len(arr)):
        space_col = 0
        for j in range(len(arr[i])):
            if arr[i][j] == ' ':
                space_col += 1

        past = len(arr[i])
        if space_col != 0:
            arr[i] = arr[i].replace(' ', ' ' + ((mx - past) // space_col * ' '))
            arr[i] = arr[i].replace(' ' * ((mx - past) // space_col + 1), ' ' * ((mx - past) // space_col + 2),
                                    (mx - past) % space_col)
        else:
            arr[i] = arr[i] + ' ' * (mx - past)


# Удаление слова
def del_word(arr, word_):
    for i in range(len(arr)):
        s = ""
        j = 0
        while True:
            if j == len(arr[i]):
                if word_ == s:
                    if j - 1 - len(s) > 0:
                        arr[i] = arr[i][:j-1-len(s)]
                    else:
                        arr[i] = ""
                break
            elif arr[i][j].isalpha():
                s += arr[i][j]
            else:
                if word_ == s:
                    if j == len(s):
                        arr[i] = arr[i].replace(s, '', 1)
                        j -= len(s)
                    else:
                        arr[i] = arr[i][:j-len(s)-1] + arr[i][j:]
                        j -= len(s) + 1
                s = ""
            j += 1


# Замена слова
def replace_word(arr, old, new):
    for i in range(len(arr)):
        s = ""
        j = 0
        while True:
            if j == len(arr[i]):
                if old == s:
                    arr[i] = arr[i][:j - len(s)] + new
                break
            elif arr[i][j].isalpha():
                s += arr[i][j]
            else:
                if old == s:
                    arr[i] = arr[i][:j - len(s)] + new + arr[i][j:]
                    j += (len(new) - len(old)) - 1
                s = ""
            j += 1


# Вычисление выражения
def calculate(arr):
    for k in range(len(arr)):
        arr[k] += " "
    i = 0
    while i < len(arr):
        result = term = rep = 0
        begin = sign = -1
        for j in range(len(arr[i])):
            if arr[i][j].isdigit():
                if begin == -1:
                    begin = j
                term = term * 10 + int(arr[i][j])
            elif arr[i][j] == '+' or arr[i][j] == '-':
                if begin != -1:
                    rep = 1
                else:
                    begin = j
                if sign == -1:
                    result = term
                elif sign == 1:
                    result = result + term
                else:
                    result = result - term
                sign = (arr[i][j] == '+')
                term = 0
            else:
                if begin != -1:
                    if sign == -1:
                        result = term
                    elif sign == 1:
                        result = result + term
                    else:
                        result = result - term

                    if rep == 1:
                        arr[i] = arr[i][:begin] + str(result) + arr[i][j:]
                        i -= 1
                        break

                    result = term = rep = 0
                    begin = sign = -1
        i += 1

    for k in range(len(arr)):
        arr[k] = arr[k][:len(arr[k]) - 1]


# Удаление предложения
def del_sent(arr):
    arr[len(arr) - 1] += " "
    for k in range(len(arr)):
        arr[k] += " "

    i = ind = col = num = 0
    min_col = -1
    while i < len(arr):
        for j in range(len(arr[i]) - 1):
            if arr[i][j] != ' ' and arr[i][j + 1] == ' ':
                col += 1
            elif arr[i][j] == ' ' and j > 0 and (arr[i][j - 1] in ".?!"):
                if min_col == -1:
                    min_col = col
                elif min_col > col:
                    min_col = col
                    ind = num
                col = 0
                num += 1
        i += 1

    i = num = 0
    s = ""
    while i < len(arr):
        for j in range(len(arr[i])):
            if num == ind:
                s += arr[i][j]

            if arr[i][j] == ' ' and j > 0 and (arr[i][j - 1] in ".!?"):
                num += 1
        i += 1

    print("Искомое предложение:", s + "\n")

    i = num = 0
    while i < len(arr):
        j = 0
        while j < len(arr[i]):
            if arr[i][j] in ".!?":
                num += 1
            if num == ind:
                if j + 1 < len(arr[i]):
                    arr[i] = arr[i][:j] + arr[i][j+1:]
                else:
                    arr[i] = arr[i][:j]
                j -= 1
            j += 1
        i += 1

    for i in range(len(arr)):
        arr[i] = arr[i].rstrip()


# Проверка на то, что слово не содержит пробельных символов
def check_space(word):
    if len(word) == 0:
        return False
    for i in range(len(word)):
        if word[i] == ' ':
            return False

    return True


# Исходный текст
text = ["Мы стоим в девяти километрах от фронта. Вчера нас сменили, и теперь, набив желудок белыми бобами с",
        "говядиной, все сыты и довольны. Каждый 10+2 сумел даже запастись на вечер полным котелком и вдобавок получить",
        "       двойной паек колбасы и хлеба, а это уже кое-что. Давненько такого не бывало: красномордый кашевар",
        "предлагает жратву; каждого, кто проходит мимо, подзывает 11-3 взмахом черпака и накладывает щедрую порцию. Он",
        "в полном отчаянии, потому что знать не знает, как бы 4+5-1 опорожнить походную кухню. Тьяден и Мюллер",
        "  раздобыли несколько умывальных тазиков, и он наполнил их вровень с краями, про запас. Тьяден поступает",
        "так от ненасытности, Мюллер – из осторожности. Куда у Тьядена. все это девается, для всех загадка. Он был",
        "и остается тощим как 2+1-12 селедка. 2+1-12+9-1+0+0-1."]
while True:
    # Вывод меню
    try:
        state = int(input('''0 - Завершение программы
1 - Выровнять текст по левому краю
2 - Выровнять текст по правому краю
3 - Выровнять текст по ширине
4 - Удаление всех вхождений заданного слова
5 - Замена одного слова другим во всём тексте
6 - Вычисление арифметического выражения
7 - Удаление из текста первого предложения с наименьшим количеством слов

Введите номер команды: '''))
    except ValueError:
        print("\nНомер команды - целое число\n")
        continue

    # Выбор и обработка действия
    if state == 0:
        break
    elif state == 1:
        left_way(text)
    elif state == 2:
        right_way(text)
    elif state == 3:
        mid_way(text)
    elif state == 4:
        word = input("Введите слово, которое хотите удалить: ")
        if not(check_space(word)):
            print("Слово не должно содержать пробельных символов. Попробуйте снова.\n")
            continue
        del_word(text, word)
    elif state == 5:
        old_word = input("Введите слово, которое хотите заменить: ")
        if not(check_space(old_word)):
            print("Слово не должно содержать пробельных символов. Попробуйте снова.\n")
            continue
        new_word = input("Введите слово, на которое хотите заменить: ")
        if not(check_space(new_word)):
            print("Слово не должно содержать пробельных символов. Попробуйте снова.\n")
            continue
        replace_word(text, old_word, new_word)
    elif state == 6:
        calculate(text)
    elif state == 7:
        del_sent(text)
    else:
        print("\nНомер должен лежать в отрезке от 0 до 7\n")
        continue

    # Вывод измененного текста
    for i in range(len(text)):
        print(text[i])
