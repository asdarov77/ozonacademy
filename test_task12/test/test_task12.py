# -*- coding: utf-8 -*-
"""
Created on Wed May 27 18:12:47 2020

@author: Admin
"""

import unittest
#import task12
from calc import Calculator


class TestCalc(unittest.TestCase):
    '''Тесты для функции суммирования '''
    
    def test_summation_number(self):
        '''Правда ли при вводе цифры функция просуммирует как положено  '''
        test2=Calculator(10,20)
        summation_number = test2.summation()
        self.assertEqual(summation_number,30)
    def test_subtruction(self):
        '''Правда ли что 30 минус 5 равно 25   '''
        test2=Calculator(30,5)
        subtruction_number = test2.subtruction()
        self.assertEqual(subtruction_number,25)
    def test_multiplication_number(self):
        '''Правда ли при 5 усножить на 4 равно 20  '''
        test2=Calculator(5,4)
        multiplication_number = test2.multiplication()
        self.assertEqual(multiplication_number,20)
    def test_division_number(self):
        '''Правда ли 30 разделить на 10 равно 3  '''
        test2=Calculator(30,10)
        division_number = test2.division()
        self.assertEqual(division_number,3)
    def test_summation_letter(self):
        '''Правда ли при вводе букв функция просуммирует   '''
        test2=Calculator('a','3')
        summation_letter = test2.summation()
        self.assertEqual(summation_letter,'a3')
    def test_summation_null_letter(self):
        '''сложение строк корректно ли   '''
        test2=Calculator(' ','3')
        summation_letter = test2.summation()
        self.assertEqual(summation_letter,' 3')
    
unittest.main()

