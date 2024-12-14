"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""


nums = [100,4,200,1,3,2]

#The entire difficulty is to make the algorithm 0(n) time

def longestConsecutive(nums):
    numSet = set(nums) #Typecasting it into a set makes its lookup O(n), hash dict works too
    longest = 0

    for num in numSet:
        if (num - 1) not in numSet: #The lookup in a set is O(n), we check every num if its num-1 is present in the set this way, 
            #if it's not :
            length = 1 #Resets back to 1 everytime a consecutive number reaches its end
            while (num + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest

print(longestConsecutive(nums))