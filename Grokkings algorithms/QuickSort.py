#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 00:44:51 2021

@author: cyrussafdar
"""
test=[9,8,7,6,5]
test2=[1,2,4,5,3,1,1]
test3=test+test2
test4= test*5+test2*2
def QuickSort(A):
    if len(A)<2:
        return A
    
    pivot=A[0]
    left=[i for i in A[1:] if i<pivot]
    right=[i for i in A[1:] if i>=pivot]
    return QuickSort(left)+[pivot]+QuickSort(right)