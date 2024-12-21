"""
Given a 0-indexed string word and a character ch, 
reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). 
If the character ch does not exist in word, do nothing.

For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). 
The resulting string will be "dcbaefd".
Return the resulting string.

 Example 1:
Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"
Explanation: The first occurrence of "d" is at index 3. 
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".
"""

word = "abcdefd" 
ch = "d"
def reversePrefix(word, ch): #Obviously can be done in a one-liner, but anyone using two-pointer is a fool and overengineered a solution 
    toasting = ""
    word2 = "" #serve no meeaning except True or False check
    for char in word:
        toasting += char
        if char in ch:
            if word2 == "": #If True
                toasting = toasting[::-1]
                word2 += toasting #set the check to False
    return toasting

print(reversePrefix(word, ch))