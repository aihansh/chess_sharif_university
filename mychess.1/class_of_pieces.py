import myfunction
import chess_board
import copy


class location():
    def __init__(self, row, colmn):
        self.row = row
        self.column = int(colmn)

    def info(self):
        return self.row, self.column
    

class piece():

    def __init__(self,  name, side, row, colmn, shape):
        self.row = row
        self.colmn = int(colmn)
        self.side = side
        self.name = name
        self.shape = shape


last_move = False
list_for_en_passant_row = []


class pawn(piece):

    def __init__(self, side, row, colmn, shape = None):
        self.can_en_passant = False
        if shape ==  None:
            if side == "white" :
                shape = "\u265F"
                self.shape = shape
            else:
                shape = "\u2659"
                self.shape = shape
        super().__init__("pawn", side, row, colmn, self.shape)

    def moving(self, m):
        m = list(m)
        m[1] = int(m[1])
        temp1 = copy.deepcopy(self.row)
        temp2 = copy.deepcopy(self.colmn)
        if 1 <= m[1] <= 8 and (myfunction.isnt_balcked_pawn(self.side, self.row, self.colmn)\
                                or myfunction.pawn_capchering(self, m[0], m[1]) \
                                    or myfunction.is_starting(self, m[0], m[1])\
                                        or myfunction.it_can_en_passnt(self, m[0], m[1])):
            self.colmn = m[1]
            self.row = m[0]
            if self.side == "white":
                if myfunction.is_king_checked_there(self.side, chess_board.kw.row, chess_board.kw.colmn):
                    self.colmn = temp1
                    self.row = temp2
                    return False
            else:
                if myfunction.is_king_checked_there(self.side, chess_board.kb.row, chess_board.kb.colmn):
                    self.colmn = temp1
                    self.row = temp2
                    return True

            if myfunction.is_it_promotion(self):
                myfunction.promotion_pawn(self)
            last_move =  False
            list_for_en_passant_row.remove()
            return True
        else:
            return False
    

    def can_move_to(self, mrow, mcolmn):
        mcolmn = int(mcolmn)
 
        if self.side == "white":
            if self.colmn + 1 == mcolmn and self.row == mrow:
                return myfunction.isnt_bolcked_pawn(self.side, self.row, self.colmn)
            elif self.colmn == 2 and mcolmn == 4 and self.row == mrow:
                return myfunction.isnt_bolcked_pawn_for_start(self.side, self.row, self.colmn)
            elif self.colmn + 1 == mcolmn and abs(ord(self.row) - ord(mrow)) == 1:
                for i in chess_board.black_pieces:
                    if i.row == mrow and i.colmn == mcolmn:
                        return True
        elif self.side == "black":
            if self.colmn - 1 == mcolmn and self.row == mrow:
                return myfunction.isnt_bolcked_pawn(self.side, self.row, self.colmn)
            elif self.colmn == 7 and mcolmn == 5 and self.row == mrow:
                return myfunction.isnt_bolcked_pawn_for_start(self.side, self.row, self.colmn)
            elif self.colmn - 1 == mcolmn and abs(ord(self.row) - ord(mrow)) == 1:
                for i in chess_board.white_pieces:
                    if i.row == mrow and i.colmn == mcolmn:
                        return True
        return False


    def __del__(self):
            print(f"your {self.name} is capthered")


