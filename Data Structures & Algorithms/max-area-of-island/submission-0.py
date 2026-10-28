class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        r, c = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] != 1:
                return 0
            grid[i][j] = 0
            count = 1
            count += dfs(i + 1, j)
            count += dfs(i, j + 1)
            count += dfs(i - 1, j)
            count += dfs(i, j - 1)
            return count
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res