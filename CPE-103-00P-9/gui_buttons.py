import sys
drom PyQt5.QtWidgets import QWidget, QApplication, QQMainWindow, QPushButton
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self)
        super().__init__() #initialithe main window like in the previous one
        #window = QMainWindow()
        self.title = "PyQt Button"
        self.x=200 #or left
        self.y=200 #or top
        self.width=300
        self.height=300
        self.intTUI()

    def iniTUi(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('panda_bear_icon_153300.ico'))




