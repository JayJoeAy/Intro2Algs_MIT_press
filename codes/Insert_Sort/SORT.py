# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 13:48:44 2020

@author: Erfan

"""
import numpy as np
def SORT(A) :
for j in range (1,A.size):
    A_sub = A[0:j]
    key = A[j]
    A_sub = np.append(A_sub, key)
    i = j-1
    while i>=0 and A[i] < key:
        A[i+1] = A[i]
        i = i-1
    A[i+1] = key
    return A
# if __name__ == "__main__" :
#     SORT(A)
    