# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as log
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLineEdit,QPushButton

class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('second window')
        self.setFixedWidth(500)
        
        mainLayout = QVBoxLayout()

        self.admin1 = QLineEdit()
        self.admin2 = QLineEdit()
        mainLayout.addWidget(self.admin1)
        mainLayout.addWidget(self.admin2)

        self.updateButton = QPushButton('update')
        self.deleteButton = QPushButton('delete')
        self.closeButton = QPushButton('Close')
        self.updateButton.clicked.connect(self.update)
        self.deleteButton.clicked.connect(self.delete)
        self.closeButton.clicked.connect(self.close)
        mainLayout.addWidget(self.updateButton)
        mainLayout.addWidget(self.deleteButton)
        mainLayout.addWidget(self.closeButton)
        

        self.setLayout(mainLayout)
    
    def update(self):
            
          
                db=log.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="register"  
                )
                
                mycursor=db.cursor()
                name=self.admin1.text()
                email=self.admin2.text()
                updateq="UPDATE admin SET email=%s WHERE Password=%s"
                value=(name,email)
                 
                try:
                    mycursor.execute(updateq, value)
                    db.commit()
                    print("success")
                except:
                    print("failed")
                    
    def delete(self):
        
        
                db=log.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="register"  
                )
                
                mycursor=db.cursor()
                email=self.admin1.text()

                deletea="DELETE FROM admin WHERE email=%s"
                value=(email,)
                    
                try:
                    mycursor.execute(deletea, value)
                    db.commit()
                    print("success")
                except:
                    print("failed")   
    
    def displayInfo(self):
        self.show()

class Ui_Form1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(709, 464)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei Light")
        font.setPointSize(10)
        Form.setFont(font)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(330, 110, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tb3 = QtWidgets.QLineEdit(Form)
        self.tb3.setGeometry(QtCore.QRect(220, 190, 351, 21))
        self.tb3.setObjectName("tb3")
        self.lb3 = QtWidgets.QLabel(Form)
        self.lb3.setGeometry(QtCore.QRect(120, 190, 81, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb3.setFont(font)
        self.lb3.setObjectName("lb3")
        self.pb2 = QtWidgets.QPushButton(Form)
        self.pb2.setGeometry(QtCore.QRect(310, 320, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pb2.setFont(font)
        self.pb2.setStyleSheet("color: green;")
        self.pb2.setObjectName("pb2")
        self.tb4 = QtWidgets.QLineEdit(Form)
        self.tb4.setGeometry(QtCore.QRect(220, 230, 351, 21))
        self.tb4.setObjectName("tb4")
        self.lb4 = QtWidgets.QLabel(Form)
        self.lb4.setGeometry(QtCore.QRect(120, 230, 81, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb4.setFont(font)
        self.lb4.setObjectName("lb4")
        self.pb3 = QtWidgets.QPushButton(Form)
        self.pb3.setGeometry(QtCore.QRect(480, 270, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pb3.setFont(font)
        self.pb3.setStyleSheet("color: green;")
        self.pb3.setObjectName("pb3")
        self.lb4_2 = QtWidgets.QLabel(Form)
        self.lb4_2.setGeometry(QtCore.QRect(350, 280, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lb4_2.setFont(font)
        self.lb4_2.setObjectName("lb4_2")
        self.secondWindow = SecondWindow()
        self.pb2.clicked.connect(self.value1)
        # self.pb2.clicked.connect(self.user)
        self.pb2.clicked.connect(self.passingInformation)
        # self.pb2.clicked.connect(self.user)
        # self.pb3.clicked.connect(self.gotocreate)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    # def user(self):
    #     self.details=QtWidgets.QMainWindow()
    #     self.ui=Ui_Form1()
    #     self.ui.setupUi(self.details)
    #     self.details.show()

    def value1(self):

            db=log.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="register"    
            )
            mycursor=db.cursor()   
            email=self.tb3.text()
            Password=self.tb4.text()

            query="SELECT * FROM admin WHERE email=%s AND Password=%s"
            value=(email,Password)
            mycursor.execute(query,value)
            harsh= mycursor.fetchall()
        
            if (len(harsh))>0:
                    print("user found")
                    
            else:            
                    print("user not found")
    
                
    def passingInformation(self):
        self.secondWindow.admin1.setText(self.tb3.text())
        self.secondWindow.admin2.setText(self.tb4.text())
        self.secondWindow.displayInfo()

    # def gotocreate(self):
    #     pb3=Ui_Form1()
    #     widget.addWidget(pb3)
    #     QtWidgets.setCurrentIndex(QtWidgets.currentIndex()+1)
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Log In "))
        self.lb3.setText(_translate("Form", "Email Id"))
        self.pb2.setText(_translate("Form", "Login"))
        self.lb4.setText(_translate("Form", "Password"))
        self.pb3.setText(_translate("Form", "Sign up"))
        self.lb4_2.setText(_translate("Form", "Don\'t have account ?"))

if __name__ == "__main__":
        import sys
        app=QtWidgets.QApplication(sys.argv)
        Form=QtWidgets.QWidget()
        ui = Ui_Form1()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())
        