# Solves sudoku puzzles using recursive recall
# This was discussed on Computerphile's youtube channel

# sample sudoku problem
grid =  [  [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9] ]

def check_grid(y, x, number):
    global grid
# This checks for number matches along each row
    for i in range(0, 9):
        if grid[y][i] == number:
            return False
# This checks for number matches down each column
    for i in range(0, 9):
        if grid[i][x] == number:
            return False
# This checks for number matches on the 3x3 squares
    xx = (x//3)*3
    yy = (y//3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[yy+i][xx+j] == number:
                return False
# If there are no matches, blocking the number, return True
    return True

def solve_grid():
    global grid
# This checks each row, one-by-one, looking for 0, which indicates an empty place
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
# Check each number from 1-9 in that empty spot by using the check_grid function created above
# When that function returns True, that number is placed in the square and the function moves on
                for number in range(1, 10):
                    if check_grid(y, x, number):
                        grid[y][x] = number
                        solve_grid()
# If the function ever finds a square where no numbers can be placed, then it resets that position to 0 and returns
# The return function forces the recursive recall to return to a previously marked number to see if it can be changed
# If that previously guessed position cannot be solved, then the function continues to recall, eventually correcting the error
                        grid[y][x] = 0
                return
    show_grid(grid)

def show_grid(x):
    for i in x:
        print(i)

solve_grid()