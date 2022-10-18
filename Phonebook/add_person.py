# Модуль добавления данных

p  = []
path_file = ''

def init(data, path_f):
    global p
    global path_file
    p = data
    path_file = path_f

def seve_file_p():
   
    with open(path_file, 'a', encoding='utf-8') as file:
            file.write(f'{p[0]}, {p[1]}, {p[2]}, {p[3]}, {p[4]}')
            file.write('\n')