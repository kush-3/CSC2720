def detect_fraud_cluster(grid, t):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return 0
        if grid[r][c] < t or (r, c) in visited:
            return 0
        visited.add((r, c))
        size = 1
        size += dfs(r+1, c)
        size += dfs(r-1, c)
        size += dfs(r, c+1)
        size += dfs(r, c-1)

        return size
    
    clusters = 0
    largest = 0 
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] >= t and (r,c) not in visited:
                size = dfs(r, c)
                clusters += 1
                largest = max(largest, size)
    
    return [clusters, largest ]

grid = [
  [1, 7, 8, 2],
  [3, 8, 9, 1],
  [2, 6, 3, 7],
  [5, 5, 7, 8]
]
t = 7

print(detect_fraud_cluster(grid, t))