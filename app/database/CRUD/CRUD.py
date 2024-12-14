from app.enitities.metal import Metal
from sqlalchemy import create_engine
from app.database.tables.tables import Base
from app.database.tables.tables import IBeamTable, ChannelTable
from app.database.tables.tables import PipeTable, ProfileTable
from sqlalchemy.orm import Session
import enum



class Details(enum.Enum):
    '''
    Детали запроса
    '''

    ALL = "all value"



class MetalCRUD():
    '''
    Класс для взаимодействия с бд
    '''
    
    # строка подключения
    sqlite_database = "sqlite:///app/database/MetalLibrary/MetalLibrary.db" 


    def __init__(self) -> None:

        self.engine = create_engine(self.sqlite_database, echo=False)
        Base.metadata.create_all(bind=self.engine)

        self.table_dict = {
            "ibeam": IBeamTable,
            "channel": ChannelTable,
            "pipe": PipeTable,
            "profile": ProfileTable
        }



    def get_name_profiles(self) -> list:
        '''
        Получить список названий профилей
        '''
        return list(self.table_dict.keys())



    def get_by_number(self, number:str, name:str) -> Metal:
        '''
        Получить метал по номеру профиля и имени профиля
        (Только для швеллеров и двутавров)
        '''

        table = self.table_dict.get(name)

        with Session(autoflush=False, bind=self.engine) as db:
            result = db.get(table, number)
        
        return result


    
    def get_by_name(self, name:str, GOST = Details.ALL) -> list:
        '''
        Получить список металла по имени профиля

        Получает название профиля (например, двутавр или швеллер и тд.)
        Выдает весь список имеющихся профилей по умолчанию.
        Если уточнить нужный гост, то выдаст результат
        только по этому нормативному документу.
        '''

        table = self.table_dict.get(name)

        if GOST is Details.ALL:
            with Session(autoflush=False, bind=self.engine) as db:
                result = db.query(table.profile_number).all()
        
        return result