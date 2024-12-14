from collections import *

nums = [1,1,1,2,2,3] 
k = 2

"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
"""



def topKFrequent(nums, k):
    ans = [] #To return
    mydict = defaultdict(int) #Defaultdict used to track how many times each element appears in nums
    for x in nums:
        mydict[x] +=1
    mydictsorted = {z: v for z, v in sorted(mydict.items(), key=lambda item: item[1])} #Sorts by values, not keys
    inv_map = dict(reversed(list(mydictsorted.items()))) #Reverse the Dict sorted by values
    for i,v in enumerate(inv_map):
        ans.append(v)
    return (ans[:k]) #Returns list up to "k" argument

print (topKFrequent(nums, k))