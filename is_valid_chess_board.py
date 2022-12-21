import sys

chess_board = {
    '1h': 'bking', '6c': 'wqueen',
    '2g': 'bbishop', '5h': 'bqueen', 
    '3f': 'wking', '6c': 'wrook'}

print(chess_board)    

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

def count_coordinates():
    # This counts the number of times a piece is found in the chess board

    coords = {}

    for coord in list(chess_board.keys()):
        count = coords.setdefault(coord, 0)
        count += 1
        coords[coord] = count
    
    return coords


def check_validity():
    # This checks if the chess board is valid

    for coord, piece in chess_board.items():
        num_coord = int(coord[0])
        char_coord = coord[1]

        player = piece[0]
        curr_piece = piece[1:]

        used_pieces = count_coordinates
        avail_pieces = list(chess_board.values())

        # if the first char is a number and the second char is btw a to h and the coord is only 2 chars
        if((num_coord not in range(1, 9)) or (char_coord not in letters) or (len(coord) != 2)):
            print(f"Invalid Board: The coordinate {coord} does not exist in chess") 
            sys.exit()
        # if the first letter of the piece is a valid player and the second is a valid piece
        if((curr_piece not in pieces) or (player not in players.keys())):
            if(player not in players.keys()):
                print(f"Invalid Board: There is no {player} {piece[1:]} piece in chess")
            else:
                print(f"Invalid Board: There is no {(players[piece[0]]).upper()} {(piece[1:]).title()} piece in chess")
            sys.exit()
        # if one king is missing      
        if('bking' not in avail_pieces):
            print(f"You are missing a BLACK King")
            sys.exit()
        if('wking' not in avail_pieces):
            print(f"You are missing a WHITE King")
            sys.exit()
        # if there is more than more king 
        if((count_piece('bking') > 1) or (count_piece('wking') > 1)):
            print(f"You can't have more than one {(players[piece[0]]).upper()} {(piece[1:].title())} in chess")
            sys.exit()

    print('Valid Chess Board you have there😊')

# check_validity()

print(count_coordinates())
# write a function that counts the coord used