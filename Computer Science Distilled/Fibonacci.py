#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 00:58:00 2021

@author: cyrussafdar
"""

def Fib(n):
    if n<=2:
        return 1
    return Fib(n-1)+Fib(n-2)