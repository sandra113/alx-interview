#!/usr/bin/python3
"""
island_perimeter
"""

def island_perimeter(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with 4 sides for each land cell
                perimeter += 4

                #check the cell above (i-1,j)
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2  # one shared side with the cell above

                # Check the cell to the left (i, j-1)
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2  # One shared side with the cell to the left

    return perimeter