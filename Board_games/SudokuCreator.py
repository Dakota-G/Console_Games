import random

# TODO:
# Create a function to seed a 9x9 grid 
# Use the SudokuSolver to solve that grid completely (this will ensure it is valid)
# Remove spaces from the grid
# Spaces removed determined by difficulty?

def seed_grid():
    global grid
    grid =  [[],[],[],[],[],[],[],[],[]]
    numbers = [1,2,3,4,5,6,7,8,9]
    places = [0,1,2,3,4,5,6,7,8]
    for row in grid:
        insert = numbers.pop(random.randint(0, len(numbers)-1))
        place = places.pop(random.randint(0, len(places)-1))
        for x in range(9):
            if x == place:
                row.append(insert)
            else:
                row.append(0)
    return solve_grid()

def show_grid(x):
    for i in x:
        print(i)
    
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
    return create_spaces()

def create_spaces():
    global grid
    for row in grid:
        while row.count(0) < 6:
            x = random.randint(0,8)
            y = random.randint(0,8)
            grid[y][x] = 0
    return show_grid(grid)
                
seed_grid()