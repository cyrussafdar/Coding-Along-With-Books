#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 09:35:45 2022

@author: cyrussafdar
"""
M={1:1,2:2}
def dfib(n):
    if n not in M.keys():
        M[n]=dfib(n-1)+dfib(n-2)
    return M[n]
    