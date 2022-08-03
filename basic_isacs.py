from openpyxl import Workbook
from openpyxl import load_workbook

lib = load_workbook(filename='lib.xlsx')
l1 = (lib['l1']) #переменная с листом с именем 'l1'


class metal (object):
    counter = 2 #это счетчик строк
                #начинается с 2, потому что 1 строка будет занята заголовками
    metal_list = [] #массив для создания имен профилей
    
    @staticmethod
    def number_check(string_1): #сравнение введенных данных с библиотекой сечений
        sent_string = string_1
        send = []
        while True:
            for n, i in enumerate(l1['A']):
                if sent_string == i.value:
                    send = [sent_string, l1['B{}'.format(n+1)].value]
            if len(send) == 0:
                print('Введенный номер профиля отсутствует в библиотеке - {}'.format(string_1)) 
                sent_string = input('Введите исправлненный номер профиля - ') #ДОБАВИТЬ ВЫХОД из цикла В ДАЛЬНЕЙШЕМ ПОСЛЕ ТЕСТА
            else:
                return send
        

    def __init__(self, profile):
        verification = metal.number_check(profile)
        self.profile = verification[0]                    #обязательным аргументом для создания класса является номер профиля 
        self.unit_weight = verification[1]                      #задается после создания экземпляра
        self.length = input('Введите длину детали: ')                           #задается после создания экземпляра
        self.counter_number = metal.counter       #каждому экземпляру задается номер строки
        metal.counter+=1
    
    def __del__(self):
        pass



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
            check = metal(input_b)
            metal.metal_list.append(check)
        
        
