# Модуль добавления данных

p  = []
path_file = ''

def init(data, path_f):
    global p
    global path_file
    p = data
    path_file = path_f

def seve_file_p():
   
    # if not path.exists('phone_book.csv'):
        # with open('phone_book.csv', 'r', encoding='utf-8') as file:
        #     person = file.readlines()
            # person = file.readlines()[-2].split(',')
            # person = file.readlines()[-2].strip(',').split()
            # print(person)
            # person[0] = int(person[0])
            # person[0] += 1
    
        # count = 1
    with open(path_file, 'a', encoding='utf-8') as file:
            file.write(f'{p[0]}, {p[1]}, {p[2]}, {p[3]}, {p[4]}')
            file.write('\n')