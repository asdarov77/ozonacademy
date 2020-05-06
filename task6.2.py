# -*- coding: utf-8 -*-
"""
Created on Tue May  5 18:07:50 2020

@author: Admin
"""

i=0
birthday = input("Ведите дату рождения ddmmyy\n: ").strip()

filename = 'pi_million_digits.txt'
with open(filename) as file:   
    for line in file:
        line = line.strip()
        if birthday in line:
           print('счастливчик,в строке номер', i)
        else:
            i+=1
        



