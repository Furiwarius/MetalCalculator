from openpyxl import Workbook
from openpyxl import load_workbook

lib = load_workbook(filename='lib.xlsx')
l1 = (lib['l1']) #переменная с листом с именем 'l1'

'''
print(l1['A2'].value)
for n, i in enumerate(l1['A']):
    if i != None:
        print(n)
        print(i.value)'''

class metal (object):
    counter = 2 #это счетчик строк
                #начинается с 2, потому что 1 строка будет занята заголовками
    metal_list = [] #массив для создания имен профилей
    '''
    @classmethod
    def number_check(self, string_1): #сравнение введенных данных с библиотекой сечений
        for n, i in enumerate(l1['A']):
            if string_1 == i.value:
                return [string_1, l1['B{}'.format(n+1)].value]
        return False'''

    def __init__(self, profile):
        self.profile = profile                    #обязательным аргументом для создания класса является номер профиля 
        self.unit_weight = 0                      #задается после создания экземпляра
        self.length = 0                           #задается после создания экземпляра
        self.counter_number = metal.counter       #каждому экземпляру задается номер строки
        metal.counter+=1



def number_check(string_1): #Проверка профиля
    for n,i in enumerate(l1['A']):
        if string_1 == i.value:
            return [string_1, l1['B{}'.format(n+1)].value]
        
    #есть идея переноса в класс в функцию init
    #при неверном номере профиля будет запрашивать новый
    return False

def file_creation(): #функция для создания файла, позднее перекочует в класс metal
    exel_file = Workbook()
    file_name = input('введите имя файла: ')
    if file_name == '': exel_file_name = 'new_exel_file.xlsx'.format(file_name) #файл будет называться new_exel_file если ничего не введено
    else: exel_file_name = '{}.xlsx'.format(file_name) #даем название создаваемому файлу
    
    exel_file_1 = exel_file.active #создаем лист exel_file_1
    title_name = input('введите имя листа: ')
    if title_name == '': exel_file_1.title = 'basic' #в файле будет называется basic если ничего не введено
    else: exel_file_1.title = '{}'.format(title_name)

    exel_file_1['A1'] = 'Материал'
    exel_file_1['B1'] = 'Вес 1 м.п.'
    exel_file_1['C1'] = 'Количество м.п.'
    exel_file_1['D1'] = 'Масса'
    # тело для записи данных в файл
    for i in metal.metal_list:
        exel_file_1['A{}'.format(i.counter_number)] = i.profile
        exel_file_1['B{}'.format(i.counter_number)] = i.unit_weight
        exel_file_1['C{}'.format(i.counter_number)] = i.length
        exel_file_1['D{}'.format(i.counter_number)] = '=C{}*B{}'.format(i.counter_number, i.counter_number)

    #конец записи и сохранение файла
    print('Конец записи')
    exel_file.save(filename = exel_file_name)


while True:
    #0 - выход
    #1 - узнать вес нужного количества заданного номера
    #2-
    input_a = int(input('введите номер операции - '))
    if input_a == 0: 
        print('Выход')
        break
    if input_a == 1:
        while True:
            input_b = input('Введите нормер сечения - ')
            if input_b == 'конец': break
            elif input_b == 'показ':
                for i in metal.metal_list:
                    print('№ {} - {} м.п. весит - {} кг'.format(i.profile, i.length, i.unit_weight))
                continue
            elif input_b == 'запись':
                file_creation()
                break
            check = number_check(input_b)            
            if check != False:
                metal.metal_list.append(check[0]) #проблемы возникнуть не должно, тк мы сразу же после проверки добавляем элемент в список
                metal.metal_list[len(metal.metal_list)-1] = metal(metal.metal_list[len(metal.metal_list)-1])
                metal.metal_list[len(metal.metal_list)-1].unit_weight = check[1]
            else:
                print('Такого номер сечения нет в библиотеке - {}'.format(input_b))
                print('Или вы ввели некоректный номер')
                continue
            input_c = input('введите количество м.п. - ')
            metal.metal_list[len(metal.metal_list)-1].length = input_c
        
        
