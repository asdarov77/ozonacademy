# -*- coding: utf-8 -*-
"""
В данном примере будем под палиндромом понимать так называемый зеркальный вариант
# -*- coding: utf-8 -*-
"""



def is_palindrome(string):
    ln_string=len(string)
    middle=int(ln_string/2)
    a=string[0:middle]
    b=string[middle:ln_string]
    
    print(a)
    print(b)
    if a==b[::-1]:
        return True

string=input('Введи строку для провери:  ')
if len(string)%2!=0:
    print('Строка', string, 'не является полиндромом,введи четное количество символов')
elif is_palindrome(string)==True:
    print('Строка', string, ' полиндромом')
    
