def min_price(grid):
    rows = len(grid)
    cols = len(grid[0])

    from functools import lru_cache

    @lru_cache(None)
    def dfs(r, c, used_pass):
        # out of bounds
        if r >= rows or c >= cols:
            return float('inf')

        fee = grid[r][c]

        # reached destination
        if r == rows - 1 and c == cols - 1:
            if used_pass:
                return fee
            else:
                return min(fee, 0)  # optionally use pass here

        # move options
        right = dfs(r, c + 1, used_pass)
        down = dfs(r + 1, c, used_pass)
        diag = dfs(r + 1, c + 1, used_pass)

        # if pass already used
        cost_if_used = fee + min(right, down, diag)

        # if pass not used yet, we may use it here
        if not used_pass:
            right2 = dfs(r, c + 1, True)
            down2 = dfs(r + 1, c, True)
            diag2 = dfs(r + 1, c + 1, True)
            cost_use_here = 0 + min(right2, down2, diag2)
            return min(cost_if_used, cost_use_here)

        return cost_if_used


grid = [
    [3, 2 ,8],
    [1, 9, 1],
    [7, 2, 3],
]

print(min_price(grid))