class bishop(piece):

    def __init__(self, side, row, colmn, shape = None):
        if shape is None:
            if side == "white":
                shape = "\u265D"
                self.shape = shape
            else:
                shape = "\u2657"
                self.shape = shape
         
        super().__init__("bishop", side, row, colmn, self.shape)

    def moving(self, m):
        m = list(m)
        temp1 = copy.deepcopy(self.colmn)
        temp2 = copy.deepcopy(self.row)
        if ord(m[0]) - ord(self.row) == int(m[2]) - self.colmn\
            and 97 <= ord(m[0]) <= 104 and 0 <= int(m[1]) <= 8\
                and myfunction.is_blocked_bishope(self.side, self.row, self.colmn, m[0], m[1]):
            if self.side == "white":
                for i in chess_board.black_pieces:
                    if i.row == m[0] and i.colmn == m[1]:
                         del i
            else:
                for i in chess_board.white_pieces:
                    if i.row == m[0] and i.colmn == m[1]:
                         del i
            self.row = m[0]
            self.colmn = int(m[1])
            if self.side == "white":
                if myfunction.is_king_checked_there(self.side, chess_board.kw.row, chess_board.kw.colmn):
                    self.colmn = temp1
                    self.row = temp2
                    return False
            else:
                if myfunction.is_king_checked_there(self.side, chess_board.kb.row, chess_board.kb.colmn):
                    self.colmn = temp1
                    self.row = temp2
                    return True
            last_move = False
            list_for_en_passant_row.remove()
            return True
        else:
            return False



    def can_move_to(self, mrow, mcolmn):
        if self.row == mrow:
            if self.side == "white":
                return myfunction.isnt_blocked_rook_white(self.row, self.colmn, mrow, mcolmn)
            else:
                return myfunction.isnt_blocked_rook_black(self.row, self.colmn, mrow, mcolmn)
        elif self.colmn == int(mcolmn):
            if self.side == "white":
                return myfunction.isnt_blocked_rook_white(self.row, self.colmn, mrow, mcolmn)
            else:
                return myfunction.isnt_blocked_rook_black(self.row, self.colmn, mrow, mcolmn)
        return False

    

    def __del__(self):
            print(f"your {self.name} is capthered")


class rook(piece):
    def __init__(self, side, row, colmn, shape = None):
        if shape == None:
            if side == "white":
                shape = "\u265C"
                self.shape = shape
            else:
                shape = "\u2656"
                self.shape = shape
        super().__init__("rook", side, row, colmn, shape)

    def moving(self, m):
        m = list(m)
        temp1 = copy.deepcopy(self.colmn)
        temp2 = copy.deepcopy(self.row)
        if self.r == m[0] and 0 <= int(m[1]) <= 8:
            if self.side == "white":
                if myfunction.isnt_blocked_rook_white(self.row, self.colmn, m[0], m[1]):
                    for i in chess_board.black_pieces:
                        if i.row == m[0] and i.colmn == m[1]:
                            del i
                    self.colmn = int(m[1])
                    if myfunction.is_king_checked_there(self.side, chess_board.kw.row, chess_board.kw.colmn):
                        self.colmn = temp1
                        return False
                    last_move = False
                    list_for_en_passant_row.remove()
                    return True
            else:
                if myfunction.isnt_blocked_rook_black(self.row, self.colmn, m[0], m[1]):
                    for i in chess_board.white_pieces:
                        if i.row == m[0] and i.colmn == m[1]:
                            del i
                    self.colmn = int(m[1])
                    if myfunction.is_king_checked_there(self.side, chess_board.kb.row, chess_board.kb.colmn):
                        self.colmn = temp1
                        return False
                    last_move = False
                    list_for_en_passant_row.remove()
                    return True
        elif self.colmn == int(m[1]) and 97 <= ord(m[0]) <= 104:
            if self.side == "white":
                if myfunction.isnt_blocked_rook_white(self.row, self.colmn, m[0], m[1]):
                    for i in chess_board.black_pieces:
                        if i.row == m[0] and i.colmn == m[1]:
                            del i
                    self.row = m[0]
                    if myfunction.is_king_checked_there(self.side, chess_board.kw.row, chess_board.kw.colmn):
                        self.row = temp2
                        return False
                    last_move = False
                    list_for_en_passant_row.remove()
                    return True
            else:
                if myfunction.isnt_blocked_rook_black:
                    for i in chess_board.white_pieces:
                        if i.row == m[0] and i.colmn == m[1]:
                            del i
                    self.row = m[0]
                    if myfunction.is_king_checked_there(self.side, chess_board.kb.row, chess_board.kb.colmn):
                        self.row = temp2
                        return True
                    last_move = False
                    list_for_en_passant_row.remove()
                    return True
        else:
            return False
        

    def can_move_to(self, mrow, mcolmn):
        if self.row == mrow:
            if self.side == "white":
                return myfunction.isnt_blocked_rook_white(self.row, self.colmn, mrow, mcolmn)
            else:
                return myfunction.isnt_blocked_rook_black(self.row, self.colmn, mrow, mcolmn)
        elif self.colmn == int(mcolmn):
            if self.side == "white":
                return myfunction.isnt_blocked_rook_white(self.row, self.colmn, mrow, mcolmn)
            else:
                return myfunction.isnt_blocked_rook_black(self.row, self.colmn, mrow, mcolmn)
        return False


    def __del__(self):
            print(f"your {self.name} is capthered")


