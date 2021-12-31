#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 02:14:41 2021

@author: cyrussafdar
"""
import copy
emptyBoardDict={}
for i in range(8):
    emptyBoardDict[i]=[0]*8

partiallysolvedBoardDict=dict()
for i in range(8):
    partiallysolvedBoardDict[i]=[0]*8
partiallysolvedBoardDict[0][3]=1




solvedBoardDict=copy.deepcopy(partiallysolvedBoardDict)

solvedBoardDict[1][6]=1
solvedBoardDict[2][2]=1
solvedBoardDict[3][7]=1
solvedBoardDict[4][1]=1
solvedBoardDict[5][4]=1
solvedBoardDict[6][0]=1
solvedBoardDict[7][5]=1



#Board Class has a 8X8 array
class Board():
    def __init__(self,positionDict):
        self.position=positionDict
        
        self.update_positions()
    def update_positions(self):
        self.available=copy.deepcopy(emptyBoardDict)
        for i in range(8):
            for j in range(8):
                if(self.position[i][j]==1):
                    for k in range(8):
                        self.available[i][k]=1
                        self.available[k][j]=1
                        if(i+k<8):
                            if(j+k<8):
                                self.available[(i+k)][(j+k)]=1
                            if(0<=j-k):
                                self.available[(i+k)][(j-k)]=1
                        if(0<=i-k):
                            if(j+k<8):
                                self.available[(i-k)][(j+k)]=1
                            if(0<=j-k):
                                self.available[(i-k)][(j-k)]=1
        unattackedlist=list()
        for i in range(8):
            for j in range(8):
                if(self.available[i][j]==0):
                    unattackedlist.append([i,j])
        self.unattacked_positions=unattackedlist
                    
    def place_queen(self,coordinates):
        self.position[coordinates[0]][coordinates[1]]=1
        self.update_positions()
    def remove_queen(self,coordinates):
        self.position[coordinates[0]][coordinates[1]]=0
        self.update_positions()
        
        
    def has_8_queens(self):
        count=0
        for i in range(8):
            for j in range(8):
                if(self.position[i][j]==1):
                    count+=1
        return count==8
                        
def queens(board):
    if board.has_8_queens():
        print(board.position)
        return board
    #print(board.available)
    for position in board.unattacked_positions:
        #print(position)
        board.place_queen(position)
        #print(board.position)
        #print(board.available)
        #print()
        solution=queens(board)
        if solution:
            return solution
        board.remove_queen(position)
    return False
    
    #def Print(self):
    
#def Eight_queens(board):
    