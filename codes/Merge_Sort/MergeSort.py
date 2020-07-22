# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:11:59 2020

@author: Erfan
"""
import numpy as np
from Insertion import SORT

def MERGE_SORT(A, p, r):
    q = int((r+p)/2)
    MERGE(A, p, q, r)

def MERGE(Array, p, q, r):
    n1 = q-p
    n2 = r-q 
    L = np.zeros(n1+1)
    R = np.zeros(n2+1)
    L[:-1] = Array[p:q]
    SORT(L)
    R[:-1] = Array[q:r]
    SORT(R)
    L[-1] = 1e6
    R[-1] = 1e6
    i = 0
    j = 0
    for k in range(p, r):
        if L[i] <= R[j]:
            Array[k] = L[i]
            i = i+1
        else:
            Array[k] = R[j]
            j = j+1
    return Array
if __name__ == "__main__" :
    length = 20
    A = np.random.randint(1,length,length)
    p = 0
    r = A.size
    print(A)
    MERGE_SORT(A, p, r)
    print(A)