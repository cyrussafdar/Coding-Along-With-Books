#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 09:23:25 2021

@author: cyrussafdar
"""
A=[1,2,3,4,5,6,7]
B=[1,2,7,9,13,19]
def NonRecursiveBinarySearch(nums,target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low