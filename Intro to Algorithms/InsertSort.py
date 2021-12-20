#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 14:28:00 2021

@author: cyrussafdar
"""
A1=[4,9,8,6,5,2,1,7,4,3]*5
def InsertionSort(A):
    print(A)
    for j in range(1,len(A)):
        #number being considered
        key=A[j]
        #intialised as the nunmber before j i.e. a pointer to the number before
        # key
        i=j-1
        #while i is greater than = 0 and the number is greater than key
        while(i>=0 and A[i]<key):
            #while A[i] is greater than key make the sorted list longer and go
            #down one more
            A[i+1]=A[i]
            i=i-1
        #when the loop is exit the A[i] is less than equal to key or no 
        #smaller number was found hence set A[i+1] to key
        A[i+1]=key
    print(A)