class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def findemptycell(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        return(i,j)
            return None
        def possible(emptycell, value):
            row = emptycell[0]
            col = emptycell[1]
            startrow = (row // 3) * 3
            startcol = (col // 3) * 3
            if value in board[row] or value in list(zip(*board))[col]:
                return False
            for i in range(startrow,startrow+3):
                for j in range(startcol,startcol+3):
                    if board[i][j] == value:
                        return False
            return True       
                    
        def fill(board):
            emptycell = findemptycell(board)
            if emptycell == None:
                return True
            
            for i in range(1,10):
                if possible(emptycell, str(i)):
                    board[emptycell[0]][emptycell[1]] = str(i)
                    if fill(board) == True:
                        return True
                    else:
                        board[emptycell[0]][emptycell[1]] = "."
            return False
        
        fill(board)
