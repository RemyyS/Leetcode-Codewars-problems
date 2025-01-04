"""Given the head of a singly linked list, reverse the list, and return the reversed list.

 Example 1:
 Input: head = [1,2,3,4,5]
 Output: [5,4,3,2,1] 
"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev = None
        curr = head # Setting pointers : We setup the prev and curr values to None (meaning the first linked list previous node is Null) 
                    #and current as HEAD, because it's the first one we receive
        while curr: #Loops as long as the linked list is not over iterating
            nxt = curr.next #Temporary variable to store current value, because we'll save another value to "curr" later
            curr.next = prev #I want to set the next linked list to previous (None if it's the first one)
            prev = curr
            curr = nxt #This is why we had to set nxt to curr.next at the beginning of the loop
        return prev #It's where the last value is stored when the loop ends
        
