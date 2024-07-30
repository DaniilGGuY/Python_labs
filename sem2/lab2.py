import matplotlib.pyplot as plt
import numpy as np
import math as m


def func(x0):
   return m.sin(x0)


def diff_func(x0):
    return m.cos(x0)


def second_diff(x0):
    return (-1) * m.sin(x0)


def third_diff(x0):
    return (-1) * m.cos(x0)


def newton_meth(a, b, Nmax, eps, function, diff_function):
    delta = 1
    x = (a + b) / 2
    col = 0
    while delta > eps and col <= Nmax:
        new_x = x - function(x) / diff_function(x)
        delta = abs(function(x))
        x = new_x
        col += 1

    return x, col

roots = list()
extrs = list()
infls = list()
a = float(input())
b = float(input())
h = float(input())
Nmax = int(input())
eps = float(input())
table_data=[ ["Номер корня", "Отрезок", "Приближенное значение", "Значение функции", "Количество итераций"] ]
begin, end = a, b
while a < b:
    root = newton_meth(a, a + h, Nmax, eps, func, diff_func)
    extr = newton_meth(a, a + h, Nmax, eps, diff_func, second_diff)
    infl = newton_meth(a, a + h, Nmax, eps, second_diff, third_diff)

    if abs(func(root[0])) < eps and root[0] >= a and root[0] < a + h:
        #print(root[0], end='\n')
        roots.append(root[0])
        table_data.append([len(roots), f"[{a};{a + h}]", f"{root[0]:.6g}", f"{func(root[0]):.6g}", root[1]])

    if abs(diff_func(extr[0])) < eps and extr[0] >= a and extr[0] < a + h:
        #print(extr[0], end='\n')
        extrs.append(extr[0])

    if abs(third_diff(infl[0])) < eps and infl[0] >= a and infl[0] < a + h:
        #print(infl[0], end='\n')
        infls.append(infl[0])

    a += h

fig, ax = plt.subplots()
fig2, ax2 = plt.subplots()
step = (end - begin) / 1000
while begin < end:
    ax.scatter(begin, func(begin), s=3, color='black')
    begin += step

for i in roots:
    ax.scatter(i, func(i), s=30, color='red')

for i in extrs:
    ax.scatter(i, func(i), s=30, color='blue')

for i in infls:
    ax.scatter(i, func(i), s=30, color='yellow')

ax.set(title='График функции')
ax.grid()
table = ax2.table(cellText=table_data, loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 3)
ax2.axis('off')
plt.show()
plt.show()