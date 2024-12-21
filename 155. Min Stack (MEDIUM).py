"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Example 1:
Input:
 ["MinStack","push","push","push","getMin","pop","top","getMin"]
 [[],[-2],[0],[-3],[],[],[],[]]
Output:
 [null,null,null,null,-3,null,0,-2]
"""

Input = ["MinStack","push","push","push","getMin","pop","top","getMin"][[],[-2],[0],[-3],[],[],[],[]]

class MinStack: #0(1) time complexity, as the description asked

    def __init__(self):
        self.stack = []
        self.minvaluestack = [] #Initialize a second stack that will only store the minimum value up to this point, min value will take from this stack

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if self.minvaluestack != []: #We check that the stack is not empty, if not we append the value as is
            newval = min(val, self.minvaluestack[-1]) #newval checks if the value appended is lower than the lowest item in the minvaluestack
            return self.minvaluestack.append(newval) 
        else:
            return self.minvaluestack.append(val)
        #I could have replaced the name "newval" by "val" and appended "val" in a one-liner (without the if-else staterment), but I think this is cleaner and more readable
        
    def pop(self) -> None:
        self.stack.pop()
        self.minvaluestack.pop()
    
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minvaluestack[-1]
    
