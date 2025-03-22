import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon

class App(QMainWIndow):

    def __init__(self):
        super().__init__() #initializes the main window like in the previous one
        #window = QMainWindow()
        self.title = "First OOP GUI"
        self.iniTUI()

    def iniTUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(200,200,300,300)
        self.setWindowIcon(QIcon('panda_bear_icon_153300.ico')) # sets an icon
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = App()
    sys.exit(app.exec_())