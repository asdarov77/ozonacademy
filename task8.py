# -*- coding: utf-8 -*-
"""
Created on Mon May 11 13:04:57 2020

@author: Admin
"""

import re

validLogin="^[A-Za-z0-9._%+-]{2,15}$"
validMail="^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$"
print('Для выхода введите q')

while True:
    login=input('Введи свой login:\n ')
    if login =='q':
        break
    mail=input('Введи свой mail:\n ')
    if mail =='q':
        break
    patLogin = re.compile(validLogin)
    patmail = re.compile(validMail)
    matLogin = re.search(patLogin, login)
    matMail = re.search(patmail, mail)
    
    if matLogin and matMail:
        string=login+' '+mail+'\n'
        with open('report.txt','a') as file:
            file.write(string)
    elif matLogin!=1:
        print('Недопустимый символ в имени пользователя') 
    elif matMail!=1:
        print('Недопустимое имя почты')     
print('Вы вышли из программы,результаты в файле')
    

        