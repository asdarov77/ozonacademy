# -*- coding: utf-8 -*-


from PyQt5 import QtWidgets
from helloform import Ui_HelloForm  # импорт приветственной формы
from regform import Ui_RegForm  # импорт формы регистрации
from PyQt5.QtWidgets import QWidget, QDialogButtonBox, QToolTip, QPushButton, QApplication, QMessageBox
import xos
import sys
import re
from random import randint
import json

class Hello(QtWidgets.QMainWindow):
    def __init__(self):
        super(Hello, self).__init__()
        self.ui = Ui_HelloForm()
        self.secondwin = Reg() # Создадим виджет и сохраним ссылку на него(secondwin)
        self.ui.setupUi(self)
        self.ui.buttonBox.rejected.connect(self.reg) # Вызов второй формы по нажатию на клавишу НЕТ
        self.ui.buttonBox.accepted.connect(self.nolik) # Запуск игры
    def reg(self):
        self.secondwin.show()
    def nolik(self):
        pass # Заглушка на кнопку Yes
 
class Reg(QtWidgets.QMainWindow):
    def __init__(self):
        super(Reg, self).__init__()
        self.ui = Ui_RegForm()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.add_user)
        self.ui.buttonBox.rejected.connect(self.close) # Закрываем форму 2 и возвращаемся на главную
    def add_user(self):
        login = self.ui.login_input.text() # lineEdit=QtGui.QLineEdit()
        password = self.ui.pass_input.text()
        print('Новый пользователь', login,password)
        self.val_user=Validate(login,password) # val_user-объект класса Validate
        if self.val_user.validate_login()==1 and self.val_user.validate_password()==1:
            if login not in user_mas:
                user_mas.append(login)
                self.new_user=Users(login,password) # new_user - объект класса Users
                self.ui.login_input.setText('') # Очищаем поля ввода
                self.ui.pass_input.setText('') # Очищаем поля ввода
            else:
                QMessageBox.information(self, "Error ", "This user already exists")
        else:
            QMessageBox.information(self, "Error ", "Try another login or password")
            self.ui.login_input.setText('')
            self.ui.pass_input.setText('')

class Users:
    """Базовый класс пользователя"""
    def __init__(self, login, password):
        """ инициализирует атрибуты логин и пароль пользователя"""
        self.login = login
        self.password = password
        self.uniq_id=self.generate_id()
        print ("новый пользователь " + self.login+" пароль "+ self.password + "  ID  " +str(self.uniq_id)+ "  создан  " )
        auth=(str(login)+' '+str(password)+' '+str(self.uniq_id)) # Строка для передачи записи в файл методу write()
        f = open('auth.txt', 'a')
        f.write(auth)
        f.write('\n')
        f.close()  
        to_json={'user': login, 'pass': password, 'id': self.uniq_id}
        file=open('auth.json', 'a')
        json.dump(to_json,file)
        file.write('\n')
        file.close()
    def generate_id(self):
        uniq_id=randint(1000,9999)
        return uniq_id
         
class Validate():
    """Класс для валидации пользователей"""
    def __init__(self, valid_login, valid_password):
         """ инициализирует атрибуты класса Users"""
         self.valid_login = valid_login
         self.valid_password = valid_password
    def validate_login(self):
        patLogin = re.compile(validLogin)
        matLogin = re.search(patLogin, self.valid_login)
        if matLogin:
            rez_login=1
            return rez_login
        else:
            return print('Попробуй другой логин')
    def validate_password(self):
        patPass = re.compile(validPass)
        matPass = re.search(patPass, self.valid_password)
        if matPass:
            rez_pass=1
            return rez_pass
        else:
            return print('Попробуй другой пароль')

user_mas=[] # Костыль для проверки существования такого пользователя (по логину)       
validLogin="^[A-Za-z]{2,16}$"
validPass="^[A-Za-z0-9.#@*_%+-]{2,16}$" 
    
app = QtWidgets.QApplication([])
application = Hello()
application.show()
sys.exit(app.exec())
