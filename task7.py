# -*- coding: utf-8 -*-
"""
Created on Tue May 12 15:30:19 2020

@author: Admin
"""

def apply_discount(product, discount):
    """ принимаем на вход данные о товаре в виде словаряя и скидку"""
    price = int(product['цена'] * (1.0 - discount))
    try:
        assert 0 <= price <= product['цена']
    except AssertionError:
        print('протри глаза  ')
    else:
        return price, product['имя']

##kreslo = {'имя': 'кресло', 'цена': 12000}

#объявляем скидку в 25 процентов
##print(apply_discount(kreslo, 0.25))
# но положим кто-то из маркетологов уснул и случайно передал скидку не  0.25, а 2.5

##print(apply_discount(kreslo, 2.5))
#теперь у нас выполнение программы остановится
# потому что нельзя выполнять программу доплачивая покупателю за покупки

slovar={}
discount=[]
with open('discount.txt') as file:   
    for line in file:
        line=line.strip()    
        discount.append(line)
file.close()
i=0
with open('data.txt',encoding="utf-8") as file:   
    for line in file:
        line=line.strip()    
        slovar['имя']=line.split(',')[0]
        slovar['цена']=int(line.split(',')[1])
        print(apply_discount(slovar, float(discount[i])))
        i+=1
file.close()  
