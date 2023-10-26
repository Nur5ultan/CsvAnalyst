# Программа анализа .csv файлов

import tkinter as tk
from tkinter.scrolledtext import ScrolledText as st
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import os
import pandas as pd

#  Создание главного окна
window = tk.Tk()
window.geometry("550x550")
window.title("Программа анализа .csv файлов")

# Создание меток вывода
lbl_00 = tk.Label(text="Файл:")
lbl_00.grid(row=0, column=0, padx=10, pady=10, sticky="e")

lbl_01 = tk.Label(text="")
lbl_01.grid(row=0, column=1, sticky="w")

lbl_10 = tk.Label(text="Строк:")
lbl_10.grid(row=1, column=0, padx=10, pady=10, sticky="e")

lbl_11 = tk.Label(text="")
lbl_11.grid(row=1, column=1, sticky="w")

lbl_20 = tk.Label(text="Столбцов:")
lbl_20.grid(row=2, column=0, padx=10, pady=10, sticky="e")

lbl_21 = tk.Label(text="")
lbl_21.grid(row=2, column=1, sticky="w")

# Создание текстового вывода
output_text = st(height=22, width=50)
output_text.grid(row=3, column=1, padx=10, pady=10, sticky="w")


# Диалог открытия файла
def do_dialog():
    my_dir = os.getcwd()
    name = fd.askopenfilename(initialdir=my_dir)
    return name


# Обработка csv файла при помощи pandas
def pandas_read_csv(file_name):
    df = pd.read_csv(file_name, header=None, sep=";")
    count_rows = df.shape[0]
    count_columns = df.shape[1]
    lbl_11["text"] = count_rows
    lbl_21["text"] = count_columns
    return df


# Выборка столбца в список
def get_column(df, column_ix):
    count_rows = df.shape[0]
    lst = []
    for i in range(count_rows):
        lst.append(df.iat[i, column_ix])
    return lst


# Обработчик нажатия кнопки
def process_btn():
    file_name = do_dialog()
    lbl_01["text"] = file_name
    df = pandas_read_csv(file_name)
    lst = get_column(df, 2)
    for item in lst:
        output_text.insert(tk.END, str(item) + os.linesep)
    mb.showinfo(title=None, message="Готово")


# Создание кнопки
btn = tk.Button(window, text="Прочитать файл", command=process_btn)
btn.grid(row=4, column=1)


# Запуск цикла mainloop
window.mainloop()
