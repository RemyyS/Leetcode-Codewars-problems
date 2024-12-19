"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
"""

#Input: nums = [0,1,1]
#Output: []
#Explanation: The only possible triplet does not sum up to 0.


nums = [-1,0,1,2,-1,-4]
#Output: [[-1,-1,2],[-1,0,1]]

def threeSum(nums):
    incrIndex = 1 #Used to increment index
    solution = []
    target = 0 #Does not need to be declared, I just have to replace "target" by 0 everywhere, but makes the code a tiny bit more flexible
    l = 0 #left pointer
    r = len(nums) - 1
    sum = 0 #sum in this case being the number that's to be added to the 2 pointers, NOT the literal sum
    nums.sort() #Sorting the array makes the algorithm faster, and allows us to use the two-pointer solution used in 167.Two sums II on leetcode
    for x in nums:
        
        sum = x
        l = 0 + incrIndex
        r = len(nums) - 1
        incrIndex +=1
        while l < r:
            if nums[l] + nums[r] + sum < target:
                
                l+=1
            elif nums[l] + nums[r] + sum > target:
                r-=1
            else: 
                solution.append([nums[l], nums[r], sum])
                l+=1
    #To eliminate duplicates:
    list2 = []
    if len(solution) >= 2: 
        for q in solution:
            if q not in list2:
                list2.append(q)
                
        return list2
    return solution            

print (threeSum(nums))

#Different solution used on Leetcode because my solution gets a time limit error on the site only on last edge cases(with massive input numbers), even if my solution is big O(n^2), like other two pointers solutions that passed. This is a bug on their site, as stated by many users in the comment section. A few years ago my code would have passed, but with time Leetcode gets slower/less memory is used for tests, IDK