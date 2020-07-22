# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 13:48:44 2020

@author: Erfan

"""
import numpy as np
def SORT(Array):
    for j in range (1,Array.size):
        A_sub = Array[0:j]
        key = Array[j]
        A_sub = np.append(A_sub, key)
        i = j-1
        while i>=0 and Array[i] > key:
            Array[i+1] = Array[i]
            i = i-1
        Array[i+1] = key
    return Array
    