# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:42:37 2017

@author: Jayson
"""

def sublistInRange(list, min, max):
    inRange = []
    for element in list:
        if element >= min and element <= max:
            #this value is in the range
            #add it to our result list
            inRange.append(element)
    return inRange
    
sublist = sublistInRange([0,5,8,3,21,7,4,14,90], 4, 14)
print(sublist)    