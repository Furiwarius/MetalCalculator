from dataclasses import dataclass

@dataclass
class Metal():
    '''
    Абстрактный класс
    '''

    profile_number:str
    document:str
    weight:str   