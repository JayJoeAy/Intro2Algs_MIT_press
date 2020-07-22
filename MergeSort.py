# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:11:59 2020

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

def dev(Array):
    L = Array[:int(len(Array)/2)]
    R = Array[int(len(Array)/2):]
    return L, R
    
def MERGE(Array):
    print(Array)
    L, R = dev(Array)
    if Array.size != 1:
        L, R = dev(Array)
        MERGE(L)
        MERGE(R)
        i = 0
        j = 0
        k = 0
        for k in range(Array.size-1):
            if L[i] <= R[j]:
                Array[k] = L[i]
                if i<(len(L)-1):
                    i = i+1
            else:
                Array[k] = R[j]
                Array[k+1] = L[i]
                if j<(len(R)-1):
                    j = j+1
        return Array

if __name__ == "__main__" :
    length = 4
    A = np.random.randint(1,length,length)
    print("this is ",A)
    p = 0
    r = A.size
    q = int((r+p)/2)
    MERGE(A)
    print (A)