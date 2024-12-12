"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
"""

nums = [1,2,3,4] #Input
#Output: [24,12,8,6]

def productExceptSelf(nums): #Does passes the O(n) test on Leetcode but isn't strictly speaking O(n)
        n = len(nums)
        output_array = [1]*n
        
        #Calculate the left product
        left = 1 
        for i in range(n):
            output_array[i]=left
            
            left = left*nums[i]
             
            
        #Calculate the right product
        right = 1
        for i in range(n-1,-1,-1):
            output_array[i]*=right
            right*=nums[i]
        
        return output_array

print (productExceptSelf(nums))