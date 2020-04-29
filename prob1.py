# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 19:28:05 2020

@author: Admin
"""

unconfirmed_users = ['pavel', 'petr', 'semen']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()   # метод pop мы свами уже должны были разбирать

    print(f"Verifying user: {current_user.title()}")    
    confirmed_users.append(current_user) # Показывваем всех подтвердивших пользователей


print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:    
    print(confirmed_user.title())

    
    
spisok = ['skovorodka', 'stolick', 'istoria', 'skovorodka', 'stena', 'kartina']
while 'skovorodka' in spisok:
    spisok.remove('skovorodka')
    print(spisok)