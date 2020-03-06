# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 11:12:52 2017

@author: Jayson
"""

def drawParallelogram(numRows, numCols):
    for rows in range(numRows, 0, -1):
        print(' ' * (numRows - rows) + '*' * (numRows))
        
drawParallelogram(10, 8)            