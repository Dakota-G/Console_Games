def StartGame():
    global moveset
    moveset = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}
    print("Let's begin! X goes first!")
    return request_move('X')

def print_grid():
    print(f"{moveset['1']} | {moveset['2']} | {moveset['3']}")
    print("---------")
    print(f"{moveset['4']} | {moveset['5']} | {moveset['6']}")
    print("---------")
    print(f"{moveset['7']} | {moveset['8']} | {moveset['9']}")
 
def request_move(symbol):
    print(f"It is {symbol}'s turn!")
    print_grid()
    move = input(f"Where would you like to place your {symbol}?")
    return make_move(move, symbol)
 
def make_move(place, symbol):
    # Make sure that the place selected is between 1-9 (on the grid)
    if(int(place) > 9 or int(place) < 1):
        print("Sorry, that isn't a valid placement! Select a number between 1 and 9!")
        return request_move(symbol)
    # Make sure that the place selected is empty
    if(moveset[place]) == 'X' or (moveset[place]) == 'O':
        print("Sorry, that space is taken!")
        return request_move(symbol)
    # If the placement is valid, set the symbol and check for a win/stalemate
    else:
        moveset[place] = symbol
        return check_grid(symbol)
 
def check_grid(symbol):
    # Check columns and rows for a 3-way match
    for i in range(1, 10, 3):
        if(moveset[str(i)] == moveset[str(i+1)] == moveset[str(i+2)]):
            print_grid()
            print(f"{symbol} wins!")
            input("Press Enter to Play Again")
            return StartGame()
    for i in range(1, 4):
        if(moveset[str(i)] == moveset[str(i+3)] == moveset[str(i+6)]):
            print_grid()
            print(f"{symbol} wins!")
            input("Press Enter to Play Again")
            return StartGame()
    # Check diagonals for 3-way match
    if(moveset['1'] == moveset['5'] == moveset['9']):
            print_grid()
            print(f"{symbol} wins!")
            input("Press Enter to Play Again")
            return StartGame()
    elif(moveset['3'] == moveset['5'] == moveset['7']):
            print_grid()
            print(f"{symbol} wins!")
            input("Press Enter to Play Again")
            return StartGame()
    # Check for stalemate
    stalemate = True
    for key in moveset:
        if(moveset[key] != 'X' and moveset[key] != 'O'):
            stalemate = False
    if stalemate == True:
            print_grid()
            print("Stalemate! Nobody won!")
            input("Press Enter to Play Again")
            return StartGame()
    print("No winner yet!")
    # If no win/stalemate conditions are met, let the other player make a move
    if(symbol == 'X'):
        return request_move('O')
    return request_move('X')
 
StartGame()
