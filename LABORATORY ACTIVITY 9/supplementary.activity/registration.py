import sys
from PyQt5.QtWidgets import QWidget , QApplication, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon, QFont


class  RegisterAccount(QWidget):

    def __init__(self):
        super().__init__()

        self.title = "Account Registration System"
        self.x = 400
        self.y =  400
        self.width = 500
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('image.ico'))
        self.setStyleSheet("background-color: #9AAABA;")

        #REGISTRATION FORM
        self.textboxlbl = QLabel("Account Registration", self)
        self.textboxlbl.move(100, 10)
        self.textboxlbl.setFont(QFont("Courier ", 20, QFont.Bold))

        #FIRST NAME
        self.textboxlbl1 = QLabel("First Name:", self)
        self.textboxlbl1.move(50, 80)
        self.textboxlbl1.setFont(QFont("Courier ", 10, QFont.Bold))
        self.textboxlbl1 = QLineEdit(self)
        self.textboxlbl1.move(190,75)
        self.textboxlbl1.resize(250, 30)
        self.textboxlbl1.setStyleSheet("background-color: white;")
        #LAST NAME
        self.textboxlbl2 = QLabel("Last Name:", self)
        self.textboxlbl2.move(50, 118)
        self.textboxlbl2.setFont(QFont("Courier ", 10, QFont.Bold))
        self.textboxlbl2 = QLineEdit(self)
        self.textboxlbl2.move(190, 110)
        self.textboxlbl2.resize(250, 30)
        self.textboxlbl2.setStyleSheet("background-color: white;")
        #USERNAME
        self.textboxlbl3 = QLabel("Username:", self)
        self.textboxlbl3.move(50, 154)
        self.textboxlbl3.setFont(QFont("Courier ", 10, QFont.Bold))
        self.textboxlbl3 = QLineEdit(self)
        self.textboxlbl3.move(190, 145)
        self.textboxlbl3.resize(250, 30)
        self.textboxlbl3.setStyleSheet("background-color: white;")
        #PASSWORD
        self.textboxlbl4 = QLabel("Password:", self)
        self.textboxlbl4.move(50, 190)
        self.textboxlbl4.setFont(QFont("Courier ", 10, QFont.Bold))
        self.textboxlbl4= QLineEdit(self)
        self.textboxlbl4.move(190, 180)
        self.textboxlbl4.resize(250, 30)
        self.textboxlbl4.setEchoMode(QLineEdit.Password)
        self.textboxlbl4.setStyleSheet("background-color: white;")
        # CONFIRM PASSWORD
        self.textboxlbl5 = QLabel(" Confirm Password:", self)
        self.textboxlbl5.move(40, 224)
        self.textboxlbl5.setFont(QFont("Courier ", 10, QFont.Bold))
        self.textboxlbl5 = QLineEdit(self)
        self.textboxlbl5.move(190, 215)
        self.textboxlbl5.resize(250, 30)
        self.textboxlbl5.setEchoMode(QLineEdit.Password)
        self.textboxlbl5.setStyleSheet("background-color: white;")
        #EMAIL ADDRESS
        self.textboxlbl6 = QLabel("Email Address:", self)
        self.textboxlbl6.move(50, 260)
        self.textboxlbl6.setFont(QFont("Courier ", 10, QFont.Bold))
        self.textboxlbl6 = QLineEdit(self)
        self.textboxlbl6.move(190, 250)
        self.textboxlbl6.resize(250, 30)
        self.textboxlbl6.setStyleSheet("background-color: white;")
        #CONTACT NUMBER
        self.textboxlbl7 = QLabel("Contact Number:", self)
        self.textboxlbl7.move(50, 295)
        self.textboxlbl7.setFont(QFont("Courier ", 10, QFont.Bold))
        self.textboxlbl7 = QLineEdit(self)
        self.textboxlbl7.move(190, 285)
        self.textboxlbl7.resize(250, 30)
        self.textboxlbl7.setStyleSheet("background-color: white;")
        #SUBMIT BUTTON
        self.button = QPushButton ('Submit', self)
        self.button.setToolTip("")
        self.button.move(200, 350)
        self.button.setStyleSheet("background-color: #837E93;")
        #CLEAR BUTTON
        self.button = QPushButton('Clear', self)
        self.button.setToolTip("")
        self.button.move(350, 350)
        self.button.clicked.connect(self.clear_fields)
        self.button.setStyleSheet("background-color: #837E93;")

    def clear_fields(self):
        for widget in self.findChildren(QLineEdit):
            widget.clear()

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegisterAccount()
    window.show()
    sys.exit(app.exec_())




