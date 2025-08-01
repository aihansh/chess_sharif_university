import re
import players
import chess_board
import myfunction

def reeding_request(text, side):
    pattern = r"(\w{4,6})\s+in+\s+([a-h][1-8])+\s+move+\s+to\s+([a-h][1-8])"
    temp = re.search(pattern, text.lower())  # تبدیل به حروف کوچک
    if not temp:
        return False
        
    piece_name = temp.group(1)
    location_of_piece = temp.group(2)
    move_of_piece = temp.group(3)
    
    # تبدیل موقعیت به فرمت مناسب
    piece_row = location_of_piece[0]
    piece_col = int(location_of_piece[1])
    
    if side == "white":
        for i in chess_board.white_pieces:
            if i.name.lower() == piece_name.lower() and i.row == piece_row and i.colmn == piece_col:
                return i.moving(move_of_piece)
    else:
        for i in chess_board.black_pieces:
            if i.name.lower() == piece_name.lower() and i.row == piece_row and i.colmn == piece_col:
                return i.moving(move_of_piece)
    print("reeding")
    return False


request0 = input("I\'m  player1 and ready for cool game: ")
if request0 ==  'yes':
    request1 = input("I\'m  player2 and ready for cool game: ")
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
    # نمایش صفحه بعد از هر حرکت 
            import os
            os.system("cls")
            import board
            board.board_bace = [["." for _ in range(8)] for _ in range(8)]
    
    # آپدیت صفحه
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
    
    # دریافت حرکت بازیکن فعلی
            if first.side == "white":
               request = input(f"{first.name} (white) enter your move: ")
               while not reeding_request(request, "white"):
                    request = input("Invalid move. Try again: ")
            else:
                request = input(f"{secend.name} (black) enter your move: ")
                while not reeding_request(request, "black"):
                     request = input("Invalid move. Try again: ")
    # تعویض نوبت
            first, secend = secend, first