#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 23:37:49 2021

@author: cyrussafdar
"""

def recursiveCount(A):
    if(len (A)==0):
        return 0
    return 1+recursiveCount(A[1:])


