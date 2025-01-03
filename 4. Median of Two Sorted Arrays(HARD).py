"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

 Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

 Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""
nums1 = [1,2] 
nums2 = [3,4]
#Output : 2.5 (float)

def findMedianSortedArrays(nums1, nums2):
    """
    At first I thought of merging nums 1 and nums 2 using
    an algorithm to check if the next number is lower on nums1 or nums2,
    but I thought of bruteforcing it during implementation,
    and this pass every test cases on leetcode, even if it isn't
    O(log (m+n)) as stated and required by the wording of the problem,
    so that's why I included a second solution,
    (also it's a HARD difficulty question and this wasn't that hard)
    """
    
    merged = nums1 + nums2
    merged.sort()
    
    total = len(merged)

    if total % 2 == 1:
        return float(merged[total // 2])
    
    else:
        middle1 = merged[total // 2 - 1]
        middle2 = merged[total // 2]
        return (float(middle1) + float(middle2)) / 2.0
    
def findMedianSortedArrays2(nums1, nums2):
    #Two pointers solution
    len1, len2 = len(nums1), len(nums2)
    i = j = 0
    median1 = median2 = 0

    for count in range((len1 + len2) // 2 + 1):
        median2 = median1
        if i < len1 and j < len2:
            if nums1[i] > nums2[j]:
                median1 = nums2[j]
                j += 1
            else:
                median1 = nums1[i]
                i += 1
        elif i < len1:
            median1 = nums1[i]
            i += 1
        else:
            median1 = nums2[j]
            j += 1

    if (len1 + len2) % 2 == 1:
        return float(median1)
    else:
        return (median1 + median2) / 2.0
    
print (findMedianSortedArrays2(nums1, nums2))