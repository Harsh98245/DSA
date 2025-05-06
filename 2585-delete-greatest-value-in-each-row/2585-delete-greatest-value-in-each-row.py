class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Step 1: Sort each row in ascending order
        for row in grid:
            row.sort()
        
        result = 0
        n = len(grid[0])  # number of columns

        # Step 2: Iterate over each column from last to first
        for col in range(n - 1, -1, -1):
            max_val = 0
            for row in grid:
                max_val = max(max_val, row[col])
            result += max_val

        return result
