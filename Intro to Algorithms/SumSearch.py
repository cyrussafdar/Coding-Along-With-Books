#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 16:20:08 2021

@author: cyrussafdar
"""
B=[1,2,3,4,5,5]
C=[2,3,4,4,2,1,9]
def TestMerge(A,p,q,r):
    n_1=q-p+1
    n_2=r-q
    LeftArray=[0]*(n_1+1)
    RightArray=[0]*(n_2+1)
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
def SumSearch(S,X):
#    """Input: S: a set of numbers, X: Target sum
#        Output: Boolean indicating if S contains any elements such that
#        s1+s2=X"""
    S=Merge_Sort(S,0,len(S)-1)
    r=0
    l=len(S)-1
    while (r<l):
        Sum=S[r]+S[l]
        if(Sum==X):
            return True
        elif(Sum>X):
            l=l-1
        else:
            r=r+1
                
    return False
