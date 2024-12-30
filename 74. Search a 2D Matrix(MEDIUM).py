"""
You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

def searchMatrix(matrix, target):
    for row in matrix: #I've thought about zipping lists together but I think it's worse in terms of time complexity
        if row[-1] >= target: #Because lists are sorted, checks only if the last input in each list is superior to target, if it is, then the target is in the row, or else it would have triggered in the row before
            return target in row #This allows to check against edge cases and to find the target inside the row
        
    return False #Putting return False here instead of after a "else" statement allows us to not get tricked by several edge cases where very few numbers are given in the matrix
        
print(searchMatrix(matrix, target))