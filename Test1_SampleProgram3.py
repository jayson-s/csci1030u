# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:53:26 2017

@author: Jayson

Example output for n = 4:
    >>>drawTriangle2(4)
    **** 
    ***  
    **   
    *
Notes:
    - There are n lines
    - The first line has n stars
"""

def drawTriangle2(n):
    #draw each line
    numSpaces = 0
    
    for i in range(n, 0, -1):   # [n, n-1, ..., ]
       
        #draw 'numSpaces' spaces 
       for space in range(numSpaces):
           print(' ', end='')
        
       #draw 'i' stars
       for star in range(i):
           print('*', end='')
           
       #go to the next line
       print('')
       
def drawTriangle2Alt(n):
    for numStars in range(n, 0, -1):
        print(' ' * (n-numStars) + '*' * )
       
       
       
       
drawTriangle2(4)       