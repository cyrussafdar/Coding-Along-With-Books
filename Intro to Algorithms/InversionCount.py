#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 00:01:39 2021

@author: cyrussafdar
"""
A=[2,3,8,6,1]
def TestMerge(A,p,q,r):
    Inversions=0
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
                Inversions+=len(LeftArray)-i
                j+=1
    return Inversions
def Merge_Sort(A,p,r):
    if p<r:
        q=(int)((p+r)/2)
        R=Merge_Sort(A,p,q)
        L=Merge_Sort(A,q+1,r)
        Inv=TestMerge(A,p,q,r)+R+L
        return Inv
    return 0