class king(piece):
    def __init__(self, side, row, colmn, shape = None):
        if shape == None:
            if side == "white":
                shape = "\u265A"
                self.shape = shape
            else:
                shape = "\u2654"
                self.shape = shape
        super().__init__("king", side, row, colmn, shape)

    def moving(self, m):
        m = list(m)
        if 0 <= self.colmn - 1 <= int(m[1]) <= self.colmn + 1 <= 8 and \
            97 <= ord(self.row) - 1 <= ord(m[0]) <= ord(self.row) + 1 <= 104 \
                and myfunction.is_blocked_bishope(self.side, self.row, self.colmn, m[0], m[1])\
                      and not(myfunction.is_king_checked_there(self.side, m[0], m[1])): 
            if self.side == "black" and myfunction.isnt_blocked_rook_black(self.row, self.colmn, m[0], m[1]):
                for i in chess_board.white_pieces:
                    if i.row == m[0] and i.colmn == m[1]:
                        del i
                self.row = m[0]
                self.colmn = int(m[1])
                last_move = False
                list_for_en_passant_row.remove()
                return True
            elif self.side == "white" and myfunction.isnt_blocked_rook_white(self.row, self.colmn, m[0], m[1]):
                for i in chess_board.black_pieces:
                    if i.row == m[0] and i.colmn == m[1]:
                        del i
                self.row = m[0]
                self.colmn = int(m[1])
                last_move = False
                list_for_en_passant_row.remove()
                return True
    
        else:
            return False
        
    def can_move_to(self, mrow, mcolmn):
        mcolmn = int(mcolmn)
        if abs(ord(mrow) - ord(self.row)) <= 1 and abs(mcolmn - self.colmn) <= 1:
            return myfunction.is_blocked_bishope(self.side, self.row, self.colmn, mrow, mcolmn)
        return False




    def __del__(self):
            print(f"your {self.name} is capthered")


