#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 14:25:22 2021

@author: cyrussafdar
"""
from collections import deque
graph = {}
graph['you'] = ['alice', 'bob', 'claire'] 
graph['bob'] = ['anuj', 'peggy'] 
graph['alice'] = ['peggy'] 
graph['claire'] = ['thom', 'jonny'] 
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

def person_is_seller(name):
    return name[-1]=='y'

#general BFS
def BFS(graph,checking_function):
    search_queue=deque()
    print(graph)
    
    for key in graph.keys():
        search_queue+=graph[key]
    searched={}
    while search_queue:
        item=search_queue.popleft()
        if item not in searched:
            if person_is_seller(item):
                print(str(item)+" meets the condition")
                return True
            else:
                search_queue+=graph[item]
                searched[item]=True
    return False