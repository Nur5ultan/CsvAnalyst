# Программа анализа .csv файлов

from distutils.cygwinccompiler import check_config_h
from re import T
import tkinter as tk
from tkinter.scrolledtext import ScrolledText as st
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import os
import pandas as pd
from tomlkit import item

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


# Если в этом поле имя, пусть вернет True
def meet_name(field):
    checkfor = [
        "Вера",
        "Анатолий",
        "Мария",
        "Артём",
        "Алексей",
        "Валерия",
        "Наталья",
        "Оксана",
        "Галина",
        "Марина",
        "Вероника",
        "Виталий",
        "Борис",
        "Диана",
        "Ева",
    ]
    for s in checkfor:
        if s in str(field):  # Нашлось
            return True
    # Ничего не нашлось
    return False


# Если в этом списке многие элементы содержат имя, пусть вернет True
def list_meet_name(fields_list):
    counter_total = 0
    counter_meet = 0
    for list_item in fields_list:
        counter_total += 1
        if meet_name(list_item):
            counter_meet += 1
    # Конец подсчёта
    ratio = counter_meet / counter_total
    if ratio > 0.1:
        return True, ratio
    # Не набралось нужного количество совпадений
    return False, ratio


# Если в этом поле дата в формате AM/PM, пусть вернет True
def meet_date_am_pm(field):
    checkfor = [" AM", " PM"]
    for s in checkfor:
        if s in str(field):  # Нашлось!
            return True
    # Ничего не совпало
    return False


# Если в этом списке многие элементы содержат дату в формате AM/PM, пусть вернет True
def list_meet_data_am_pm(fields_list):
    counter_total = 0
    counter_meet = 0
    for list_item in fields_list:
        counter_total += 1
        if meet_date_am_pm(list_item):
            counter_meet += 1
    # Конец подсчёта
    ratio = counter_meet / counter_total
    if ratio > 0.5:
        return True, ratio
    # Не набралось нужного количество совпадений
    return False, ratio


# Пройти все столбцы
def check_all_columns(df):
    columns_count = df.shape[1]
    for i in range(columns_count):  # от 0 до columns_count-1
        lst = get_column(df, i)
        # Первый критерий
        result = list_meet_name(lst)
        if result[0]:
            output_text.insert(
                tk.END,
                "В столбце "
                + str(i + 1)
                + " предположительно содержится имя."
                + os.linesep,
            )
            output_text.insert(
                tk.END,
                "Процент совпадений "
                + "{:.2f}".format(result[1] * 100)
                + "%."
                + os.linesep
                + os.linesep,
            )
            continue  # Все нашли, можно идти к следующему столбцу

        # Второй критерий
        result_2 = list_meet_data_am_pm(lst)
        if result_2[0]:
            output_text.insert(
                tk.END,
                "В столбце "
                + str(i + 1)
                + " предположительно содержится дата в формате AM/PM."
                + os.linesep,
            )
            output_text.insert(
                tk.END,
                "Процент совпадений "
                + "{:.2f}".format(result_2[1] * 100)
                + "%."
                + os.linesep
                + os.linesep,
            )
            continue  # Все нашли, можно идти к следующему столбцу

        # Cоответствия критериям не найдено
        output_text.insert(
            tk.END,
            "Предположений для столбца "
            + str(i + 1)
            + " не найдено."
            + os.linesep
            + os.linesep,
        )


# Обработчик нажатия кнопки
def process_btn():
    file_name = do_dialog()
    lbl_01["text"] = file_name
    df = pandas_read_csv(file_name)
    check_all_columns(df)
    mb.showinfo(title=None, message="Готово")


# Создание кнопки
btn = tk.Button(window, text="Прочитать файл", command=process_btn)
btn.grid(row=4, column=1)


# Запуск цикла mainloop
window.mainloop()
