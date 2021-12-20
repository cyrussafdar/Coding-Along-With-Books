#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 23:00:28 2021

@author: cyrussafdar
"""
SumTest=[1,2,3,4,5] #Sum=15
SumTest2=[10,20,50,90] #Sum=170
def recursiveSum(A,i):
    if(len (A)==0):
        return 0
    if(i==len(A)-1):
        return A[i]
    
        
    return A[i]+recursiveSum(A,i+1)

def recursiveSum2(A):
    if(len (A)==0):
        return 0
    return A[0]+recursiveSum2(A[1:])

def TheirSum(A):
    if A==[]:
        return 0
    return A[0]+TheirSum(A[1:])
