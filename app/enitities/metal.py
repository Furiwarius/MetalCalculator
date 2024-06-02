from dataclasses import dataclass

@dataclass
class Metal():
    '''
    Металл
    '''

    id:int
    profile_number:str
    document:str
    weight:str