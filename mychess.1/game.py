import re
import players
import chess_board
import board
import myfunction
import imaplib

def reeding_request(text, side):
    pattern = r"(\w{4,6})\s+in\s+([a-h][1-8])\s+move\s+to\s+([a-h][1-8])"
    temp = re.search(pattern, text)
    if temp == None:
        pattern = r"(\w{4,5})+castle"
        temp = re.search(pattern, text)
        t = myfunction.castle(side, temp.group(1))
        return t
    piece_name = temp.group(1)
    location_of_piece = temp.group(2)
    l = list(location_of_piece)
    move_of_piece = temp.group(3)
    if side == "white":
        for i in chess_board.white_pieces :
            if i.name == piece_name and i.row == l[0] and i.colmn == l[1]:
                if i.moving(move_of_piece):
                    return True
                    break
    else:
        for i in chess_board.black_pieces :
            if i.name == piece_name and i.colmn == l[1] and i.row == l[0]:
                if i.moving(move_of_piece):
                    return True
                    break

request0 = input("I/'m  player1 and ready for cool game: ")
if request0 ==  'yes':
    request1 = input("I/'m  player2 and ready for cool game: ")
    if request1 == "yes":
        player1 = None
        player2 = None
        player1, player2 = players.chanse(player1, player2)
        if player1.side == "white":
            first = player1
            secend = player2
        else:
            first = player1
            secend = player2
        while True:
            request_white = input(f"{first.name} pleas write your select your piece : ")
            if reeding_request(request_white, "white"):
                imaplib.reload(board)
                for row in board.board_bace:
                    print(' '.join(row))
                request_black = input(f"{secend.name} pleas write your move: ")
                if reeding_request(request_black, "black"):
                    imaplib.reload(board)
                    for row in board.board_bace:
                        print(' '.join(row))
                else:
                    while True:
                        request_black = input(f"{secend.name} pleas write your move: ")
                        if reeding_request(request_black, "black"):
                            imaplib.reload(board)
                            for row in board.board_bace:
                                print(' '.join(row))
                        if request_black == "out" or request_white == "out":
                            print("the game is over")
                            break

            if request_black == "out" or request_white == "out":
                print("the game is over")
                break