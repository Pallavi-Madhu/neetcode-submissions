class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        count = 0
        visit = set()

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))

            while q:
                r,c = q.popleft()
                direction = [[1,0],[0,1],[-1,0],[0,-1]]
                for dr,dc in direction:
                    row = r + dr
                    col = c + dc

                    if(row in range(ROWS) and col in range(COLS) 
                    and grid[row][col] == '1' and (row,col) not in visit):
                        q.append((row,col))
                        visit.add((row,col))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visit:
                    bfs(r,c)
                    count += 1
        return count
