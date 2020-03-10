# TODO: Need to add a board check to return a win or a draw


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
    for x in range(1, 6):
# Check rows
        if(
        board[x][2] and board[x][3] and board[x][4] and board[x][5] == piece) or (
        board[x][1] and board[x][2] and board[x][3] and board[x][4] == piece) or(
# Check columns 
        board[2][x] and board[3][x] and board[4][x] and board[5][x] == piece) or (
        board[1][x] and board[2][x] and board[3][x] and board[4][x] == piece):
            print(f"{piece} wins!")

# Check diagonals



def start_game():
    print("Let's play connect four!")
    request_move('X')

start_game()
