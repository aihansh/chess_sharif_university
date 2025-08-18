import re
import chess_board
import myfunction
import ChessClockApp
import players
import class_of_pieces


def chanse(player1, player2):
    from random import randint
    coin = randint(0,1)
    if coin == 0 :
        player1 = players.white("player1")
        player2 = players.black("player2")
    else:
        player1 = players.black("player1")
        player2 = players.white("player2")
    return player1, player2


def reeding_request(text, side):


    '''the function that proceses the request'''


    pattern1 = r"([a-h][1-8])+\s+move+\s+to\s+([a-h][1-8])"
    temp = re.search(pattern1, text.lower())
    if not temp:
        pattern2 = r"(\w{4,5})+\s+castle"
        temp = re.search(pattern2, text)
        if not temp :
            return False
        type_castle = temp.group(1)
        myfunction.castle(type_castle, side)
    location_of_piece = temp.group(1)
    move_of_piece = temp.group(2)

    piece_row = location_of_piece[0]
    piece_col = int(location_of_piece[1])

    if side == "white":
        for i in chess_board.white_pieces:
            if i.row == piece_row and i.colmn == piece_col:
                return i.moving(move_of_piece)
    else:
        for i in chess_board.black_pieces:
            if i.row == piece_row and i.colmn == piece_col:
                return i.moving(move_of_piece)
    print("reading")
    return False

#game starting here
request0 = input("I'm player1 and ready for cool game: ")
if request0 == 'yes':
    request1 = input("I'm player2 and ready for cool game: ")
    if request1 == "yes":
        player1 = None
        player2 = None
        player1, player2 = chanse(player1, player2)

        if player1.side == "white":
            first = player1
            secend = player2
        else:
            first = player1
            secend = player2
        #game starting here
        clock = ChessClockApp.ChessClockApp()
        clock.active_side = "right" if first.side == "white" else "left"
        clock.toggle_start() 
        def anlizing_situation(side):
            our_pieces = chess_board.white_pieces if side == "white" else chess_board.white_pieces
            for me in our_pieces :
                for square in class_of_pieces.boerd:
                    square = list(square)
                    if not me.can_move_to_isnt_king_check(square[0], square[1]):
                        if side == "white":
                            if myfunction.is_king_checked_there(side, chess_board.kw.row, chess_board.kw.colmn):
                                import game
                                first.sitaution = "Lose"
                                secend.sitaution = "Win"
                            else:
                                import game
                                sitaution = "Draw"
                                sitaution = "Darw"
                        else:
                            if myfunction.is_king_checked_there(side, chess_board.kb.row, chess_board.kb.colmn):
                                import game
                                first.sitaution = "Win"
                                secend.sitaution = "Lose"
                            else:
                                import game
                                first.sitaution = "Draw"
                                secend.sitaution = "Darw"
        import os
        import board

        while True:
            os.system("cls" if os.name == "nt" else "clear")
            board.board_bace = [["." for _ in range(8)] for _ in range(8)]

            #updating the board
            for piece in chess_board.black_pieces:
                row = 8 - piece.colmn
                col = ord(piece.row) - 97
                if 0 <= row < 8 and 0 <= col < 8:
                    board.board_bace[row][col] = piece.shape

            for piece in chess_board.white_pieces:
                row = 8 - piece.colmn
                col = ord(piece.row) - 97
                if 0 <= row < 8 and 0 <= col < 8:
                    board.board_bace[row][col] = piece.shape

            for row in board.board_bace:
                print(' '.join(row))

            
            if first.side == "white":
                if first.situation == None :
                    request = input(f"{first.name} (white) enter your move: ")
                    while not reeding_request(request, "white"):
                        request = input("Invalid move. Try again: ")
                    anlizing_situation("black")
                    clock.press("right")
                else :
                    print(f"white is {first.situation} and black is {secend.situation}")


            else:
                if secend.situation == None :
                    request = input(f"{secend.name} (black) enter your move: ")
                    while not reeding_request(request, "black"):
                        request = input("Invalid move. Try again: ")
                        anlizing_situation("white")
                        clock.press("left")
                else :
                    print(f"white is {first.situation} and black is {secend.situation}")

            first, secend = secend, first
