# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:06:33 2020

@author: Erfan
"""
import numpy as np
def FIND_MAX_SUBARRAY(A,low, high):
    if high == low:
        return(low, high, A[low])
    else:
        mid = (low+high)//2
        left_low, left_high, left_sum = FIND_MAX_SUBARRAY(A, low, mid)
        right_low, right_high, right_sum = FIND_MAX_SUBARRAY(A, mid+1, high)
        cross_low, cross_high, cross_sum = FIND_MAX_CROSSING_SUBARRAY(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        if right_sum >= right_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else :
            return cross_low, cross_high, cross_sum
        
def FIND_MAX_CROSSING_SUBARRAY(A, low, mid, high):
    left_sum = -1e6
    s = 0
    for i in range(mid, low-1, -1):
        s = s + A[i]
        if s > left_sum:
            left_sum = s
            max_left = i
    right_sum = -1e6
    s = 0
    for j in range(mid+1, high+1):
        s = s + A[j]
        if s > right_sum:
            right_sum = s
            max_right =  j
    return (max_left, max_right, left_sum+right_sum)

if __name__ == '__main__':
    A = np.array([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7])
    low = 0
    mid = A.size//2
    high = A.size-1
    # max_left, max_right, s = FIND_MAX_CROSSING_SUBARRAY(A, low, mid, high)
    max_left, max_right, s = FIND_MAX_SUBARRAY(A, low, high)