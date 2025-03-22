import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__() #initialithe main window like in the previous one
        #window = QMainWindow()
        self.title = "PyQt Button"
        self.x=200 #or left
        self.y=200 #or top
        self.width=300
        self.height=300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('panda_bear_icon_153300.ico'))

        #In GUI Python, these buttons, textboxes, labels are called widgets
        self.button = QPushButton('Click me!', self)
        self.button.setToolTip("You've hovered over me")
        self.button.move(110,70) #button.move(x,y)

        self.button2 = QPushButton('Register', self)
        self.button2.setToolTip("This button does nothing.. yet..")  # Tooltip for the new button
        self.button2.move(110, 100)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())