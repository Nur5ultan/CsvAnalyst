# Программа анализа .csv файлов

import tkinter as tk

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



# Запуск цикла mainloop
window.mainloop()
