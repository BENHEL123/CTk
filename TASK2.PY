import customtkinter as ctk


def handle_button_press():
    global root, entry1, entry2
    row1 = int(entry1.get())
    row2 = int(entry2.get())# получаем введённую в поле строку в типе str
    print(f"Текст, введённый в поле: {row1}, {row2}")  # удаление текущего текста из поля

    # активируем текст-подсказку в поле и переводим фокус на окно
    entry1._activate_placeholder()
    entry2._activate_placeholder()
    root.focus_set()

    text = (row1 + row2)
    entry3.configure(state="normal")  # разблокируем поле
    entry3.delete(0, "end")  # удалим оттуда старую строчку
    entry3.insert(0, text)  # вставим новую
    entry3.configure(state="readonly")  # снова заблокируем
    # иначе в поле остался бы курсор - не очень красиво

    # если же после entry.delete(0, "end") нам надо было бы вставить какой-то новый текст в поле, то:
    # entry.insert(0, "Новый текст")


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Виджет Entry")
root.geometry("500x500")
my_font = ctk.CTkFont(size=20)

# Entry - однострочное поле для ввода
entry1 = ctk.CTkEntry(master=root)
entry1.configure(
    placeholder_text="num1",  # данный текст должен подсказывать, что нужно ввести в поле
    justify="center",  # расположение текста и подсказки будет по центру поля
    font=my_font,
    width=250  # ширина виджета в пикселях
)
entry2 = ctk.CTkEntry(master=root)
entry2.configure(
    placeholder_text="num2",  # данный текст должен подсказывать, что нужно ввести в поле
    justify="center",  # расположение текста и подсказки будет по центру поля
    font=my_font,
    width=250  # ширина виджета в пикселях
)

entry3 = ctk.CTkEntry(master=root)
entry3.configure(
    placeholder_text="num2",  # данный текст должен подсказывать, что нужно ввести в поле
    justify="center",  # расположение текста и подсказки будет по центру поля
    font=my_font,
    width=250  # ширина виджета в пикселях
)


label = ctk.CTkLabel(master=root)
label.configure(
    text="+",
    font=my_font,
    text_color='white'
)

label2 = ctk.CTkLabel(master=root)
label2.configure(
    text="=",
    font=my_font,
    text_color='white'
)
# при надобности можно привязать к entry хендлер с помощью bind
# больше об Entry - в документации:
# https://customtkinter.tomschimansky.com/documentation/widgets/entry


entry3.insert(0, '')  # вставили в поле текст
entry3.configure(state="readonly")  # заблокировали поле
button = ctk.CTkButton(master=root, text="Отобразить в консоль", font=my_font, command=handle_button_press)
# некоторые настройки можно указывать сразу при создании виджета, а не только в configure

entry1.pack(pady=(50,20))
label.pack(pady=0)
entry2.pack(pady=(20, 20))
label2.pack(pady=0)
entry3.pack(pady=20)
button.pack(pady=(20,50))
# pack() располагает виджеты друг за другом, сверху вниз
# pady=100 - означает, что текущий виджет будет отталкиваться на 100 пикселей сверху и снизу
# от краёв окна или от границ другого виджета
# как видим, между двумя виджетами расстояние 100 + 100 = 200 пикселей
# если мы хотим, чтобы между этими двумя виджетами было расстоянии 100 пикселей, то:
# entry.pack(pady=(100, 50))  <- сверху отталкиваемся на 100, снизу - на 50
# button.pack(pady=(50, 100))  <- сверху отталкиваемся на 50, снизу - на 100
# в результате расстояние между ними получится 50 + 50 = 100 пикселей

root.mainloop()
