import chess_board
import class_of_pieces
import copy
import players


#for analyzing rook move

def isnt_blocked_rook_white(row, colmn, mrow, mcolmn):
    if row != mrow and colmn != int(mcolmn):
        return False  

    direction = (0, 1) if colmn < int(mcolmn) else (0, -1) if colmn > int(mcolmn) else (1, 0) if ord(row) < ord(mrow) else (-1, 0)
    steps = max(abs(ord(mrow) - ord(row)), abs(int(mcolmn) - colmn)) - 1  # تعداد خانه‌های بین

    current_row = ord(row)
    current_colmn = colmn
    dx, dy = direction if row == mrow else (direction[0] * (ord(mrow) > ord(row) and 1 or -1), 0)  # تنظیم جهت درست

    for _ in range(steps):
        current_row += dx
        current_colmn += dy
        cr = chr(current_row)
        cc = current_colmn

        for p in chess_board.white_pieces + chess_board.black_pieces:
            if p.row == cr and p.colmn == cc:
                return False  


    for p in chess_board.white_pieces:
        if p.row == mrow and int(p.colmn) == int(mcolmn):
            return False 
    return True 


def isnt_blocked_rook_black(row, colmn, mrow, mcolmn):
    if row != mrow and colmn != int(mcolmn):
        return False  
    
    if row == mrow:  
        dx = 0
        dy = 1 if colmn < int(mcolmn) else -1
    else:  
        dy = 0
        dx = 1 if ord(row) < ord(mrow) else -1

    steps = max(abs(ord(mrow) - ord(row)), abs(int(mcolmn) - colmn)) - 1 

    current_row_ord = ord(row)
    current_colmn = colmn

    for _ in range(steps):
        current_row_ord += dx
        current_colmn += dy
        cr = chr(current_row_ord)
        cc = current_colmn

        for p in chess_board.white_pieces + chess_board.black_pieces:
            if p.row == cr and p.colmn == cc:
                return False 
    for p in chess_board.black_pieces:
        if p.row == mrow and int(p.colmn) == int(mcolmn):
            return False
    return True  

#for analyzing bishope move


def is_blocked_bishope(side, r, c, mr, mc):
    my_move = []
    directions = [(1,1), (1,-1), (-1,1), (-1,-1)]  # All diagonals
    own_pieces = chess_board.white_pieces if side == "white" else chess_board.black_pieces
    enemy_pieces = chess_board.black_pieces if side == "white" else chess_board.white_pieces
    for dx, dy in directions:
        x, y = ord(r) - 97 + dx, c + dy  # Convert to 0-7 indexing
        while 0 <= x < 8 and 0 <= y < 8:
            loc = class_of_pieces.location(chr(x + 97), y)
            found_own = any(p.row == loc.row and p.colmn == loc.colmn for p in own_pieces)
            if found_own:
                break
            found_enemy = any(p.row == loc.row and p.colmn == loc.colmn for p in enemy_pieces)
            my_move.append(loc)
            if found_enemy:
                break
            x += dx
            y += dy
    return any(loc.row == mr and loc.colmn == mc for loc in my_move)
    

#for analyzing pawn move

def isnt_bolcked_pawn(side, r, c):
    if side == "white":
        loc = class_of_pieces.location(r, c+1)
    elif side == "black":
        loc = class_of_pieces.location(r , c-1)
    for i in chess_board.white_pieces :
        if loc.row == i.row and loc.colmn == i.colmn :
            return False
    for i in chess_board.black_pieces:
        if loc.row == i.row and loc.colmn == i.colmn:
            return False
    return True



def isnt_bolcked_pawn_for_start(side, r, c):
    for k in range(1,3):
        if side == "white":
            loc = class_of_pieces.location(r, c+k)
        else:
            loc = class_of_pieces.location(r , c-k)
        for i in chess_board.white_pieces :
            if loc.row == i.row and loc.colmn == i.colmn :
                return False
        for i in chess_board.black_pieces:
            if loc.row == i.row and loc.colmn == i.colmn :
                return False
    print("black")
    return True





def pawn_capchering(pawn, mrow, mcolmn):
    if  ord(pawn.row) + 1 == ord(mrow) or ord(pawn.row) - 1 == ord(mrow):
        if pawn.side == "white" and pawn.colmn + 1 == mcolmn:
            for i in chess_board.black_pieces:
                if i.row == mrow and i.colmn == mcolmn:
                    del i
                    return True
        elif pawn.side == " black" and pawn.colmn - 1 == mcolmn:
            for i in chess_board.white_pieces :
                if i.row == mrow and i.colmn == mcolmn:
                    del i 
                    return True
    return False


