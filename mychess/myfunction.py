import chess_beord
import class_of_pieses
import copy

#for analyzing rook move


def isnt_blocked_rook_white(r, c, mr, mc):
    end_add_colmn = c
    end_mines_colmn = c
    found = False
    for i in range(1, c):
        for j in chess_beord.white_pieces:
            if i == j.colmn and j.row == r:
                end_mines_colmn = i + 1
                found = False
                break
        for j in chess_beord.black_pieces:
            if i == j.colmn and j.row == r :
                end_mines_colmn = i 
                found = True
                break
        if found:
            break
    found = False
    for i in range(c+1, 9):
        for j in chess_beord.white_pieces:
            if i == j.colmn and j.row == r:
                end_add_colmn = i -1
                found = True
                break
        for j in chess_beord.black_pieces:
            if i == j.colmn and j.row == r:
                end_add_colmn = i
                found = True
                break
        if found:
            break
    end_add_row = ord(r)
    end_mines_row = ord(r)
    for i in range(97, ord(r)):
        for j in chess_beord.white_pieces:
            if i == ord(j.row) and j.colmn == c:
                end_mines_row = i + 1
                found = False
                break
        for j in chess_beord.black_pieces:
            if i == ord(j.row) and j.colmn == c:
                end_mines_row = i
                found = False
                break
        if found:
            break
    found = False
    for i in range(ord(r) + 1, 105):
        for j in chess_beord.white_pieces:
            if i == ord(j.row) and j.ccolmn == c:
                end_add_row = i - 1
                found = True

        for j in chess_beord.black_pieces:
            if i == ord(j.r) and j.c == c:
                end_add_row = i
                found = True
                break
        if found:
            break
        move_row = []
    for i in range(end_mines_row, end_add_row):
        move_row.append(i)
    move_colmn = []
    for i in range(end_mines_colmn, end_add_colmn):
        move_colmn.append(i)
    for i in move_colmn:
        if mc == i:
            return True
            break
    for i in move_row:
        if ord(mr) == i:
            return True
            break
    return False


def isnt_blocked_rook_black(r, c, mr, mc):
    end_add_colmn = c
    end_mines_colmn = c
    fond = False
    for i in range(1, c):
        for j in chess_beord.black_pieces:
            if i == j.c and j.r == r:
                end_mines_colmn = i + 1
                found = False
                break
        for j in chess_beord.white_pieces:
            if i == j.c and j.r == r:
                end_mines_colmn = i
                found = False
                break
        if fond:
            break
    found = False
    for i in range(c+1, 9):
        for j in chess_beord.black_pieces:
            if i == j.c and j.r == r:
                end_add_colmn = i - 1
                found = True
                break
        for j in chess_beord.white_pieces:
            if i == j.c and j.r == r:
                end_add_colmn = i
                found = True
                break
        if found:
            break
    end_add_row = ord(r)
    end_mines_row = ord(r)
    for i in range(97, ord(r)):
        for j in chess_beord.black_pieces:
            if i == ord(j.r) and j.c == c:
                end_mines_row = i + 1
                fond = False
                break
        for j in chess_beord.white_pieces:
            if i == ord(j.r) and j.c == c:
                end_mines_row = i
                fond = False
                break
        if fond:
            break
    fond = False
    for i in range(ord(r) + 1, 105):
        for j in chess_beord.black_pieces:
            if i == ord(j.r) and j.c == c:
                end_add_row = i - 1
                fond = True
                break
        for j in chess_beord.white_pieces:
            if i == ord(j.r) and j.c == c:
                end_add_row = i
                fond = True
                break
        if fond:
            break
    move_row = []
    for i in range(end_mines_row, end_add_row):
        move_row.append(i)
    move_colmn = []
    for i in range(end_mines_colmn, end_add_colmn):
        move_colmn.append(i)
    for i in move_colmn:
        if mc == i:
            return True
            break
    for i in move_row:
        if ord(mr) == i:
            return True
            break
    return False


#for analyzing bishope move


