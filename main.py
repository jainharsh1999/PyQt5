import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.uic import loadUi
import mysql.connector as con

# class LoginApp(QDialog):
#     def __init__(self):
#         super(LoginApp,self). __init__()
#         loadUi("login-form.ui",self)
        
class RegApp(QDialog):
    def __init__(self):
        super(RegApp,self). __init__()
        loadUi("reg.ui",self)    
        self.pb2.clicked.connect(self.register)
        # self.pushButton2.clicked.connect(self.login)
    
    def register(self):
        name = self.tb1.text()   
        mobile_number = self.tb2.text()  
        # email_id = self.tb3.text()  
        # occuption  = self.tb4.text()  
        # address = self.tb5.text()  
        # city = self.tb6.text()  
        # state = self.tb7.text()  
        # country = self.tb8.text()  
        db = con.connect(host="localhost", user="root",password="",db="sample")
        cursor = db.cursor()
        cursor.execute("select * from userlist where username' "+ name +"' and name'" + mobile_number +"' and mobile'")
        result = cursor.fetchone()
        if result:
            QMessageBox.information(self, "Registered" , "congrats!! You register successfully!!")
        else:
            QMessageBox.information(self, "Registered" , "Invalid user..!! register for new user!!")


    def show_reg(self):
        widget.setCurrentIndex(1)              

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
# loginform = LoginApp()
registerform = RegApp()
# widget.addWidget(loginform)
widget.addWidget(registerform)
widget.setFixedWidth(680)
widget.setFixedHeight(620)
widget.setCurrentIndex(0)
widget.show()

app.exec_()      
        