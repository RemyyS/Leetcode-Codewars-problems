"""
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
"""

heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# Output: 49


# The below brute-force solution works, but does not pass the Time Limit requirement.
def maxArea(heights):
    res = 0
    for i in range(len(heights)):
        for j in range(i + 1, len(heights)):
            res = max(res, min(heights[i], heights[j]) * (j - i))
    return res


# print(maxArea(height))


def maxArea2(heights):
    l = 0
    r = len(heights) - 1
    result = 0

    while l < r:  # setting up the two pointer solution
        area = (r - l) * min(heights[l], heights[r])  # right pointer - left pointer, multiplied by the height of the minimal height of the pointer, min necessary because we are calculating water that tops off the minimum height
        result = max(result, area)  # Conserve the biggest result
        if (heights[l] <= heights[r]):  # Usually it's "<" and not "<=", the equal sign is necessary for edge cases where the two height are the same, moving one side or the other does not matter
            l += 1
        else:
            r -= 1
    return result


print(maxArea2(heights))
