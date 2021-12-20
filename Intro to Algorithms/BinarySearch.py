#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 14:22:05 2021

@author: cyrussafdar
"""
B=[1,2,3,4,5,6,7]
C=[3,4,5,6,11,23,12]


#def binary_search(A,v):
#    """Input: A:Array to be searched, v: value to look for"""
#    mid=(int)(len(A)/2)
#    print(A)
#    if v == A[mid]:
#        #print(mid)
#        return mid
#    elif len(A)==1:
#        print("get's here")
#        return None
#    elif v<A[mid]:
#        binary_search(A[0:mid],v)
#    else:
#        binary_search(A[mid::],v)

def binary_search(A,start,end,v):
    """Input: A:Array to be searched, v: value to look for
    Output: Index of the array at which the value was found"""
    mid=(int)((start+end)/2)
    #print(mid)
    if v == A[mid]:
        return mid
    elif end-start==1:
        return None
    if v<A[mid]:
        return binary_search(A,start,mid,v)
    else:
        return binary_search(A,mid,end,v)
    

    