class queen(piece):
    def __init__(self, side, row, colmn, shape = None):
        if shape == None:
            if side == "white":
                shape = "\u265B"
                self.shape = shape
            else:
                shape = "\u2655"
                self.shape = shape
        super().__init__("queen", side, row, colmn, shape)

    def moving(self, m):
        m = list(m)
        temp1 = copy.deepcopy(self.colmn)
        temp2 = copy.deepcopy(self.row)
        if 0 <= int(m[1]) <= 8 and 97 <= ord(m[0]) <= 104 and\
                myfunction.is_blocked_bishope(self.side, self.row, self.colmn, m[0], m[1]):
            if self.side == "black" and\
                   myfunction. isnt_blocked_rook_black(self.row, self.colmn, m[0], m[1]):
                for i in chess_board.white_pieces:
                    if i.row == m[0] and i.colmn == m[1]:
                        del i
                self.row = m[0]
                self.colmn = int(m[1])
                if myfunction.is_king_checked_there(self.side, chess_board.kb.row, chess_board.kb.colmn):
                    self.colmn = temp1
                    self.row = temp2
                    return False
                last_move = False
                list_for_en_passant_row.remove()
                return True
            elif self.side == "white" and\
                    myfunction.isnt_blocked_rook_black(self.row, self.colmn, m[0], m[1]):
                for i in chess_board.black_pieces:
                    if i.row == m[0] and i.colmn == m[1]:
                        del i
                self.row = m[0]
                self.colmn = int(m[1])
                if myfunction.is_king_checked_there(self.side, chess_board.kw.row, chess_board.kw.colmn):
                    self.colmn = temp1
                    self.row = temp2
                    return True
                last_move = False
                list_for_en_passant_row.remove()
                return True
        else:
            return False
    def can_move_to(self, mrow, mcolmn):
        mcolmn = int(mcolmn)
        if self.row == mrow or self.colmn == mcolmn:
            if self.side == "white":
                return myfunction.isnt_blocked_rook_white(self.row, self.colmn, mrow, mcolmn)
            else:
                return myfunction.isnt_blocked_rook_black(self.row, self.colmn, mrow, mcolmn)
        elif abs(ord(mrow) - ord(self.row)) == abs(mcolmn - self.colmn):
            return myfunction.is_blocked_bishope(self.side, self.row, self.colmn, mrow, mcolmn)
        return False


    def __del__(self):
            print(f"your {self.name} is capthered")


class knight(piece):
    def __init__(self, side, row, colmn, shape = None):
        if shape == None:
            if side == "white":
                shape = "\u265E"
                self.shape = shape
            else:
                shape = "\u2658"
                self.shape = shape
        super().__init__(side, "knight", row, colmn, shape)

    def moving(self, m):
        m = list(m)
        m[1] = int(m[1])
        temp1 = copy.deepcopy(self.colmn)
        temp2 = copy.deepcopy(self.row)
        row_of_knight = ord(self.row)
        move_knight = []
        move_knight.append([row_of_knight + 1, self.colmn + 2])
        move_knight.append([row_of_knight + 1, self.colmn - 2])
        move_knight.append([row_of_knight - 1, self.colmn + 2])
        move_knight.append([row_of_knight - 1, self.colmn - 2])
        move_knight.append([row_of_knight + 2, self.colmn + 1])
        move_knight.append([row_of_knight - 2, self.colmn + 1])
        move_knight.append([row_of_knight + 2, self.colmn - 1])
        move_knight.append([row_of_knight - 2, self.colmn - 1])
        if 0 <= m[1] <= 8 and 97 <= ord(m[0]) <= 104 and\
                [ord(m[0]), m[1]] in move_knight:
            if self.side == "white":
                for j in chess_board.white_pieces:
                    if i.row == m[0] and i.colmn == m[1] :
                        for i in chess_board.black_pieces:
                            if i.row == m[0] and i.colmn == m[1]:
                              del i
                        self.row = m[0]
                        self.colmn = m[1]
                        if myfunction.is_king_checked_there(self.side, chess_board.kw.row, chess_board.kw.colmn):
                            self.colmn = temp1
                            self.row = temp2
                            return False
                        last_move = False
                        list_for_en_passant_row.remove()
                        return True
            elif self.side == "black":
                for j in chess_board.black_pieces:
                    if i.row == m[0] and i.colmn == m[1] :
                        for i in chess_board.white_pieces:
                            if i.row == m[0] and i.colmn == m[1]:
                              del i
                        self.row = m[0]
                        self.colmn = m[1]
                        if myfunction.is_king_checked_there(self.side, chess_board.kb.row, chess_board.kb.colmn):
                                self.colmn = temp1
                                self.row = temp2
                                return False
                        last_move = False
                        list_for_en_passant_row.remove()
                        return True
            else:
                return False
        else:
            return False
        del move_knight


    def can_move_to(self, mrow, mcolmn):
        mcolmn = int(mcolmn)
        dx = abs(ord(mrow) - ord(self.row))
        dy = abs(mcolmn - self.colmn)
        return (dx, dy) in [(1, 2), (2, 1)]


    def __del__(self):
            print(f"your {self.name} is capthered")