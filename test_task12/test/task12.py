# -*- coding: utf-8 -*-
"""
Created on Wed May 27 15:02:40 2020

@author: Admin
"""

class Calculator:
    """Базовый класс калькулятор,выполняющий действия сложения,вычитания,деления и умножения"""
    def __init__(self, x, y):
        """ инициализирует атрибуты x и y - вводимые числа"""
        self.x = x
        self.y = y
    def summation(self):
        return x+y
    def subtruction(self):
        return x-y  
    def multiplication(self):
        return x*y  
    def division(self):
        return x/y      
    
x = int(input('Введи первое число\n'))
y = int(input('Введи второе число\n'))
operate = Calculator(x,y)
choice=1
while choice!=0:
    print('0. Выход')
    print('1. Сложить')
    print('2. Вычесть')
    print('3. Умножить')
    print('4. Разделить')
    choice=int(input('Введи номер операции\n'))
    if choice==0:
        print('Выход ')
    elif choice==1:
        print('результат операции сложения ', operate.summation())
    elif choice==2:
        print('результат операции вычитания  ', operate.subtruction())
    elif choice==3:
        print('результат операции умножения  ', operate.multiplication())
    elif choice==4:
        print('результат операции деления ', operate.division())
    else:
        print('Ввод строго число от 0 до 4\n')
print('Работа калькулятора завершена\n')
