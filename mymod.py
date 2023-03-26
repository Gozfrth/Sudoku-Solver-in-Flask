def sol(whole_grid):
    def is_legal(grid, row, col, num):
        return not in_row(grid, row, num) and not in_col(grid, col, num) and not in_box(grid, row, col, num)

    def in_row(grid, row, num):
        for i in range(len(grid)):
            if grid[row][i] == num:
                return True
        return False

    def in_col(grid, col, num):
        for i in range(len(grid[0])):
            if grid[i][col] == num:
                return True
        return False

    def in_box(grid, row, col, num):
        for i in range((row // 3) * 3, (row // 3) * 3 + 3):
            for j in range((col // 3) * 3, (col // 3) * 3 + 3):
                if grid[i][j] == num:
                    return True
        return False

    def find_zero(grid):
        for i in range(9):
            for j in range(9):
                if not grid[i][j]:
                    return i, j
        return None

    def solve(grid):
        temp = find_zero(grid)
        if not temp:
            print('done')
            return True
        else:
            row, col = temp
        for n in range(1, 10):
            if is_legal(grid, row, col, n):
                grid[row][col] = n
                if solve(grid):
                    return True
                grid[row][col] = 0
        return False

    grid_copy = [[whole_grid[i][j] for j in range(9)] for i in range(9)]
    print(grid_copy)
    solve(grid_copy)
    print(grid_copy)
    return grid_copy


if __name__ == '__main__':
    # Add test code here if you want to test the module by running this file directly
    pass
