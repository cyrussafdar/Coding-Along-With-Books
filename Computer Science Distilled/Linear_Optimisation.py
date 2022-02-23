#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 12:05:31 2022

@author: cyrussafdar
"""

#SMART FURNISHING Your office needs filing cabinets. 
#Cabinet X costs $10, occupies 6 square feet and holds 8 cu- bic feet of files. 
#Cabinet Y costs $20, occupies 8 square feet and holds 12 cubic feet of files. 
#You have $140, and you can use up to 72 square feet in the office for the cabinets. 
#What should you buy to maximize storage capacity?
class Cabinet:
    def __init__(self,price,space,capacity):
        self.price=price
        self.space=space
        self.capacity=capacity
def lin_optimization(Budget,Office_space):
    #To add more cabinet types add here and add more nested loops
    x=Cabinet(10,6,8)
    y=Cabinet(20,8,12)
    z=Cabinet(30,12,14)
    cab_types=[x,y,z]
    MaxCabs=dict()
    solution=[0]*4
    #intialising the dictionary
    for i in cab_types:
        MaxCabs[i]=min(Budget//i.price,Office_space//i.space)
        
    Total_cost=0
    Total_space=0
    Total_cap=0
    #X max value
    for i in range(MaxCabs[cab_types[0]]+1):
        #Y max value
        for j in range(MaxCabs[cab_types[1]]+1):
           
            for k in range(MaxCabs[cab_types[2]]+1):
                current_cost=0
                current_space=0
                current_cap=0
                candidate_sol=[i,j,k]
                for l in range(len(cab_types)):
                    current_cost+=candidate_sol[l]*cab_types[l].price
                    current_space+=candidate_sol[l]*cab_types[l].space
                    current_cap+=candidate_sol[l]*cab_types[l].capacity
                #print(candidate_sol)
                if(Total_cap<current_cap and Budget>=current_cost and Office_space>=current_space):
                    
                    solution=candidate_sol
                    Total_cost=current_cost
                    Total_space=current_space
                    Total_cap=current_cap
    
    print(f"For a budget of {Budget} and office space of {Office_space} ")
    print(cab_types)
    for i in range(len(cab_types)):
        print(f"Buy {solution[i]} of Cabinet costing ${cab_types[i].price} taking up {cab_types[i].space} cubic feet and holding {cab_types[i].capacity} cubic feet each")
    
    
    print(f"Total cost of ${Total_cost} ")
    print(f"Total space of {Total_space} cubic feet")
    print(f"Total capacity of {Total_cap} cubic feet")
        