#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 15:11:45 2021

@author: cyrussafdar
"""

def recursiveCountdown(N):
    print(N)
    if(N==0):
        return
    recursiveCountdown(N-1)

