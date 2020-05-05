# -*- coding: utf-8 -*-
"""
Created on Tue May  5 18:07:50 2020

@author: Admin
"""
mas=[]
sum=0
filename = 'numbers.txt'
with open(filename) as file:   
    for line in file:
        line= line.strip()    
        mas.append(line)

print(mas)
print('максимальное значение:', max(mas))
print('минимальное значение:', min(mas))
for num in mas:
    sum+=int(num)

print('сумма элементов:', sum)
print('среднее значение:', sum/len(mas))
slovar={'максимальное значение:':max(mas),'минимальное значение:': min(mas),'среднее значение:':sum/len(mas),'сумма элементов:': sum}
with open('report.txt','w') as file:
    for item in slovar.items():
#        print(str(item).replace('(','').replace(')',''))
        file.write(str(item).replace('(','').replace(')','')+'\n')

