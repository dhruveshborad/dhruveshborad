# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(701, 467)
        self.logintitle = QtWidgets.QLabel(Form)
        self.logintitle.setGeometry(QtCore.QRect(300, 40, 121, 61))
        self.logintitle.setObjectName("logintitle")
        self.labeluser = QtWidgets.QLabel(Form)
        self.labeluser.setGeometry(QtCore.QRect(40, 130, 131, 41))
        self.labeluser.setObjectName("labeluser")
        self.labelpass = QtWidgets.QLabel(Form)
        self.labelpass.setGeometry(QtCore.QRect(40, 180, 121, 31))
        self.labelpass.setObjectName("labelpass")
        self.lineEditusername = QtWidgets.QLineEdit(Form)
        self.lineEditusername.setGeometry(QtCore.QRect(200, 140, 291, 24))
        self.lineEditusername.setObjectName("lineEditusername")
        self.labelforegatepass = QtWidgets.QLabel(Form)
        self.labelforegatepass.setGeometry(QtCore.QRect(10, 240, 211, 31))
        self.labelforegatepass.setObjectName("labelforegatepass")
        self.lineEditpassword = QtWidgets.QLineEdit(Form)
        self.lineEditpassword.setGeometry(QtCore.QRect(200, 190, 291, 24))
        self.lineEditpassword.setObjectName("lineEditpassword")
        self.pushButtonforegatepassword = QtWidgets.QPushButton(Form)
        self.pushButtonforegatepassword.setGeometry(QtCore.QRect(210, 240, 131, 31))
        self.pushButtonforegatepassword.setStyleSheet("")
        self.pushButtonforegatepassword.setObjectName("pushButtonforegatepassword")
        self.pushButtonsignup = QtWidgets.QPushButton(Form)
        self.pushButtonsignup.setGeometry(QtCore.QRect(140, 290, 101, 41))
        self.pushButtonsignup.setStyleSheet("background-color: rgb(148, 0, 74);\n"
"font: 9pt \"Segoe UI\";\n"
"font: italic 16pt \"Segoe UI\";\n"
"alternate-background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 255, 255, 255), stop:0.373979 rgba(255, 255, 255, 255), stop:0.373991 rgba(33, 30, 255, 255), stop:0.624018 rgba(33, 30, 255, 255), stop:0.624043 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));")
        self.pushButtonsignup.setObjectName("pushButtonsignup")
        self.pushButtonlogin = QtWidgets.QPushButton(Form)
        self.pushButtonlogin.setGeometry(QtCore.QRect(260, 290, 91, 41))
        self.pushButtonlogin.setStyleSheet("background-color: rgb(148, 0, 74);\n"
"font: italic 16pt \"Segoe UI\";\n"
"alternate-background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 255, 255, 255), stop:0.373979 rgba(255, 255, 255, 255), stop:0.373991 rgba(33, 30, 255, 255), stop:0.624018 rgba(33, 30, 255, 255), stop:0.624043 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));")
        self.pushButtonlogin.setObjectName("pushButtonlogin")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.logintitle.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700; color:#9d004f;\">Login</span></p></body></html>"))
        self.labeluser.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#9a004f;\">Username</span></p></body></html>"))
        self.labelpass.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#9a004f;\">Password</span></p></body></html>"))
        self.labelforegatepass.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; color:#006fa7;\">Foregatepassword?</span></p></body></html>"))
        self.pushButtonforegatepassword.setText(_translate("Form", "ForegatePassword"))
        self.pushButtonsignup.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700; font-style:normal; color:#ac2b5f;\">Signup</span></p></body></html>"))
        self.pushButtonsignup.setText(_translate("Form", "Signup"))
        self.pushButtonlogin.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700; color:#98004f;\">Login</span></p></body></html>"))
        self.pushButtonlogin.setText(_translate("Form", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())