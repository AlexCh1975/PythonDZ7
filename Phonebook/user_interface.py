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
        
    # if len(data) > 0: 
    #     return data
    # data.update('search', 'search')
    # input("Поиск по фамилии: ")
    #return 
    
# Ввод данных в phonebook

def ui_interface():
    print("-----------------------------------------")
    person = []
    print("Введите фамилию: ")
    surname = input()
    person.append(surname)
    print("Введмте имя: ")
    name = input()
    person.append(name)
    print("Введите номер телефона: ")
    phone = input()
    person.append(phone)
    print("Описание: ")
    comment = input()
    person.append(comment)

    return person

# def print_user(data):
#     print("-----------------------------------------")
#     print(data)