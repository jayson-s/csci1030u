# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:29:31 2017

@author: Jayson
"""

def jumpMaximum(list):
    
    #find the index of the maximum value in list
    maximumIndex = 0
    for index in range(1, len(list)):
        if list[index] > list[maximumIndex]:
            maximumIndex = index
    
    #swap the first and the maximum
    first = list[0]
    list[0] = list[maximumIndex]
    list[maximumIndex] = first
    
    #return the updated list
    return list

newList = jumpMaximum([5,8,3,21,7,4,14,99])
print(newList)