"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true
"""


# My Approach would be to use a stack queue, brute forcing it seems too easy and too messy

s = "()"
#Output = True

def isValid(s):
    
    if len(s) %2 != 0:
        return False #To quickly check if the input is odd, so worth checking.
    else:
        pass

    stack = []
    dictos = {")":"(", "]":"[", "}":"{"}

    for x in s:
        if x in dictos:
            if stack and stack[-1] == dictos[x]: # [-1] refers to last item in stack, implying last item push to stack
                # This checks if stack item matches ht eitem in dictos
                stack.pop() # Delete last item in stack
            else:
                return False
        else:
            stack.append(x)
    if stack == []:
        return True
    else:
        return False #This is used for edge cases #95