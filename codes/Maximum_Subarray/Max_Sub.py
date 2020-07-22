# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:06:33 2020

@author: Erfan
"""
import numpy as np
def FIND_MAX_CROSSING_SUBARRAY(A, low, mid, high):
    left_sum = -1e6
    s = 0
    for i in range(mid, low, -1):
        s = s + A[i]
        if s > left_sum:
            left_sum = s
            max_left = i
    right_sum = -1e6
    s = 0
    for j in range(mid+1, high):
        s = s + A[j]
        if s > right_sum:
            right_sum = s
            max_right =  j
    return (max_left, max_right, left_sum+right_sum)
if __name__ == '__main__':
    A = np.array([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7])
    low = 1
    mid = A.size//2
    high = A.size
    max_left, max_right, s = FIND_MAX_CROSSING_SUBARRAY(A, low, mid, high)