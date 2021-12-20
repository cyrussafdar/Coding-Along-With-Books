#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 12:30:24 2021

@author: cyrussafdar
"""
test_1=[1,1,1,1]
test_2=[0,1,1,1]
test_3=[1,0,0,0]
test_4=[1,1,1,1,1]
def BinaryAdd(A,B):
    """Input: Arrays A and B of length n signifying a binary number
        Output: Array C of length n+1 signifying the binary sum of A and B"""
    carry=0
    C=[0]*(len(A)+1)
    for i in range(len(A)):
        print(i)
        SUM=A[i]+B[i]+carry
        C[i]=SUM%2
        carry=SUM>>1
    
    C[i+1]=carry
    return C
