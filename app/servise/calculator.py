from app.enitities.profiles import Metal


class Calculator():
    '''
    Калькулятор металла
    '''

    def __init__(self) -> None:
        
        self.profiles:list


    def add_profile(self, profile:Metal) -> None:
        '''
        Добавить профиль
        '''

        self.profiles.append(profile)
    

    def IndicateQuantity(self, index:int, value:float) -> None:
        '''
        Указать количество материала
        '''

        self.profiles[index].value = value


    def get_quote(self) -> list:
        '''
        Получить рассчет
        '''

        return [profile.weight*profile.value for profile in self.profiles]


    def update(self, index:int, new_value:int) -> None:
        '''
        Изменить количество материала
        '''

        self.profiles[index].value = new_value
    

    def delete(self, index:int) -> None:
        '''
        Удалить профиль из списка
        '''

        self.profiles.pop(index)