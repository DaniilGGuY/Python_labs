import tkinter as tk
import tkinter.messagebox as mb
import tkinter.filedialog as fd
from PIL import Image, ImageTk
from numpy import array, uint8

# Рисует картинку
def show_pict(img):
    display = ImageTk.PhotoImage(img.resize((400, 400)))
    pict['image'] = display
    pict.image = display

# Выбрать файл с картинкой
def find_img():
    path = fd.askopenfilename(title="Выберите файл")
    if not path:
        return

    img = Image.open(path).convert("RGB")
    show_pict(img)

# Составляем матрицу пикселей нашего изображения в формате rgb
def bitmap(img):
    width, height = img.size

    matrix = []
    for h in range(height):
        matrix.append([])
        for w in range(width):
            matrix[-1].append(list(img.getpixel((w, h))))

    matrix = array(matrix, dtype = uint8)

    return matrix

# Кодируем изображение
def code(img):
    non_code = 0b11111110
    symb_bit = 0b10000000

    width, height = img.size
    matrix = bitmap(img)
    text = inp.get()
    if text == '':
        print("Пустая строка")
        return
    elif len(text) > width * height // 3 - 1:
        print("Слишком длинная строка")
        return

    arr = list(text.encode('ascii')) + [0]
    shape = matrix.shape
    matrix = matrix.ravel()
    i = 0
    while arr:
        if (i + 1) % 9 != 0 or i == 0:
            matrix[i] = matrix[i] & non_code | (arr[0] & symb_bit != 0)
            symb_bit >>= 1
        else:
            symb_bit = 0b10000000
            arr.pop(0)
        i += 1

    matrix.resize(shape)
    new_img = Image.fromarray(matrix)
    show_pict(new_img)
    print("Закодировано!")
    return

# Декодируем изображение
def decode(img):
    pixel_bit = 0b00000001
    i = symb_ascii = 0
    matrix = bitmap(img)
    shape = matrix.shape
    matrix = matrix.ravel()
    text = symb = ""

    while i < len(matrix) and symb != '\x00':
        if (i + 1) % 9 != 0 or i == 0:
            symb_ascii += (matrix[i] % 2) << (8 - (i + 1) % 9)
        else:
            symb = chr(symb_ascii)
            text += symb
            symb_ascii = 0
        i += 1

    text = text[:len(text)-1]
    print('Раскодировано!\n',text, sep='')


root = tk.Tk()
root.title("Стеганография")

inp = tk.Entry(root, width=70)
inp.grid(column=0, row=0, columnspan=3)

tk.Button(text="Выбрать файл", width=20, height=3, command=lambda : find_img()).grid(column=0, row=1)
tk.Button(text="Закодировать", width=20, height=3, command=lambda : code(ImageTk.getimage(pict.image))).grid(column=1, row=1)
tk.Button(text="Декодировать", width=20, height=3, command=lambda : decode(ImageTk.getimage(pict.image))).grid(column=2, row=1)

pict = tk.Label(root)
pict.grid(column=0, row=2, columnspan=3)

root.mainloop()