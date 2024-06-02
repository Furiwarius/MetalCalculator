from app.enitities.metal import Metal
import enum

class Details(enum.Enum):
    '''
    Детали запроса
    '''

    ALL = "all value"


class metalCRUD():
    '''
    Класс для взаимодействия с бд
    '''


    def get_name_profiles(self) -> list:
        '''
        Получить список названий профилей
        '''


    def get_by_number(self, number:str) -> Metal:
        '''
        Получить метал по номеру профиля
        '''

    
    def get_by_name(self, name:str, GOST = Details.ALL) -> list:
        '''
        Получить список металла по имени профиля

        Получает название профиля (например, двутавр или швеллер и тд.)
        Выдает весь список имеющихся профилей по умолчанию.
        Если уточнить нужный гост, то выдаст результат
        только по этому нормативному документу.
        '''