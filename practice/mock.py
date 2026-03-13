def border(n):
    grid = [["-"] * n for _ in range(n)]

    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                grid[r][c] = "*"

    print(grid)
    return grid


border(5)