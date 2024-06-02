from dataclasses import dataclass

@dataclass
class Metal():
    '''
    Абстрактный класс
    '''

    id:int
    profile_name:str
    profile_number:str
    document:str
    weight:str   