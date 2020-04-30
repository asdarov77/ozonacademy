# -*- coding: utf-8 -*-
"""
В данном примере будем под палиндромом понимать так называемый зеркальный вариант
# -*- coding: utf-8 -*-
"""



def is_palindrome(string):
    if string == string[::-1]:
        return True

string=input('Введи строку для провери:  ')
if is_palindrome(string)==True:
    print('Строка', string, ' полиндромом')
else:
    print('Увы')
    
