#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 00:27:26 2021

@author: cyrussafdar
"""
testA=[1,2,3,3,3,4,4,5,2,4,5,7,1,2,3,6]
testB=[3,2,1,5,4,6,8,7,9,10]*40
testC=[1, 2, 3, 3, 3, 4, 4, 5, 1, 2, 2, 3, 4, 5, 6, 6]
def Merge(A,p,q,r):
    n_1=q-p+1
    n_2=r-q
    LeftArray=[0]*(n_1+1)
    RightArray=[0]*(n_2+1)
    for i in range(n_1):
        LeftArray[i]=A[p+i]
    for j in range(n_2):
        RightArray[j]=A[q+j+1]
    #high numbers I am using as the sentinel value
    LeftArray[i+1]=999999999999999
    RightArray[j+1]=999999999999999
    i=0
    j=0
    for k in range(p,r+1):
        if(LeftArray[i]<=RightArray[j]):
            A[k]=(LeftArray[i])
            i+=1
        else:
            A[k]=(RightArray[j])
            j+=1
def TestMerge(A,p,q,r):
    n_1=q-p+1
    n_2=r-q
    LeftArray=[0]*(n_1)
    RightArray=[0]*(n_2)
    for i in range(n_1):
        LeftArray[i]=A[p+i]
    for j in range(n_2):
        RightArray[j]=A[q+j+1]
    i=0
    j=0
    for k in range(p,r+1):
        if(j==n_2):
            A[k]=(LeftArray[i])
            i+=1
        elif(i==n_1):
            A[k]=(RightArray[j])
            j+=1
        else:
            if(LeftArray[i]<=RightArray[j]):
                A[k]=(LeftArray[i])
                i+=1
            else:
                A[k]=(RightArray[j])
                j+=1
def Merge_Sort(A,p,r):
    if p<r:
        q=(int)((p+r)/2)
        Merge_Sort(A,p,q)
        Merge_Sort(A,q+1,r)
        TestMerge(A,p,q,r)
    return A
