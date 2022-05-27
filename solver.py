
from re import L


class SudokuSolver:
    WHITE = (255, 255, 255)

    def solve(self, grid, surface, x, y, quite_mode=False):
        
        temp_grid = grid.editable_grid
        while grid.default_grid[y][x] != 0 or temp_grid[y][x] != 0:
            if x < 8:
                x += 1
            elif x == 8 and y < 8:
                x = 0
                y += 1
            elif x == 8 and y == 8:  # the base case
                return True
        for value in range(1, 10):
            if grid.check_valid_position(x, y, value):
                temp_grid[y][x] = value

                if self.solve(grid, surface, x, y):
                    if not quite_mode:
                        grid.editable_grid = temp_grid
                    return True

                # if there is no possible value, reset the cell value.
                temp_grid[y][x] = 0
        if not quite_mode:
            grid.editable_grid = temp_grid
        return False
