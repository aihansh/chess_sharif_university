import chess_board

# Initialize an empty 8x8 board
board_bace = [["." for i in range(8)] for j in range(8)]

# Place black pieces
for piece in chess_board.black_pieces:
    row = 8 - piece.colmn
    col = ord(piece.row) - 97
    if 0 <= row < 8 and 0 <= col < 8:
        board_bace[row][col] = piece.shape

# Place white pieces
for piece in chess_board.white_pieces:
    row = 8 - piece.colmn
    col = ord(piece.row) - 97
    if 0 <= row < 8 and 0 <= col < 8:
        board_bace[row][col] = piece.shape

if __name__ == "__main__" :
    for row in board_bace:
        print(' '.join(row))