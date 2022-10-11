class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row, col = len(maze), len(maze[0])
        def valid(mat, row, col):
            if 0 <= row < len(mat) and 0 <= col < len(mat[0]):
                return True
            return False
        
        def isborder(i,j):
            if(i == 0 or i == row-1) or (j == 0 or j == col - 1):
                return True
            return False

        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        
        def bfs(mat,r,c,visited):
            #start
            visited.add((r,c))
            queue = [(r,c,0)]
            while queue:
                cell = queue.pop(0)
                for d in directions:
                    nrow, ncol, ndist = cell[0] + d[0], cell[1] + d[1], cell[2] + 1
                    if not valid(mat, nrow, ncol) or (nrow,ncol) in visited or mat[nrow][ncol] == "+":
                        continue
                    if mat[nrow][ncol] == "." and isborder(nrow,ncol):
                        return ndist
                    visited.add((nrow,ncol))
                    queue.append((nrow,ncol,ndist))
            return -1
        
        return bfs(maze, entrance[0],entrance[1],set())
