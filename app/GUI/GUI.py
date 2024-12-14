import sys
from PyQt5.QtWidgets import QApplication, QWidget

# В дальнейшем будет удалено, тк настраиваться приложение будет через файл
setting = {"title":"MetalCalculator", "resize":(250, 150), "move":(300,300)}


class AppGUI():

    def __init__(self) -> None:

        self.app = QApplication(sys.argv)


class Window():
    
    def __init__(self) -> None:
        
        self.window = QWidget()

        self.read_setting()
        self.setting_window()
    

    def read_setting(self) -> None:
        '''
        Чтение настроек
        '''
        global setting
        
        self.resizeX = setting.get("resize")[0]
        self.resizeY = setting.get("resize")[1]
        self.moveX = setting.get("move")[0]
        self.moveY = setting.get("move")[1]
        self.title = setting.get("title")


    def setting_window(self) -> None:
        '''
        Настройка окна
        '''

        self.window.resize(self.resizeX, self.resizeY)
        self.window.move(self.moveX, self.moveY)
        self.window.setWindowTitle('Simple')
    

    def show(self) -> None:
        '''
        Показать окно
        '''
        self.window.show()

a = AppGUI()