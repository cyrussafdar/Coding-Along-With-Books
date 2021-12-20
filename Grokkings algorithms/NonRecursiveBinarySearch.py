#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 09:23:25 2021

@author: cyrussafdar
"""
A=[1,2,3,4,5,6,7]
B=[1,2,7,9,13,19]
def NonRecursiveBinarySearch(List,value):
    low=0
    high=len(List)
    while(low<=high):
        mid=(high+low)//2
        guess=List[mid]
        if(guess==value):
            return mid
        if(guess>value):
            high=mid-1
        else: #guess>value
            low=mid+1
    #when nothing is found
    return None
            