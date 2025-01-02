"""
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

 Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

 Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

nums = [4,5,6,7,0,1,2]
target = 0


def search(nums, target): #Is not the intended route to take for the problem, it's supposed to be a binary search problem. This works and passes time limit exceeded check by leetcode
    try:
        toreturn = nums.index(target)        
        return toreturn
    
    except ValueError:
        return -1
        
        
print(search(nums, target))



class Solution: #Actual intended solution by leetcode, can be used for 153
    def search(self, nums, target):
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l
        
        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        result = binary_search(0, pivot - 1)
        if result != -1:
            return result
        
        return binary_search(pivot, len(nums) - 1)