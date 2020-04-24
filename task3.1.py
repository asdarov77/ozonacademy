# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 17:12:38 2020

@author: Admin
"""

for i in range(1, 10):
    for j in range(1, 10):
        print ('{} x {} = {}'.format(j, i, i*j).center(10), end='   ')
    print()