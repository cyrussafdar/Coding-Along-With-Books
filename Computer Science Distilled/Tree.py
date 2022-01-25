#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 17:53:32 2022

@author: cyrussafdar
"""
import random
class Tree(object):
    def __init__(self, value):
        self.value=value
        self.right=None
        self.left=None
    def insert(self,new_node):
        node=self
        while (node!= None):
            last_node=node
            if(new_node.value>node.value):
                node=node.right
            else:
                node=node.left
        if(new_node.value>last_node.value):
            last_node.right=new_node
        else:
            last_node.left=new_node
    @property
    def Treetolist(self):
        #Node to self hehehe
        Node=self
        result=list()
        #if(Node==None):
        #    #return 
        #using a quick sort like implementation
        if(Node.left!=None):
            left=Node.left.Treetolist
            for i in left:
                result.append(i)
        result.append(Node.value)
        if(Node.right!=None):
            right=Node.right.Treetolist
            for i in right:
                result.append(i)
                
        return result
    
    def Balance(self):
        nodes=self.Treetolist
        BalancedTree=BalanceTree(nodes)
        self.value=BalancedTree.value
        self.right=BalancedTree.right
        self.left=BalancedTree.left
        
def Find_Node(binary_tree,value):
    node=binary_tree
    while(node != None):
        if node.value==value:
            return node
        if value> node.value:
            node=node.right
        else:
            node=node.left
    return "Not Found"
        
       
def BalanceTree(nodes):
        if(len(nodes)==0 or nodes==None):
            return None
        middle=int(len(nodes)/2)
        left=nodes[0:middle]
        right=nodes[middle+1:]
        balanced=Tree(nodes[middle])
        balanced.left=BalanceTree(left)
        balanced.right=BalanceTree(right)      
        return balanced
#implementing the Tree 
#         10
#      /      \
#     6      18
#    / \    /  \
#   4  8   15  21
def TreeImplementation():
    RootNode=Tree(10)
    RootNode.left=Tree(6)
    RootNode.right=Tree(18)
    RootNode.left.left=Tree(4)
    RootNode.left.right=Tree(8)
    RootNode.right.right=Tree(21)
    RootNode.right.left=Tree(15)
    return RootNode

def RandomTree():
    treesize=random.randint(1,25)
    RootNode=Tree(random.randint(1,100))
    for i in (range(treesize)):
        RootNode.insert(Tree(random.randint(1,100)))
    return RootNode

def UnbalancedTree():
    RootNode=Tree(11)
    for i in range(10,0,-1):
        RootNode.insert(Tree(i))
    return RootNode
        
def TreeImplementationM():
    RootNode=Tree(10)
    RootNode.insert(Tree(6))
    RootNode.insert(Tree(18))
    RootNode.insert(Tree(4))
    RootNode.insert(Tree(8))
    RootNode.insert(Tree(21))
    RootNode.insert(Tree(15))
    return RootNode

