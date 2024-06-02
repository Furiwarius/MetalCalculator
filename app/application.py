from app.servise.calculator import Calculator

class App():
    '''
    Класс приложения
    '''

    def __init__(self) -> None:
        
        self.calc = Calculator()
    


    def run(self) -> None:
        '''
        Запустить
        '''