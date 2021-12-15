# create a grid of array with an array inside it which is the rows.
import numpy as np
grid = [[0,0,0,0,0,0,2,0,0],
        [0,8,0,0,0,7,0,9,0],
        [6,0,2,0,0,0,5,0,0],
        [0,7,0,0,6,0,0,0,0],
        [0,0,0,9,0,1,0,0,0],
        [0,0,0,0,2,0,0,4,0],
        [0,0,5,0,0,0,6,0,3],
        [0,9,0,4,0,0,0,7,0],
        [0,0,6,0,0,0,0,0,0]]

def check_number(row, col, number):
        global grid
        #is number present in the row
        for r in range(0,9):
                if grid[row][r] == number:
                        return False

        # is number present in the column
        for r in range(0,9):
                if grid[r][col] == number:
                        return False

        # is number present in the square
        r0 = (row//3) * 3
        c0 = (col//3) * 3

        for i in range(0,3):
                for j in range(0,3):
                        if grid[r0 + i][c0 + j] == number:
                                return False

        return True

def solve():
        global grid
        for row in range(0,9):
                for col in range(0,9):
                        if grid[row][col]==0:
                                for number in range(1, 10):
                                        if check_number(row, col, number):
                                                grid[row][col] = number
                                                solve()
                                                grid[row][col] = 0
                                return
        print(np.matrix(grid))
        input('more possible solutions')

solve()


