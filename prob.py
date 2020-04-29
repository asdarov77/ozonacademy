# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 18:20:12 2020

@author: Admin
"""

#amount_key_of_words=input("сколько слов в словаре")
#aow=int()
#slovar={'book':'книга','bear':'медведь'}
#slovar['floor']='пол'
#print(slovar)
#slovar={}
#for i in range(aow):
#    key=input('введи слово на англ языке: ')
#    value=input('введи перевод: ')
#    slovar[key]=value
    
#for key in slovar.keys():
#    print('введите перевод слова', key, ':')
#    answer = input(' : ')
    
#if slovar[key] == answer:
#    print('нет')
#else:
#    print('правильно ')    

#user= {
#'id' : 104,
#'name' : 'Petr',
#'surname' : 'Ivanov'      
#       }


print('будем тренироваться')
print('стоп слово stop')
slovar={}
while True:
    key=input('введи слово на англ языке: ')
    if key=='stop':
        break
    value=input('введи перевод: ')
    slovar[key]=value
print(slovar)

errors=0
bonus=0
        
for key in slovar.keys():
    print('введите перевод слова', key, ':')
    answer = input(' : ')
    if slovar[key] == answer:
        print('нет')
    else:
        
        print('правильно ')   
    