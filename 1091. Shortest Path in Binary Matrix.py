class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def valid(mat, row, col):
            if 0 <= row < len(mat) and 0 <= col < len(mat[0]):
                return True
            return False

        directions = ((0, 1), (1, 0), (0, -1), (-1, 0), (1,1), (-1,-1), (-1,1), (1,-1)) 

        def bfs(mat,r,c,visited):
            #start
            visited.add((r,c))
            queue = [(r,c,1)]
            while queue:
                cell = queue.pop(0)
                
                for d in directions:
                    nrow, ncol, ndist = cell[0] + d[0], cell[1] + d[1], cell[2] + 1
                    if not valid(mat, nrow, ncol) or (nrow,ncol) in visited or mat[nrow][ncol] == 1:
                        continue
                    if nrow == len(mat) - 1 and ncol == len(mat[0]) - 1:
                        return ndist
                    visited.add((nrow,ncol))
                    queue.append((nrow,ncol,ndist))
            return -1
            
        if grid[0][0] == 1 or grid[len(grid)-1][len(grid[0])-1] == 1:
            return -1
        if len(grid) == 1 and len(grid[0]) == 1 and grid[0][0] == 0:
            return 1
             
        return bfs(grid,0,0,set())
