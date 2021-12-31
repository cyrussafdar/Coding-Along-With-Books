#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 01:21:16 2021

@author: cyrussafdar
"""

flowerlist=['white','orange','pink','sunflower']
flowerSet=set(flowerlist)
#don't work
def PowerSet(set_of_items):
    powerset=set()
    #emptyset=set()
    #powerset.add(emptyset)
    for item in set_of_items:
        new_set=powerset
        for elem in new_set:
            powerset.add(item)
        powerset.union(new_set)
    return powerset
def recursivePS(items):
        ps=items
        for item in items:
            ps.remove(item)
            ps.append(recursivePS(ps))
            ps.append(item)
        return ps
    
#works
def powerset(s):
    x = len(s)
    Main_list=list()
    for i in range(1 << x):
        temp_list=list()
        for j in range(x):
            if (i & (1 << j)):
                 temp_list.append(s[j])
        Main_list.append(temp_list)
    return Main_list


