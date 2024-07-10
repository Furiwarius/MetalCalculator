from PyQt5.QtWidgets import QWidget, QLabel, QComboBox

class DropDownList():
    '''
    Выпадающий список для выбора профилей металла
    '''

    def __init__(self, window:QWidget) -> None:
        
        self.lbl = QLabel("Профиль", window)
        self.combo = QComboBox(window)
        
        
    def setting(self, items:list) -> None:
        
        self.combo.addItems(items)
        
        self.combo.move(100, 100)
        self.lbl.move(100, 150)

        self.combo.activated[str].connect(self.onActivated)
    

    def onActivated(self, text):

        self.lbl.setText(text)
        self.lbl.adjustSize()