def is_blocked_bishope(side, r, c, mr, mc):
    if side == "white":
        my_move = []
        khone = class_of_pieses.location(r, c)
        for i in range(1, 9):
            khone.row = chr(ord(khone.row) + i)
            khone.colmn = khone.colmn + i
            found = False
            for j in chess_beord.white_pieces:
                if j.row == khone.row and j.colmn == khone.colmn:
                    found = True
                    break
            if found:
                break
            for j in chess_beord.black_pieces:
                if j.row == khone.row and j.colmn == khone.colmn:
                    my_move.append(khone)
                    found = True
                    break
            if found:
                break
            my_move.append(khone)
        for i in range(1, 9):
            khone.row = chr(ord(khone.row) - i)
            khone.colmn = khone.colmn - i
            found = False
            for j in chess_beord.white_pieces:
                if j.row == khone.row and j.colmn == khone.colmn:
                    found = True
                    break
            for j in chess_beord.black_pieces:
                if j.row == khone.row and j.colmn == khone.colmn:
                    my_move.append(khone)
                    found = True
                    break
            if found:
                break
            my_move.append(khone)
        for i in range(1, 9):
            khone.row = chr(ord(khone.row) - i)
            khone.colmn = khone.colmn + i
            found = False
            for j in chess_beord.white_pieces:
                if j.row == khone.row and j.colmn == khone.colmn:
                    found = True
                    break
            for j in chess_beord.black_pieces:
                if j.row == khone.row and j.colmn == khone.colmn:
                    my_move.append(khone)
                    found = True
                    break
            if found:
                break
            my_move.append(khone)
        for i in range(1, 9):
            khone.row = chr(ord(khone.row) + i)
            khone.colmn = khone.colmn - i
            found = False
            for j in chess_beord.white_pieces:
                if j.row == khone.row and j.colmn == khone.colmn:
                    found = True
                    break
            for j in chess_beord.black_pieces:
                if j.row == khone.row and j.colmn == khone.colmn:
                    my_move.append(khone)
                    found = True
                    break
            if found:
                break
            my_move.append(khone)
        for i in my_move:
            if i.row == mr and i.colmn == mc:
                return True
        return False
    else:
        my_move = []
        khone = class_of_pieses.location(r, c)
        for i in range(1, 9):
            khone.row = chr(ord(khone.row) + i)
            khone.colmn = khone.colmn + i
            found = False
            for j in chess_beord.black_pieces:
                if j.row == khone.row and j.colmn == khone.colmn:
                    found = True
                    break
            for j in chess_beord.white_pieces:
                if j.row == khone.row and j.colmn == khone.colmn:
                    my_move.append(khone)
                    found = True
                    break
            if found:
                break
            my_move.append(khone)
        for i in range(1, 9):
            khone.row = chr(ord(khone.row) - i)
            khone.colmn = khone.colmn - i
            found = False
            for j in chess_beord.black_pieces:
                if j.row == khone.row and j.colmn == khone.colmn:
                    found = True
                    break
            for j in chess_beord.white_pieces:
                if j.row == khone.row and j.colmn == khone.colmn:
                    my_move.append(khone)
                    found = True
                    break
            if found:
                break
            my_move.append(khone)
        for i in range(1, 9):
            khone.row = chr(ord(khone.row) - i)
            khone.colmn = khone.colmn + i
            found = False
            for j in chess_beord.black_pieces:
                if j.row == khone.row and j.colmn == khone.colmn:
                    found = True
                    break
            for j in chess_beord.white_pieces:
                if j.row == khone.row and j.colmn == khone.colmn:
                    my_move.append(khone)
                    found = True
                    break
            if found:
                break
            my_move.append(khone)
        for i in range(1, 9):
            khone.row = chr(ord(khone.row) + i)
            khone.colmn = khone.colmn - i
            found = False
            for j in chess_beord.black_pieces:
                if j.row == khone.row and j.colmn == khone.colmn:
                    found = True
                    break
            for j in chess_beord.white_pieces:
                if j.row == khone.row and j.colmn == khone.colmn:
                    my_move.append(khone)
                    found = True
                    break
            if found:
                break
            my_move.append(khone)
        for i in my_move:
            if i.row == mr and i.colmn == mc:
                return True
        return False


def isnt_bolcked_pawn(side, r, c):
    if side == "white":
        loc = class_of_pieses.location(r, c+1)
    else:
        loc = class_of_pieses.location(r , c-1)
    for i, j in chess_beord.white_pieces, chess_beord.black_pieces:
        if (loc.row == i.row and loc.colmn == i.colmn) \
                or (loc.row == j.row and loc.colmn == j.colmn):
            return False
    return True

def isnt_bolcked_pawn_for_start(side, r, c):
    for k in range(1,3):
        if side == "white":
            loc = class_of_pieses.location(r, c+k)
        else:
            loc = class_of_pieses.location(r , c-k)
        for i, j in chess_beord.white_pieces, chess_beord.black_pieces:
            if (loc.row == i.row and loc.colmn == i.colmn) \
                    or (loc.row == j.row and loc.colmn == j.colmn):
                return False
    return True


#for analyzing pawn move


