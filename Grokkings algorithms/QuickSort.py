#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 00:44:51 2021

@author: cyrussafdar
"""
import random
test=[9,8,7,6,5]
test2=[1,2,4,5,3,1,1]
test3=test+test2
test4= test*5+test2*2
def QuickSort(A):
    if len(A)<2:
        return A
    
    pivotIndex=random.randint(0,len(A)-1)
    pivot=A[pivotIndex]
    left=[i for i in A[0:pivotIndex]+A[pivotIndex+1:] if i<pivot]
    right=[i for i in A[0:pivotIndex]+A[pivotIndex+1:] if i>=pivot]
    #print("left ="+str(left))
    #print("right ="+str(right))
    return QuickSort(left)+[pivot]+QuickSort(right)

