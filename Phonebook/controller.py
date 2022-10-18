# Модуль управления модулями

import user_interface as ui
import get_person as gp
import add_person as ap
import modul_export as mexp
import os

# Выбор состояния
def select():
    data = ui.ui_menu()
    for key in data:
        if key == 'input': ui_add_person()
        elif key == 'import': get_import()
        elif key == 'export': get_export()

# Старе меню
def ui_add_person():
    data = ui.ui_interface()
    add_person(data)

# Добавление данных в phonebook
def add_person(data):
    count = 1
    data.insert(0, count)
    path_f = 'phone_book.csv'

    if os.path.exists(path_f) and os.path.getsize(path_f) > 0:
        gp.init(path_f)
        person = gp.read_file_p()[-1]
        person = person.split(',')
        data[0] = int(person[0]) + 1
        ap.init(data, path_f) 
        ap.seve_file_p()
    else:
        ap.init(data, path_f) 
        ap.seve_file_p()

# Импорт из файла 
def get_import():
    path_read = 'test.txt'
    if os.path.exists(path_read) and os.path.getsize(path_read) > 0:
        gp.init(path_read)
        data = gp.read_file_p()
        for i in data:
            if i == '\n': data.remove(i)
        data.pop()
        for i in data:
            i = i[3:]
            i = i.split(',')
            add_person(i)
    else:
        print("Файл не существует или он пуст!")

# Экспорт в html
def get_export():
    path_f = 'phone_book.csv'
    if os.path.exists(path_f) and os.path.getsize(path_f) > 0:
        gp.init(path_f)
        data = gp.read_file_p()
        mexp.init(data)
        mexp.rendere_html()
    else:
        print("Файл пуст или не существует!")


