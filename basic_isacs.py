from openpyxl import Workbook
from openpyxl import load_workbook

lib = load_workbook(filename='lib.xlsx')
l1 = (lib['l1'])

'''
print(l1['A2'].value)
for n, i in enumerate(l1['A']):
    if i != None:
        print(n)
        print(i.value)'''


def number_check(string_1):
    for n, i in enumerate(l1['A']):
        if string_1 == i.value:
            return [string_1, l1['B{}'.format(n+1)].value]
    return False

def file_creation(): #функция для создания файла
    global exel_file
    exel_file = Workbook()

    file_name = input('введите имя файла: ')
    global exel_file_name
    if file_name == '': exel_file_name = 'new_exel_file.xlsx'.format(file_name) #файл будет называться new_exel_file если ничего не введено
    else: exel_file_name = '{}.xlsx'.format(file_name) #даем название создаваемому файлу

    global exel_file_1
    exel_file_1 = exel_file.active #создаем лист exel_file_1
    title_name = input('введите имя листа: ')
    if title_name == '': exel_file_1.title = 'basic' #в файле будет называется basic если ничего не введено
    else: exel_file_1.title = '{}'.format(title_name)

    exel_file_1['A{}'.format(counter)] = 'Материал'
    exel_file_1['B{}'.format(counter)] = 'Вес 1 м.п.'
    exel_file_1['C{}'.format(counter)] = 'Количество м.п.'
    exel_file_1['D{}'.format(counter)] = 'Масса'
    # тело для записи данных в файл

    #конец записи и сохранение файла
    #print('Конец записи')
    #exel_file.save(filename = exel_file_name)


while True:
    #0 - выход
    #1 - узнать вес нужного количества заданного номера
    #2-
    input_a = int(input('введите номер операции - '))
    if input_a == 0: 
        print('Выход')
        break
    if input_a == 1:
        counter = 1 #счетчик строк в создаваемом файле
        file_creation()
        counter+=1

        while True:
            input_b = input('Введите нормер сечения - ')
            if input_b == 'конец': break
            check = number_check(input_b)
            if check != False:
                exel_file_1['A{}'.format(counter)] = check[0]
                exel_file_1['B{}'.format(counter)] = check[1]
            else:
                print('Такого номер сечения нет в библиотеке - {}'.format(input_b))
                print('Или вы ввели некоректный номер')
                continue

            input_c = input('введите количество м.п. - ')
            exel_file_1['C{}'.format(counter)] = input_c
            exel_file_1['D{}'.format(counter)] = '=C{}*B{}'.format(counter, counter)
            counter+=1
        
        print('Конец записи')
        exel_file.save(filename = exel_file_name)