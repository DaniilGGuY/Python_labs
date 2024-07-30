# На плоскости задано множество точек. Провести прямую по данным точкам так,
# чтобы количество точек с одной стороны от прямой и с другой отличалось минимально.
import tkinter as tk
import tkinter.messagebox as mb


def point_place(x1, y1, x2, y2, x3, y3):
    # Находим коэффициенты уравнения прямой
    a = y2 - y1
    b = x1 - x2
    c = x2 * y1 - y2 * x1
    # Подставляем координаты точки в уравнение прямой
    res = a * x3 + b * y3 + c

    if abs(res) < 1e-8:
        return 0
    elif res < 0 < b or res > 0 > b:
        return -1
    else:
        return 1


def find_line():
    if len(arr_coord_points) < 2:
        mb.showerror("Ошибка количества точек", "Количество точек на графике должно быть минимум 2")
        return

    x_1, y_1 = arr_coord_points[0]
    x_2, y_2 = arr_coord_points[1]
    min_dist = len(arr_coord_points)
    for i in range(0, len(arr_coord_points) - 1):
        for j in range(i + 1, len(arr_coord_points)):
            dist = 0
            for k in range(0, len(arr_coord_points)):
                dist += point_place(arr_coord_points[i][0], arr_coord_points[i][1], arr_coord_points[j][0],
                                    arr_coord_points[j][1], arr_coord_points[k][0], arr_coord_points[k][1])

            if abs(dist) < min_dist:
                x_1, y_1 = arr_coord_points[i]
                x_2, y_2 = arr_coord_points[j]
                min_dist = abs(dist)

    a = y_2 - y_1
    b = x_1 - x_2
    c = x_2 * y_1 - y_2 * x_1

    x_1 = 0
    y_1 = c / -b
    x_2 = 800
    y_2 = (a * 800 + c) / -b

    global id_line
    canvas.delete(id_line)
    id_line = canvas.create_line(x_1, y_1, x_2, y_2, fill='green', width=4, smooth=True)


def insert_unique(arr, el):
    is_unique = True
    for i in arr:
        if i == el:
            is_unique = False
            break

    if is_unique:
        arr.insert(0, el)


def add_coord():
    try:
        x, y = coord_entry.get().split()
        x = int(x)
        y = int(y)
        if x > 800 or y > 800 or x < 0 or y < 0:
            mb.showerror("Ошибка ввода координат", "Координаты должны быть двумя числами в интервале от 0 до 800")
            return

        canvas.create_oval(x-2, y-2, x+2, y+2, fill='black')
        coord_entry.delete(0, tk.END)
        insert_unique(arr_coord_points, (x, y))
    except ValueError:
        mb.showerror("Ошибка ввода координат", "Координаты должны быть двумя числами в интервале от 0 до 800")


def add_coord_with_mouse(event):
    x = event.x
    y = event.y
    if not(x < 0 or x > 800 or y < 50 or y > 850):
        canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill='black')
        coord_entry.delete(0, tk.END)
        insert_unique(arr_coord_points, (x, y))


arr_coord_points = list()
id_line = int()

root = tk.Tk()
root.geometry("800x900")

coord_entry = tk.Entry(root)
coord_entry.place(x=0, y=0, width=400, height=50)

add_coord_button = tk.Button(root, text="Добавить координаты", command=add_coord)
add_coord_button.place(x=400, y=0, width=400, height=50)

canvas = tk.Canvas(root, width=800, height=800, bg='white')
canvas.place(x=0, y=50)

get_solve_button = tk.Button(root, text="Найти решение", command=find_line)
get_solve_button.place(x=200, y=850, width=400, height=50)

root.bind('<Button-1>', add_coord_with_mouse)
root.bind('<Button-3>', add_coord_with_mouse)

root.mainloop()
