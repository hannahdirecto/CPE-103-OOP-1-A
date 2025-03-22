import sys
from PyQt5.QtWidgets import QWidget , QApplication, QLabel, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Account Registration System"
        self.x = 400
        self.y =  400
        self.width = 500
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('image.ico'))


        self.textboxlbl = QLabel ("Registration Form", self)
        self.textboxlbl.move(125, 10)
        self.textboxlbl.setFont(QFont("Courier ", 20, QFont.Bold))

        self.textboxlbl1 = QLabel("First Name:", self)
        self.textboxlbl1.move(50, 80)
        self.textboxlbl1.setFont(QFont("Courier ", 10, QFont.Bold))

        self.textbox = QLineEdit(self)
        self.textbox.move(175,75)
        self.textbox.resize(270, 30)
        self.textbox.setText("")

        self.textboxlbl2 = QLabel("Last Name:", self)
        self.textboxlbl2.move(50, 125)
        self.textboxlbl2.setFont(QFont("Courier ", 10, QFont.Bold))

        self.textbox = QLineEdit(self)
        self.textbox.move(175, 115)
        self.textbox.resize(270, 30)
        self.textbox.setText("")

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = App()
    sys.exit(app.exec())