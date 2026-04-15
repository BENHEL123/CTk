import customtkinter as ctk

name = 'Аноним'

def handle_button_press():
    global root, entry, name
    text = entry.get()  # получаем введённую в поле строку в типе str
    print(f"Текст, введённый в поле: {text}")
    name = text
    entry.delete(0, "end")  # удаление текущего текста из поля

    # активируем текст-подсказку в поле и переводим фокус на окно
    entry._activate_placeholder()
    root.focus_set()
    change_text()
    # иначе в поле остался бы курсор - не очень красиво

    # если же после entry.delete(0, "end") нам надо было бы вставить какой-то новый текст в поле, то:
    # entry.insert(0, "Новый текст")

def change_text():
    global label
    label.configure(
        text=f'Привет, {name}')

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Виджет Entry")
root.geometry("500x500")
my_font = ctk.CTkFont(size=20)

label = ctk.CTkLabel(master=root)
label.configure(
    text=f'Привет, {name}',
    font=my_font,
    text_color='white'
)

# Entry - однострочное поле для ввода
entry = ctk.CTkEntry(master=root)
entry.configure(
    placeholder_text="Текст-подсказка",  # данный текст должен подсказывать, что нужно ввести в поле
    justify="center",  # расположение текста и подсказки будет по центру поля
    font=my_font,
    width=250  # ширина виджета в пикселях
)
# при надобности можно привязать к entry хендлер с помощью bind
# больше об Entry - в документации:
# https://customtkinter.tomschimansky.com/documentation/widgets/entry

button = ctk.CTkButton(master=root, text="Отобразить в консоль", font=my_font, command=handle_button_press)
# некоторые настройки можно указывать сразу при создании виджета, а не только в configure

label.pack(pady=50)
entry.pack(pady=50)
button.pack(pady=50)
# pack() располагает виджеты друг за другом, сверху вниз
# pady=100 - означает, что текущий виджет будет отталкиваться на 100 пикселей сверху и снизу
# от краёв окна или от границ другого виджета
# как видим, между двумя виджетами расстояние 100 + 100 = 200 пикселей
# если мы хотим, чтобы между этими двумя виджетами было расстоянии 100 пикселей, то:
# entry.pack(pady=(100, 50))  <- сверху отталкиваемся на 100, снизу - на 50
# button.pack(pady=(50, 100))  <- сверху отталкиваемся на 50, снизу - на 100
# в результате расстояние между ними получится 50 + 50 = 100 пикселей


root.mainloop()
