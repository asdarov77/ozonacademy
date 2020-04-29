# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:09:46 2020

@author: Admin
"""
import random

print(" Cейчас вам будет предоставлена возможность введения слов")
print(" Когда заходите остановиться, просто введите q")

slovar = {'table':'стол','man':'мужчина','apple':'яблоко'}

file = open('enrus.txt')
onstring = file.read().split("\n")[:-1]
for line in onstring:
    key = line.split()[0]
    slovar[key] = line.split()[1]
file.close()  


while True:
    key = input("Ведите слово на английском\n: ").strip().lower()
    if key == 'q':
        break
    value = input("Ведите слово на русском\n: ").strip().lower()
    slovar[key] = value
print(slovar)
print("Сейчас у нас будет проверка, больше 3 ошибок нельзя")

errors = 3
bonus = 0

while  errors >0:
    key=random.choice(list(slovar.keys()))
    print("Ввeдите перевод слова", key, ": ")
    answer = input(": ").strip().lower()
    if slovar[key] == answer:
        bonus += 1
        print("Ваш счет составляет", bonus)
    else:
        errors -=1
        print(slovar[key], "- правильный ответ")
        print("У Вас осталось", errors, "ошибки")
print('game over')
print('Ваш бонусный счет составил',bonus)
        

