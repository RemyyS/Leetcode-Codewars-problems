from collections import defaultdict

"""
Given an array of strings strs, group the 
anagrams together. You can return the answer in any order.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
"""

strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


def groupAnagrams(strs): #Must return list of lists
    res = defaultdict(list)
    for s in strs:
        sortedS = ''.join(sorted(s)) #Using a trick there to solve the problem, I sort every word in the strs argument, making an anagram effectively a copy of eachother
        res[sortedS].append(s)
    return list(res.values())

print (groupAnagrams(strs))