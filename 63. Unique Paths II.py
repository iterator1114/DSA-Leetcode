class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #Valid cell and the directions tuple
        from functools import lru_cache
        import math
        global count
        def valid(mat, row, col):
            if 0 <= row < len(mat) and 0 <= col < len(mat[0]):
                return True
            return False

        directions = ((0, 1), (1, 0))


        @lru_cache(maxsize = None)
        def dfs(mat, r, c): 
            if r == len(mat) - 1 and c == len(mat[0]) - 1:
                return 1
            sols = 0
            for d in directions:
                nrow , ncol = r+d[0] , c+d[1]
                if not valid(mat, nrow, ncol) or mat[nrow][ncol] == 1:
                    continue
                sols += dfs(mat, nrow, ncol)
            return sols
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        print(count)
        obstacleGrid = tuple(map(tuple, obstacleGrid))
        return dfs(obstacleGrid, 0, 0)

       
        
