"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

 Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
"""

nums = [-1,0,3,5,9,12]
target = 9

def search(nums, target):
    def binary_search(low, high): #Exercice of remembering the binary search algorithm by heart
            if low > high: #Checks base case
                return -1
            
            mid = (low + high) // 2 #Setting Mid pointer
            
            if nums[mid] == target: #If mid is exactly on the center, return mid
                return mid
            elif nums[mid] < target: #If mid is to the left of the target
                return binary_search(mid + 1, high)
            else: #Then mid is to the right (above in sorted array) the target
                return binary_search(low, mid - 1)
    return binary_search(0, len(nums)-1)

print(search(nums, target))