def pawn_capchering(pawn, mrow, mcolmn):
    if  ord(pawn.row) + 1 == ord(mrow) or ord(pawn.row) - 1 == ord(mrow):
        if pawn.side == "white" and pawn.colmn + 1 == mcolmn:
            for i in chess_beord.black_pieces:
                if i.row == mrow and i.colmn == mcolmn:
                    del i
                    return True
        elif pawn.side == " black" and pawn.colmn - 1 == mcolmn:
            for i in chess_beord.white_pieces :
                if i.row == mrow and i.colmn == mcolmn:
                    del i 
                    return True
    return False


def is_starting(pawn, mcolmn):
    if pawn.side == "white" and pawn.c == 2 and mcolmn == 4 :
        for i in chess_beord.pawn_list_black:
            if i.colmn == 4 and (ord(i.row) + 1 == pawn.row or ord(i.row) - 1 == pawn.row)\
                 and isnt_bolcked_pawn_for_start(pawn.side, pawn.row, pawn.colmn):
                i.can_en_passant = True
                class_of_pieses.last_move = True
                class_of_pieses.list_for_en_passant_row.append(pawn.row)
        return True
    elif pawn.side == "black" and pawn.c == 7 and mcolmn == 5 :
        return True
    else:
        return False
    

def it_can_en_passant(pawn, mrow, mcolmn):
    if pawn.can_en_passand:
        if pawn.side == "white" and mrow in class_of_pieses.list_for_en_passant_row\
              and pawn.c +1 == mcolmn and class_of_pieses.last_move :
            for i in chess_beord.pawn_list_black :
                if i.row == mrow and i.colmn == mcolmn:
                    del i
            return True
        elif pawn.side == "black" and mrow in class_of_pieses.list_for_en_passant_row \
            and pawn.colmn - 1 == mcolmn and class_of_pieses.last_move :
            for i in chess_beord.pawn_list_black :
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
        new_pieces = class_of_pieses.piece_class(pawn.side, pawn.row, pawn.colmn)
        del pawn
        if new_pieces.side == "white":
           chess_beord.white_pieces.append(new_pieces)
        else:
            chess_beord.black_pieces.append(new_pieces)
        

#for analyzing king  move


def is_king_checked_there(side, mrow, mcolmn):
    if side == "white":
        enemy_pieces = chess_beord.black_pieces
    else:
        enemy_pieces = chess_beord.white_pieces

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
            if name == chess_beord.k1w :
              nmr1w = False
            else:
                nmr2w = False
    else:
            if name == chess_beord.k1b :
              nmr1w = False
            else:
                nmr2w = False


def can_casel(side, type_casel):
    if side == "white" and nmkw:
        if type_casel == "long" and nmr1w:
            for i in range(0,3):
                khone = [chr(100 - i), 1]
                for j in chess_beord.white_pieces:
                    if j.row == khone[0] and j.colmn == khone[1]:
                        return False
                if is_king_checked_there(side, khone[0],khone[1]):
                    return False
            return True
        elif type_casel == "short" and nmr2w:
            for i in range(0,2):
                khone = [chr(102 + i), 1]
                for j in chess_beord.white_pieces:
                    if j.row == khone[0] and j.colmn == khone[1]:
                        return False
                if is_king_checked_there(side, khone[0],khone[1]):
                    return False
            return True
    else:
        if type_casel == "long" and nmr1b:
            for i in range(0,3):
                khone = [chr(100 - i), 8]
                for j in chess_beord.black_pieces:
                    if j.row == khone[0] and j.colmn == khone[1]:
                        return False
                if is_king_checked_there(side, khone[0],khone[1]):
                    return False
            return True
        elif type_casel == "short" and nmr2b:
            for i in range(0,2):
                khone = [chr(102 + i), 8]
                for j in chess_beord.black_pieces:
                    if j.row == khone[0] and j.colmn == khone[1]:
                        return False
                if is_king_checked_there(side, khone[0],khone[1]):
                    return False
            return True
        

def casel(side, type_casel):
    if can_casel(side, type_casel):
        if side == "white":
            if type_casel == "long":
                chess_beord.kb.moving("g1")
                chess_beord.r2w.moving("f1")
                return True
            else:
                chess_beord.kb.moving("c1")
                chess_beord.r2w.moving("d1")
                return True
        else:
            if type_casel == "long":
                chess_beord.kb.moving("g8")
                chess_beord.r2w.moving("f8")
                return True
            else:
                chess_beord.kb.moving("c8")
                chess_beord.r2w.moving("d8")
                return True
    return False    
        