# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 12:08:19 2017

@author: Jayson
"""

def isSublist(list1, list2):


  list3 = list(list1 + list2)

  resultList = []

  for i in range(len(list3)):

    for j in range(i+1, len(list3)):
      if list3[i] == list3[j]:
    
        return True
      
      else:
         
        return False
        
  return resultList



    