
board = [   ['::', '1','2','3','4','5'],
            ['5:','_','_','_','_','_',],
            ['4:','_','_','_','_','_',],
            ['3:','_','_','_','_','_',],
            ['2:','_','_','_','_','_',],
            ['1:','_','_','_','_','_',]
        ]

def place_move(place, piece):
    global board
    for row in board:
        if row[place] == '_':
            row[place] = piece
            check_board(piece)
            if piece == 'X':
                return request_move('O')
            else:
                return request_move('X')
    print("Sorry, column appears to be full! Try Again!")
    return request_move(piece)

def request_move(piece):
    global board
    print(f"It is {piece}'s turn!")
    print_board()
    place = int(input("Which column will you drop your piece into?"))
    if(place > 5 or place < 1):
        print('Please select a column between 1 and 5!')
        return request_move(piece)
    return place_move(place, piece)

def print_board():
    global board
    print(board[5])
    print(board[4])
    print(board[3])
    print(board[2])
    print(board[1])
    print(board[0])


def check_board(piece):
    global board
    draw = True
    for x in range(1, 6):
# Check rows
        if(
        board[x][2] == piece and board[x][3] == piece and board[x][4] == piece and board[x][5] == piece) or (
        board[x][1] == piece and board[x][2] == piece and board[x][3] == piece and board[x][4] == piece):
            print_board()
            print(f"{piece} wins on row {x}!")
            return reset_game()
# Check columns 
        elif(
        board[2][x] == piece and board[3][x] == piece and board[4][x] == piece and board[5][x] == piece) or (
        board[1][x] == piece and board[2][x] == piece and board[3][x] == piece and board[4][x] == piece):
            print_board()
            print(f"{piece} wins on column {x}!")
            return reset_game()
# Check diagonals
    for x in range(1,3):
        if (board[x][1] == piece and board[x+1][2] == piece and board[x+2][3] == piece and board[x+3][4] == piece) or (
            board[x][2] == piece and board[x+1][3] == piece and board[x+2][4] == piece and board[x+3][5] == piece) or (
            board[x][4] == piece and board[x+1][3] == piece and board[x+2][2] == piece and board[x+3][1] == piece) or (
            board[x][5] == piece and board[x+1][4] == piece and board[x+2][3] == piece and board[x+3][2] == piece):
                print_board()
                print(f"{piece} wins on the diagonal!")
                return reset_game()
    for row in board:
        for space in row:
            if space == '_':
                draw = False
    if draw == True:
        print_board()
        print("Looks like a draw! Nobody wins!")
        return reset_game()

def reset_game():
    input("Press Enter to play again!")
    for x in range(1,6):
        board[1][x] = '_'
        board[2][x] = '_'
        board[3][x] = '_'
        board[4][x] = '_'
        board[5][x] = '_'
    start_game()

def start_game():
    print("Let's play connect four!")
    request_move('X')

start_game()
