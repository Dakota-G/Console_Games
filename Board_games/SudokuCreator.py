import random

# !!Global boolean 'solved' allows us to get out of the recursion, otherwise, the program will try to come up with every possible sudoku grid..
# Spaces removed determined by difficulty?

def seed_grid():
    global grid
    global solved
    grid =  [[],[],[],[],[],[],[],[],[]]
    numbers = [1,2,3,4,5,6,7,8,9]
    places = [0,1,2,3,4,5,6,7,8]
    solved = False
    for row in grid:
        insert = numbers.pop(random.randint(0, len(numbers)-1))
        place = places.pop(random.randint(0, len(places)-1))
        for x in range(9):
            if x == place:
                row.append(insert)
            else:
                row.append(0)
    solve_grid()
    return create_spaces()

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
    global solved
# This checks each row, one-by-one, looking for 0, which indicates an empty place
# The global solved variable where will stop the recursive call from continuing if it is set to True
    if solved == False:
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
# Set solved to True to keep the recursion from getting deeper, return to make the way back out of the recursive stack
    solved = True
    return

# This will randomly go through the grid's rows and add 'blank spaces' in the form of '0's
def create_spaces():
    global grid
    for i, row in enumerate(grid):
        blanks = random.randint(6,8)
        while row.count(0) < blanks:
            x = random.randint(0,8)
            grid[i][x] = 0
        print(row)

seed_grid()