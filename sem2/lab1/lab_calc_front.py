import tkinter as tk
import tkinter.messagebox as mb
import lab_calc_back as back


def correct_input(num):
    i = 0
    if i < len(num) and num[i] in "0123456789":
        while i < len(num) and num[i] in "0123456789":
            i += 1
        if i == len(num):
            return True
        if i < len(num) and num[i] == ".":
            i += 1
            if i < len(num) and num[i] in "0123456789":
                while i < len(num) and num[i] in "0123456789":
                    i += 1
                if i < len(num):
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

    return True


def from_2_to_10(num):
    for i in num:
        if i not in "01.":
            mb.showerror(title="Ошибка", message="Некорректный символ: " + i)
            return
    if not(correct_input(num)):
        mb.showerror(title="Ошибка", message="Введенное число не соответствует формату вещественного числа")
        return

    res = back.from_2_to_10(num)

    entry.delete(0, len(entry.get()))
    entry.insert(0, str(res))


def from_10_to_2(num):
    for i in num:
        if i not in "0123456789.":
            mb.showerror(title="Ошибка", message="Некорректный символ: " + i)
            return
    if not (correct_input(num)):
        mb.showerror(title="Ошибка", message="Введенное число не соответствует формату вещественного числа")
        return

    res = back.from_10_to_2(num)

    entry.delete(0, len(entry.get()))
    entry.insert(0, res)


info = "Автор: Тузов Даниил \nГруппа: ИУ7-22Б \nНазначение программы: Прогррамма является простым переводчиком " \
       "из 2 СС в 10 СС и обратно"
root = tk.Tk()
root.title("Калькулятор")
entry = tk.Entry(width=14, highlightthickness=3, font="Arial 30")
entry.grid(row=0, column=0, columnspan=4)
tk.Button(height=5, width=10, text="1", command=lambda: entry.insert(len(entry.get()), "1")).grid(row=1, column=0)
tk.Button(height=5, width=10, text="2", command=lambda: entry.insert(len(entry.get()), "2")).grid(row=1, column=1)
tk.Button(height=5, width=10, text="3", command=lambda: entry.insert(len(entry.get()), "3")).grid(row=1, column=2)
tk.Button(height=5, width=10, text="4", command=lambda: entry.insert(len(entry.get()), "4")).grid(row=2, column=0)
tk.Button(height=5, width=10, text="5", command=lambda: entry.insert(len(entry.get()), "5")).grid(row=2, column=1)
tk.Button(height=5, width=10, text="6", command=lambda: entry.insert(len(entry.get()), "6")).grid(row=2, column=2)
tk.Button(height=5, width=10, text="7", command=lambda: entry.insert(len(entry.get()), "7")).grid(row=3, column=0)
tk.Button(height=5, width=10, text="8", command=lambda: entry.insert(len(entry.get()), "8")).grid(row=3, column=1)
tk.Button(height=5, width=10, text="9", command=lambda: entry.insert(len(entry.get()), "9")).grid(row=3, column=2)
tk.Button(height=5, width=10, text="0", command=lambda: entry.insert(len(entry.get()), "0")).grid(row=4, column=0)
tk.Button(height=5, width=10, text=".", command=lambda: entry.insert(len(entry.get()), ".")).grid(row=4, column=1)
tk.Button(height=5, width=10, text="info",
          command=lambda: mb.showinfo(title="Информация", message=info)).grid(row=4, column=3)
tk.Button(height=5, width=10, text="del", command=lambda: entry.delete(len(entry.get()) - 1)).grid(row=4, column=2)
tk.Button(height=5, width=10, text="clear", command=lambda: entry.delete(0, len(entry.get()))).grid(row=1, column=3)
tk.Button(height=5, width=10, text="2->10", command=lambda: from_2_to_10(entry.get())).grid(row=2, column=3)
tk.Button(height=5, width=10, text="10->2", command=lambda: from_10_to_2(entry.get())).grid(row=3, column=3)
root.mainloop()
