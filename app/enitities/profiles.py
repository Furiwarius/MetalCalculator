from dataclasses import dataclass
from app.enitities.metal import Metal


@dataclass
class Channel(Metal):
    '''
    Швеллер
    '''
    # Высота стенки
    wall_height:int
    # Ширина полки
    shelf_width:int


@dataclass
class IBeam(Channel):
    '''
    Двутавр
    '''


@dataclass
class Pipe(Metal):
    '''
    Труба круглая
    '''
    # Радиус трубы
    radius:int
    # Толщина стенки
    wall_thickness:float


@dataclass
class Profile(Metal):
    '''
    Труба профильная
    '''
    # Ширина профиля
    heigth:int
    # Высота профиля
    weigth:int
    # Толщина стенки
    wall_thickness:float