import chess_beord

# Initialize an empty 8x8 board
board_bace = [["." for i in range(8)] for j in range(8)]

# Place black pieces
for piece in chess_beord.black_pieces:
    row = 8 - piece.colmn
    col = ord(piece.row) - 97
    if 0 <= row < 8 and 0 <= col < 8:
        board_bace[row][col] = piece.shape

# Place white pieces
for piece in chess_beord.white_pieces:
    row = 8 - piece.colmn
    col = ord(piece.row) - 97
    if 0 <= row < 8 and 0 <= col < 8:
        board_bace[row][col] = piece.shape

# Print the board
for row in board_bace:
    print(' '.join(row))

x = input("Press Enter to exit")