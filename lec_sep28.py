# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 11:15:54 2017

@author: Jayson
"""

for x in [1,2,3,4,5]:
    print(x)
    
grades = [41.0, 55.5, 100.0, 71.0, 65.5, 99.0]

if 100.0 in grades:
    print('Yes!')
    print('The 100.0 is at index', grades.index(100.0))

names1 = ['Sally', 'Bob', 'Chris', 'Jack']
names2 = ['Tom', 'Jayson', 'George']
name = names1 + names2
print(name)

