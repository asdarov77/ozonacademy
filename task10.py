# -*- coding: utf-8 -*-
"""
Created on Mon May 18 20:09:39 2020

@author: Admin
"""
from simple_benchmark import benchmark
import matplotlib.pyplot as plt
 
def function_cycle(num):
    num=int(num)
    for i in range(2,6):
        chislo=num**i
        mas.append(chislo)
    return mas

count=2
def function_recurcive(num):
    global count
    if count==6:
        return mas_rec
    else:
        mas_rec.append(num**count)
        count+=1
        return function_recurcive(num)
#def function_recurcive(num,count):
#    if count==1:
#        return mas_rec[::-1]
#    else:
#        
#        mas_rec.append(num**count)
#        return function_recurcive(num,count-1)
       
mas_rec=[]
mas=[]        
  

num=int(input('Введи число\n'))
print(function_cycle(num))
print(function_recurcive(num))

funcs = [function_cycle, function_recurcive]
arguments = {}
for j in range(100):
    arguments['j'+str(j)]=j
    argument_name = 'Числа'
aliases = {function_cycle: 'цикл', function_recurcive: 'рекурсия'}
b = benchmark(funcs, arguments, argument_name, function_aliases=aliases)
b.plot()
plt.show(b)
plt.savefig('benchmark.png')