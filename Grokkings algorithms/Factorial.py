#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 14:55:24 2021

@author: cyrussafdar
"""

def recursiveFact(N):
    if(N==1):
        return 1
   
    return recursiveFact(N-1)* N