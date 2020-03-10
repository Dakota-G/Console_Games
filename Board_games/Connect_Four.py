board = [   ['5:','_','_','_','_','_',],
            ['4:','_','_','_','_','_',],
            ['3:','_','_','_','_','_',],
            ['2:','_','_','_','_','_',],
            ['1:','_','_','_','_','_',],
            ['::', '1','2','3','4','5']
        ]

def place_move(place, board, piece):
    for row in board:
        if row[place] == '_':
            row[place] = piece
            if piece == 'X':
                return request_move(board, 'O')
            else:
                return request_move(board, 'X')
    print("Sorry, column appears to be full! Try Again!")
    return request_move(board, piece)

def request_move(board, piece):
    print(f"It is {piece}'s turn!")
    print_board(board)
    place = int(input("Which column will you drop your piece into?"))
    if(place > 5 or place < 1):
        print('Please select a column between 1 and 5!')
        return request_move(board, piece)
    return place_move(place, board, piece)

def print_board(board):
    print(board[4])
    print(board[3])
    print(board[2])
    print(board[1])
    print(board[0])
    print(board[5])

# TODO: Need to add a board check to return a win or a draw

def start_game(board):
    print("Let's play connect four!")
    request_move(board, 'X')

start_game(board)
