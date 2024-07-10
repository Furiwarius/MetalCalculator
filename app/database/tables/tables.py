from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import  Column, Integer, String, Float



class Base(DeclarativeBase):
    '''
    Базовый класс для моделей
    '''
    pass



class IBeamTable(Base):
    '''
    Таблица для двутавров
    '''
    __tablename__ = "ibeam"
    
    profile_number = Column(String, primary_key=True, index=True)
    document = Column(String, nullable=False)
    weight = Column(Float, nullable=False)
    wall_heigth = Column(Float, nullable=False)
    shelf_width = Column(Float, nullable=False)



class ChannelTable(Base):
    '''
    Таблица для швеллеров
    '''
    __tablename__ = "channel"

    # У профилей швеллеров и двутавров много общих наименований,
    # Но тк у них есть другие разные параменты, принято решение
    # хранить данные в разных таблицах. И если понадобится 
    # внести дополнительные данные в БД это будет стоить меньших усилий
    profile_number = Column(String, primary_key=True, index=True)
    document = Column(String, nullable=False)
    weight = Column(Float, nullable=False)
    wall_heigth = Column(Float, nullable=False)
    shelf_width = Column(Float, nullable=False)



class PipeTable(Base):
    '''
    Таблица для труб с круглым профилем
    '''
    __tablename__ = "pipe"

    radius = Column(Float, primary_key=True, index=True)
    # Тощина стенки
    wall_thickness = Column(Float, nullable=False)


class ProfileTable(Base):
    '''
    Таблица для труба с квадратным или прямоугольным сечением
    '''
    __tablename__ = "profile"
 
    heigth = Column(Float, primary_key=True)
    weigth = Column(Float, primary_key=True)
    # Толщина стенки
    wall_thickness = Column(Float, nullable=False)