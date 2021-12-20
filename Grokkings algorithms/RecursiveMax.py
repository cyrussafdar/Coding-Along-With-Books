#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 00:08:41 2021

@author: cyrussafdar
"""
Test=[1,2,3,4,5] #Max=5
Test2=[10,20,50,90] #Sum=90
Test3=[90,10,20,50]

def RecursiveMax(A):
    if(len(A)==0):
        return 0
    MAX=RecursiveMax(A[1:])
    if(A[0]>MAX):
        return A[0]
    else:
        return MAX
    
    
    