
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication


class Ui_HelloForm(object):
    def setupUi(self, HelloForm):
        
        HelloForm.setObjectName("HelloForm")
        HelloForm.resize(224, 185)
        self.buttonBox = QtWidgets.QDialogButtonBox(HelloForm)
        self.buttonBox.setGeometry(QtCore.QRect(30, 100, 161, 32))
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(HelloForm)
        self.label.setGeometry(QtCore.QRect(10, 10, 251, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(HelloForm)
        #self.buttonBox.accepted.connect(HelloForm.accept)
        ##self.buttonBox.accepted.connect(QCoreApplication.instance().quit)
        self.buttonBox.accepted.connect(self.MyFunction)

        #self.buttonBox.clicked.connect(self.reg)
        
        QtCore.QMetaObject.connectSlotsByName(HelloForm)
    
    def MyFunction(self):
        pass
    
#    def reg(self):
#        self.secondwin = Reg() ###Здесь класс формы 2      
#        self.secondwin.show()       
    def retranslateUi(self, HelloForm):
        _translate = QtCore.QCoreApplication.translate
        HelloForm.setWindowTitle(_translate("HelloForm", "Dialog"))
        self.label.setText(_translate("HelloForm", "Вы зарегистрированы ?"))

