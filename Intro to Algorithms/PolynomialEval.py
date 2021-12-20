#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 22:14:18 2021

@author: cyrussafdar
"""
a=[1,3,3,1]
b=[1,1,1,1,1]

def poly_evaluate(A,x):
    """Input: A: Array of polynomials,x= value of x
    Output: y"""
    y=0
    for i in range(len(A)):
        current_sum=A[i]
        for j in range(i):
            current_sum*=x
        y+=current_sum
    return y   

def Horner_poly_evaluate(A,x):
    """Input: A: Array of polynomials,x= value of x
    Output: y"""
    y=0
    for i in range(len(A)-1,-1,-1):
        y=A[i]+x*y
    return y                     