def is_starting(pawn, mcolmn):
    if pawn.side == "white" and pawn.c == 2 and mcolmn == 4 :
        for i in chess_board.pawn_list_black:
            if i.colmn == 4 and (ord(i.row) + 1 == pawn.row or ord(i.row) - 1 == pawn.row)\
                 and isnt_bolcked_pawn_for_start(pawn.side, pawn.row, pawn.colmn):
                i.can_en_passant = True
                class_of_pieces.last_move = True
                class_of_pieces.list_for_en_passant_row.append(pawn.row)
        return True
    elif pawn.side == "black" and pawn.c == 7 and mcolmn == 5 :
        return True
    else:
        return False
    

def it_can_en_passant(pawn, mrow, mcolmn):
    if pawn.can_en_passand:
        if pawn.side == "white" and mrow in class_of_pieces.list_for_en_passant_row\
              and pawn.colmn +1 == mcolmn and class_of_pieces.last_move :
            for i in chess_board.pawn_list_black :
                if i.row == mrow and i.colmn == mcolmn:
                    del i
            return True
        elif pawn.side == "black" and mrow in class_of_pieces.list_for_en_passant_row \
            and pawn.colmn - 1 == mcolmn and class_of_pieces.last_move :
            for i in chess_board.pawn_list_black :
                if i.row == mrow and i.colmn == mcolmn:
                    del i
            return True
        

def is_it_promotion(pawn):
    if pawn.side == "white":
        if pawn.colmn == 8:
            return True
    elif pawn.side == "black":
        if pawn == 1 :
            return True
    return False


def promotion_pawn(pawn):
        
        choice = input("")
        pieces_calss = {"q": queen, "r": rook,"b": bishop, "k":knight}.get(choice, queen)
        new_pieces = class_of_pieces.piece_class(pawn.side, pawn.row, pawn.colmn)
        del pawn
        if new_pieces.side == "white":
           chess_board.white_pieces.append(new_pieces)
        else:
            chess_board.black_pieces.append(new_pieces)
        

#for analyzing king  move


def is_king_checked_there(side, mrow, mcolmn):
    if side == "white":
        enemy_pieces = chess_board.black_pieces
    else:
        enemy_pieces = chess_board.white_pieces

    for enemy in enemy_pieces:
        if enemy.can_move_to(mrow, mcolmn):
            return True
    return False

nmkw = True
nmkb = True

def king_moved(side):
    if side == "white":
        nmkw = False
    else:
        nmkb = False

nmr1w = True
nmr1b = True
nmr2w = True
nmr2b = True
def rook_moved(side, name):
    if side == "white":
            if name == chess_board.k1w :
              nmr1w = False
            else:
                nmr2w = False
    else:
            if name == chess_board.k1b :
              nmr1w = False
            else:
                nmr2w = False


def can_castle(side, type_castle):
    if side == "white" and nmkw:
        if type_castle == "long" and nmr1w:
            for i in range(0,3):
                khone = [chr(100 - i), 1]
                for j in chess_board.white_pieces:
                    if j.row == khone[0] and j.colmn == khone[1]:
                        return False
                if is_king_checked_there(side, khone[0],khone[1]):
                    return False
            return True
        elif type_castle == "short" and nmr2w:
            for i in range(0,2):
                khone = [chr(102 + i), 1]
                for j in chess_board.white_pieces:
                    if j.row == khone[0] and j.colmn == khone[1]:
                        return False
                if is_king_checked_there(side, khone[0],khone[1]):
                    return False
            return True
    else:
        if type_castle == "long" and nmr1b:
            for i in range(0,3):
                khone = [chr(100 - i), 8]
                for j in chess_board.black_pieces:
                    if j.row == khone[0] and j.colmn == khone[1]:
                        return False
                if is_king_checked_there(side, khone[0],khone[1]):
                    return False
            return True
        elif type_castle == "short" and nmr2b:
            for i in range(0,2):
                khone = [chr(102 + i), 8]
                for j in chess_board.black_pieces:
                    if j.row == khone[0] and j.colmn == khone[1]:
                        return False
                if is_king_checked_there(side, khone[0],khone[1]):
                    return False
            return True
        

def castle(side, type_casel):
    if can_castle(side, type_casel):
        if side == "white":
            if type_casel == "long":
                chess_board.kb.moving("g1")
                chess_board.r2w.moving("f1")
                return True
            else:
                chess_board.kb.moving("c1")
                chess_board.r2w.moving("d1")
                return True
        else:
            if type_casel == "long":
                chess_board.kb.moving("g8")
                chess_board.r2w.moving("f8")
                return True
            else:
                chess_board.kb.moving("c8")
                chess_board.r2w.moving("d8")
                return True
    return False    


def safe_remove(LIST):
    if len(LIST) != 0 :
        LIST.remove()



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