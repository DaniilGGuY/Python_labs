# Максимальное количество точек внутри окружности. Окружность по двум точкам (одна центр, одна на дуге окружности)
import tkinter as tk
import tkinter.messagebox as mb
import math as m


eps = 1e-8
arr_coord_points = list()
id_circ = int()
id_line = int()


def place_point(x1, y1, x2, y2, x3, y3):
    r1 = m.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    r2 = m.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
    if abs(r2 - r1) < eps:
        return 0
    elif r2 > r1:
        return -1
    else:
        return 1


def find_circ():
    x_1, y_1 = arr_coord_points[0]
    x_2, y_2 = arr_coord_points[1]
    max_col = -len(arr_coord_points)
    for i in range(0, len(arr_coord_points) - 1):
        for j in range(i + 1, len(arr_coord_points)):
            col = 0
            for k in range(0, len(arr_coord_points)):
                col += place_point(arr_coord_points[i][0], arr_coord_points[i][1], arr_coord_points[j][0],
                                   arr_coord_points[j][1], arr_coord_points[k][0], arr_coord_points[k][1])

            if col > max_col:
                x_1, y_1 = arr_coord_points[i]
                x_2, y_2 = arr_coord_points[j]
                max_col = col

    r = m.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)

    global id_circ, id_line
    canvas.delete(id_circ)
    canvas.delete(id_line)
    id_circ = canvas.create_oval(x_1 - r, y_1 - r, x_1 + r, y_1 + r, fill=None, width=4)
    id_line = canvas.create_line(x_1, y_1, x_2, y_2, width=2)



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


root = tk.Tk()
root.geometry("800x900")

coord_entry = tk.Entry(root)
coord_entry.place(x=0, y=0, width=400, height=50)

add_coord_button = tk.Button(root, text="Добавить координаты", command=add_coord)
add_coord_button.place(x=400, y=0, width=400, height=50)

canvas = tk.Canvas(root, width=800, height=800, bg='white')
canvas.place(x=0, y=50)

get_solve_button = tk.Button(root, text="Найти решение", command=find_circ)
get_solve_button.place(x=200, y=850, width=400, height=50)

root.bind('<Button-1>', add_coord_with_mouse)
root.bind('<Button-3>', add_coord_with_mouse)

root.mainloop()
