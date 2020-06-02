# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'regform.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RegForm(object):
    def setupUi(self, RegForm):
        
        RegForm.setObjectName("RegForm")
        RegForm.resize(308, 252)
        self.widget = QtWidgets.QWidget(RegForm)
        self.widget.setGeometry(QtCore.QRect(6, 40, 211, 79))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_login = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_login.setFont(font)
        self.label_login.setObjectName("label_login")
        self.gridLayout.addWidget(self.label_login, 0, 0, 1, 1)
        self.login_input = QtWidgets.QLineEdit(self.widget)
        self.login_input.setObjectName("login_input")
        self.gridLayout.addWidget(self.login_input, 0, 1, 1, 1)
        self.label_pass = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_pass.setFont(font)
        self.label_pass.setObjectName("label_pass")
        self.gridLayout.addWidget(self.label_pass, 1, 0, 1, 1)
        self.pass_input = QtWidgets.QLineEdit(self.widget)
        self.pass_input.setObjectName("pass_input")
        self.gridLayout.addWidget(self.pass_input, 1, 1, 1, 1)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.buttonBox)

        self.retranslateUi(RegForm)
 #       self.buttonBox.accepted.connect(self.MyFunction) # Нажатие на эту кнопку перенесено в класс формы регистрации
 ##       self.buttonBox.rejected.connect(self.MyFunction)
        QtCore.QMetaObject.connectSlotsByName(RegForm)

    def retranslateUi(self, RegForm):
        _translate = QtCore.QCoreApplication.translate
        RegForm.setWindowTitle(_translate("RegForm", "Dialog"))
        self.label_login.setText(_translate("RegForm", "Логин"))
        self.label_pass.setText(_translate("RegForm", "Пароль"))
#    def MyFunction(self):
#        self.pass_input.setText(' ')
#        self.login_input.setText(' ')
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegForm = QtWidgets.QDialog()
    ui = Ui_RegForm()
    ui.setupUi(RegForm)
    RegForm.show()
    sys.exit(app.exec_())

