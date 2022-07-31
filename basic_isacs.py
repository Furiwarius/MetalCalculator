import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook

lib = load_workbook(filename='lib.xlsx')
l1 = (lib['l1'])

counter = 1
'''
print(l1['A2'].value)
for n, i in enumerate(l1['A']):
    if i != None:
        print(n)
        print(i.value)'''


def number_check(string_1):
    print('это отправлено в функцию {}'.format(string_1))
    for n, i in enumerate(l1['A']):
        print(i.value)
        if string_1 == i.value:
            return [string_1, l1['B{}'.format(n+1)].value]
    return False


while True:
    #0 - выход
    #1 - узнать вес нужного количества заданного номера
    #2-
    input_a = int(input('введите номер операции - '))
    if input_a == 0: 
        print('Выход')
        break
    if input_a == 1:
        exel_file = Workbook()
        exel_file_name = 'exel_file.xlsx' #даем название создаваемому файлу
        exel_file_1 = exel_file.active #создаем лист exel_file_1
        exel_file_1.title = 'basic' #в файле будет называется basic
        exel_file_1['A{}'.format(counter)] = 'material'
        exel_file_1['B{}'.format(counter)] = 'weight 1 meter'
        exel_file_1['C{}'.format(counter)] = 'number of meters'
        exel_file_1['D{}'.format(counter)] = 'weight' 
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
        
        print('Конец записи')
        exel_file.save(filename = exel_file_name)