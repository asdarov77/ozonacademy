# -*- coding: utf-8 -*-
"""
Created on Fri May 29 01:03:00 2020

@author: Admin
"""


class Calculator():
    """Базовый класс калькулятор,выполняющий действия сложения,вычитания,деления и умножения"""
    def __init__(self,x,y):
        """ инициализирует атрибуты x и y - вводимые числа"""
        self.x=x
        self.y=y
    def summation(self):
        return self.x+self.y
    def subtruction(self):
        return self.x-self.y  
    def multiplication(self):
        return self.x*self.y  
    def division(self):
        return self.x/self.y
    