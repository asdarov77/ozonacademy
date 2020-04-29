# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 18:35:28 2020

@author: Admin
"""

import random
amountOfbullets=input('А сколько зарядить >?  ')
aob= int (amountOfbullets)
baraban=[0, 0, 0, 0, 0, 0]
for i in range (aob):
    baraban[i]=1
print(baraban, 'выглядит сейчас вот так')    
howMuch=input('А сколько раз крутить?  ')
hm = int(howMuch)
for i in range (hm):
    random.shuffle(baraban)
    if baraban[0]==1:
        print('оглушительный выстрел \a')
    else:
        print('щелк')
#    print(baraban[0])
