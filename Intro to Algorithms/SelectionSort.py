#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 10:36:28 2021

@author: cyrussafdar
"""
test1=[4,9,8,6,5,2,1,7,4,3]

def SelectSort(A):
    for i in range(len(A)-1):
        key=A[i]
        swap_ind=i
        for j in range(i,len(A)):
            if(A[j]<A[swap_ind]):
                swap_ind=j
        A[i]=A[swap_ind]
        A[swap_ind]=key
        
    return A