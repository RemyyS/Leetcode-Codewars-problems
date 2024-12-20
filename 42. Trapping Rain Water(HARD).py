"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
(Visual help needed : https://leetcode.com/problems/trapping-rain-water/description/)

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output = 6



def trap(height): # My approach would be to use two pointers on each column and determine the amount of water that can be trapped 
                  # between two max height columns
    l = 0
    r = len(height) - 1
    leftmaxvalue = 0
    rightmaxvalue = 0
    result = 0

    while l < r:
        if leftmaxvalue < rightmaxvalue:
            l += 1