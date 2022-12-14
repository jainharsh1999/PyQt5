import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("reg.ui",self)
        # self.textEdit. .connect(self.loginfunction)
        # self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        # self.createaccbutton.clicked.connect(self.gotocreate)

    def loginfunction(self):
        name=self.textEdit.text()
        # password=self.password.text()
        print("Successfully logged in with email: ", name, "and password:")
        

app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(680)
widget.setFixedHeight(620)
widget.show()
app.exec_()