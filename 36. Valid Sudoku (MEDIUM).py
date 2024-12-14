"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
"""

board=[
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]
]

#Output: true

def isValidSudoku(board): # Big O(9²)
        #Would also work with a defaultdict(set) for colums, rows, and squares
        for row in range(9):
            seen = set() #Used to check rule 1
            for i in range(9): #Checks every cell and put it in hash set
                if board[row][i] == ".": 
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])
        
        for col in range(9):
            seen = set() #Used to check rule 2
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])
            
        for square in range(9): #Used to check duplicates in the the 3x3 grid the cell is in, the trickiest part
            seen = set()
            #The nested for loops below allows to divide the 3x3 entire sudoku grid
            #For edge case values  8x8 (the cell at the 9th row, 9th column), 8 divided by 3 rounds down the integer division to 2,
            #  so the cell at the 9th row and 9th column in in the grid (2,2), which is the third one to the right, third one to the bottom
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True #when every single cell has been checked

print(isValidSudoku(board))