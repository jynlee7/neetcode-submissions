class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we should check each row and column
        # then we should check the nine 3x3 sub-boxes
        # for doing that I think that we should int divide by 3
        # i would be the column number then i / 3 would be which
        # row we would filter through

        for row in range(len(board)):
            for col in range(len(board)):
                valid = set()
                if board[row][col] == ".":
                    continue
                if board[row][col] in valid:
                    return False
                valid.add(board[row][col])
        
        for col in range(len(board)):
            for row in range(len(board)):
                valid = set()
                if board[row][col] == ".":
                    continue
                if board[row][col] in valid:
                    return False
                valid.add(board[row][col])

        for square in range(len(board)):
            valid = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in valid:
                        return False
                    valid.add(board[row][col])

        return True
