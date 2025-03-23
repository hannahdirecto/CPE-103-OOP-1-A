from registration import  RegisterAccount
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegisterAccount()
    window.show()
    sys.exit(app.exec_())