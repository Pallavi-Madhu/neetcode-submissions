class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        visit = set()
        maxC = 0

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))
            count = 1

            while q:
                row,col = q.popleft()
                direction = [[1,0],[0,1],[-1,0],[0,-1]]
                for dr,dc in direction:
                    r = row + dr
                    c = col + dc
                    if ( r in range(ROWS) and c in range(COLS) 
                    and grid[r][c] == 1 and (r,c) not in visit):
                        count += 1
                        q.append((r,c))
                        visit.add((r,c))
            return count


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visit:
                    maxC = max(bfs(r,c),maxC)
        return maxC