import sys

chess_board = {
    '1h': 'bking', '6c': 'wqueen',
    '2g': 'bbishop', '5h': 'bqueen', 
    '3e': 'wking', '5a': 'bqueeneth',}

letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
pieces = ['king', 'rook', 'bishop', 'queen', 'knight', 'pawn']
players = {'b': 'black', 'w': 'white'}

def count_piece(my_piece):
    # This counts the number of times a piece is found in the chess board

    pieces = {}

    for piece in chess_board.values():
        count = pieces.setdefault(piece, 0)
        count += 1
        pieces[piece] = count
    
    return pieces[my_piece]

def check_validity():
    # This checks if the chess board is valid

    for coord, piece in chess_board.items():
        num_coord = int(coord[0])
        char_coord = coord[1]

        player = piece[0]
        curr_piece = piece[1:]

        if((num_coord not in range(1, 9)) or (char_coord not in letters) or (len(coord) != 2)):
            print(f"Invalid Board: The coordinate {coord} does not exist in chess") # if the first char is a number and the second char is btw a to h and the coord is only 2 chars
            sys.exit()

        if((curr_piece not in pieces) or (player not in players.keys())):
            print(f"Invalid Board: There is no {player} {piece[1:]} piece in chess")
            sys.exit()

        # check if any are repeated if the piece belongs to the available pieces for chess and that the pieces always start with a colour and ensure only one king

check_validity()