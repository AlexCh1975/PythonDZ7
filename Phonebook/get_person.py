# Модуль чдения данных из файла

path_file = ''

def init(path_f):
    global path_file
    path_file = path_f

def read_file_p():
    person = []
    with open(path_file, 'r', encoding='utf-8') as file:
        p = file.readlines()
        for i in range(len(p)):
            if not p[i] == '\n': person.append(p[i])
        # print(person)
    return person
