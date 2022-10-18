# Взаимодействие с пользователем

# Вабор состояния:
#   - Ввод данных
#   - Импорт из файла
#   - Экспорт в html 


def ui_menu():
    print("-----------------------------------------")
    data = {}
    print("Выберите операцию ('' - нет, 1 - да).")
    if len(data) > 0: return data
    else:
        label = input("Ввод данных: ")
        if label: data['input'] = 'input'
        
    if len(data) > 0: return data
    else:
        label = input("Импорт из файла: ")
        if label: data['import'] = 'import'
        
    if len(data) > 0: return data
    else:
        label = input("Экспорт в файл: ")
        if label: data['export'] = 'export'
    return data
    
# Ввод данных в phonebook

def ui_interface():
    print("-----------------------------------------")
    person = []
    
    while True:
        print("Введите фамилию: ")
        surname = input()
        if surname.isalpha() and len(surname) > 1:
            person.append(surname)
            break
        else: 
            print("Неверная фамилия!")

    while True:
        print("Введмте имя: ")
        name = input()
        if name.isalpha() and len(name) > 1:
            person.append(name)
            break
        else: 
            print("Неверное имя!")

    while True:
        print("Введите номер телефона: ")
        phone = input()
        if phone.isdigit() and 5 < len(phone) < 12:
            person.append(phone)
            break
        else: print("Неверный номер!")

    print("Описание: ")
    comment = input()
    person.append(comment)

    return person
