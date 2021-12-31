#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 01:02:40 2021

@author: cyrussafdar
"""

def palindrome(word):
    if len(word)<=1:
        return True
    if(word[0]!=word[-1]):
        return False
    return palindrome(word[1:len(word)-1])