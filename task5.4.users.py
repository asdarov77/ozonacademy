# -*- coding: utf-8 -*-
"""
Created on Fri May  1 01:03:12 2020

@author: Admin
"""
import random

def describe(name):
    for key in users.keys():
        if name==key:

            return users[key]
        

users={'quality':{'надежный','богатый','теряется','здоровый','удобный','мягкий','русский'},'Ivan':'Abramov', 'Руслан':'Белый','Тихон':'Зеленый','Гадя':'Хренова','Иван':'Охлобыстин','Слава':'Комиссаренко','Виктория':'Сорокина'}

name=input('\nВведи имя человека:  ') 
human_quality=random.choice(list(users['quality']))
if describe(name):
    print(name,' ',describe(name),' ',human_quality)
else:
    print('не найден')


