import myfunction
import chess_board
import copy


class location():
    def __init__(self, row, colmn):
        self.row = row
        self.colmn = int(colmn)

    def info(self):
        return self.row, self.colmn
    

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
        super().__init__("pawn", side, row, colmn, shape)

    def moving(self, m):
        m = list(m)
        m[1] = int(m[1])
        temp1 = copy.deepcopy(self.row)
        temp2 = copy.deepcopy(self.colmn)
        if 1 <= m[1] <= 8 and (myfunction.isnt_bolcked_pawn(self.side, self.row, self.colmn)\
                                or myfunction.pawn_capchering(self, m[0], m[1]) \
                                    or myfunction.is_starting(self, m[0], m[1])\
                                        or myfunction.it_can_en_passant(self, m[0], m[1])):
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
                    return False
            if myfunction.is_it_promotion(self):
                myfunction.promotion_pawn(self)
            last_move =  False
            myfunction.safe_remove(list_for_en_passant_row)
            return True
        else:
            print("moving p")
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



    def can_move_to_isnt_king_check(self, mrow, mcolmn):
            king = chess_board.kw if self.side == "white" else chess_board.kb
            mcolmn = int(mcolmn)
    
            if self.side == "white":
                if self.colmn + 1 == mcolmn and self.row == mrow:
                    return myfunction.isnt_bolcked_pawn(self.side, self.row, self.colmn) and myfunction.is_king_checked_there(self.side, king.row, king.colmn)
                elif self.colmn == 2 and mcolmn == 4 and self.row == mrow:
                    return myfunction.isnt_bolcked_pawn_for_start(self.side, self.row, self.colmn) and myfunction.is_king_checked_there(self.side, king.row, king.colmn)
                elif self.colmn + 1 == mcolmn and abs(ord(self.row) - ord(mrow)) == 1:
                    for i in chess_board.black_pieces:
                        if i.row == mrow and i.colmn == mcolmn:
                            return True
            elif self.side == "black":
                if self.colmn - 1 == mcolmn and self.row == mrow:
                    return myfunction.isnt_bolcked_pawn(self.side, self.row, self.colmn) and myfunction.is_king_checked_there(self.side, king.row, king.colmn)
                elif self.colmn == 7 and mcolmn == 5 and self.row == mrow:
                    return myfunction.isnt_bolcked_pawn_for_start(self.side, self.row, self.colmn) and myfunction.is_king_checked_there(self.side, king.row, king.colmn)
                elif self.colmn - 1 == mcolmn and abs(ord(self.row) - ord(mrow)) == 1:
                    for i in chess_board.white_pieces:
                        if i.row == mrow and i.colmn == mcolmn:
                            return myfunction.is_king_checked_there(self.side, king.row, king.colmn)
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
        m[1] = int(m[1])
        temp_row = self.row
        temp_colmn = self.colmn
        if abs(ord(m[0]) - ord(self.row)) == abs(m[1] - self.colmn) and 97 <= ord(m[0]) <= 104 and 1 <= m[1] <= 8 \
            and myfunction.is_blocked_bishope(self.side, self.row, self.colmn, m[0], m[1]):
            target_pieces = chess_board.black_pieces if self.side == "white" else chess_board.white_pieces
            for i in target_pieces:
                if i.row == m[0] and i.colmn == m[1]:
                    del i
                    break
            self.row = m[0]
            self.colmn = m[1]
            king_row, king_colmn = (chess_board.kw.row, chess_board.kw.colmn) if self.side == "white" else (chess_board.kb.row, chess_board.kb.colmn)
            if myfunction.is_king_checked_there(self.side, king_row, king_colmn):
                self.row = temp_row
                self.colmn = temp_colmn
                return False
            myfunction.last_move = False
            myfunction.safe_remove(list_for_en_passant_row)
            return True
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
    

    def can_move_to_isnt_king_check(self, mrow, mcolmn):
        king = chess_board.kw if self.side == "white" else chess_board.kb
        if self.row == mrow:
            if self.side == "white":
                return myfunction.isnt_blocked_rook_white(self.row, self.colmn, mrow, mcolmn) and myfunction.is_king_checked_there(self.side, king.row, king.colmn)
            else:
                return myfunction.isnt_blocked_rook_black(self.row, self.colmn, mrow, mcolmn) and myfunction.is_king_checked_there(self.side, king.row, king.colmn)
        elif self.colmn == int(mcolmn):
            if self.side == "white":
                return myfunction.isnt_blocked_rook_white(self.row, self.colmn, mrow, mcolmn) and myfunction.is_king_checked_there(self.side, king.row, king.colmn)
            else:
                return myfunction.isnt_blocked_rook_black(self.row, self.colmn, mrow, mcolmn) and myfunction.is_king_checked_there(self.side, king.row, king.colmn)
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
                    myfunction.safe_remove(list_for_en_passant_row)
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
                    myfunction.safe_remove(list_for_en_passant_row)
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
                    myfunction.safe_remove(list_for_en_passant_row)
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
                    myfunction.safe_remove(list_for_en_passant_row)
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
    


    def can_move_to_isnt_king_check(self, mrow, mcolmn):
        king = chess_board.kw if self.side == "white" else chess_board.kb
        if self.row == mrow:
            if self.side == "white":
                return myfunction.isnt_blocked_rook_white(self.row, self.colmn, mrow, mcolmn) and myfunction.is_king_checked_there(self.side, king.row, king.colmn)
            else:
                return myfunction.isnt_blocked_rook_black(self.row, self.colmn, mrow, mcolmn) and myfunction.is_king_checked_there(self.side, king.row, king.colmn)
        elif self.colmn == int(mcolmn):
            if self.side == "white":
                return myfunction.isnt_blocked_rook_white(self.row, self.colmn, mrow, mcolmn) and myfunction.is_king_checked_there(self.side, king.row, king.colmn)
            else:
                return myfunction.isnt_blocked_rook_black(self.row, self.colmn, mrow, mcolmn) and myfunction.is_king_checked_there(self.side, king.row, king.colmn)
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
                myfunction.safe_remove(list_for_en_passant_row)
                return True
            elif self.side == "white" and myfunction.isnt_blocked_rook_white(self.row, self.colmn, m[0], m[1]):
                for i in chess_board.black_pieces:
                    if i.row == m[0] and i.colmn == m[1]:
                        del i
                self.row = m[0]
                self.colmn = int(m[1])
                last_move = False
                myfunction.safe_remove(list_for_en_passant_row)
                return True
    
        else:
            return False
        
    def can_move_to(self, mrow, mcolmn):
        mcolmn = int(mcolmn)
        if abs(ord(mrow) - ord(self.row)) <= 1 and abs(mcolmn - self.colmn) <= 1:
            return myfunction.is_blocked_bishope(self.side, self.row, self.colmn, mrow, mcolmn)
        return False



    def can_move_to_isnt_king_check(self, mrow, mcolmn):
            mcolmn = int(mcolmn)
            if abs(ord(mrow) - ord(self.row)) <= 1 and abs(mcolmn - self.colmn) <= 1:
                king = chess_board.kw if self.side == "white" else chess_board.kb
                return myfunction.is_blocked_bishope(self.side, self.row, self.colmn, mrow, mcolmn) and myfunction.is_king_checked_there(self.side, king.row, king.colmn)
            return False






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
        m[1] = int(m[1])
        temp_row = self.row
        temp_colmn = self.colmn
        is_rook_valid = (self.row == m[0] or self.colmn == m[1]) and (myfunction.isnt_blocked_rook_white(self.row, self.colmn, m[0], m[1]) if self.side == "white" else myfunction.isnt_blocked_rook_black(self.row, self.colmn, m[0], m[1]))
        is_bishop_valid = abs(ord(m[0]) - ord(self.row)) == abs(m[1] - self.colmn) and myfunction.is_blocked_bishope(self.side, self.row, self.colmn, m[0], m[1])
        if (is_rook_valid or is_bishop_valid) and 97 <= ord(m[0]) <= 104 and 1 <= m[1] <= 8:
            target_pieces = chess_board.black_pieces if self.side == "white" else chess_board.white_pieces
            for i in target_pieces:
                if i.row == m[0] and i.colmn == m[1]:
                    del i
                    break
            self.row = m[0]
            self.colmn = m[1]
            king_row, king_colmn = (chess_board.kw.row, chess_board.kw.colmn) if self.side == "white" else (chess_board.kb.row, chess_board.kb.colmn)
            if myfunction.is_king_checked_there(self.side, king_row, king_colmn):
                self.row = temp_row
                self.colmn = temp_colmn
                return False
            myfunction.last_move = False
            myfunction.safe_remove(list_for_en_passant_row)
            return True
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
    

    def can_move_to_isnt_king_check(self, mrow, mcolmn):
        mcolmn = int(mcolmn)
        if self.row == mrow or self.colmn == mcolmn:
            if self.side == "white":
                return myfunction.isnt_blocked_rook_white(self.row, self.colmn, mrow, mcolmn) and myfunction.is_king_checked_there(self.side, chess_board.kw.row, chess_board.kw.colmn)
            else:
                return myfunction.isnt_blocked_rook_black(self.row, self.colmn, mrow, mcolmn) and myfunction.is_king_checked_there(self.side, chess_board.kw.row, chess_board.kw.colmn)
        elif abs(ord(mrow) - ord(self.row)) == abs(mcolmn - self.colmn):
            king = chess_board.kw if self.side == "white" else chess_board.kb
            return myfunction.is_blocked_bishope(self.side, self.row, self.colmn, mrow, mcolmn) and myfunction.is_king_checked_there(self.side, king.row, king.colmn)
        return False
    

    def __del__(self):
            print(f"your {self.name} is capthered")


class knight(piece):
    def __init__(self, side, row, colmn, shape=None):
        if shape is None:
            shape = "\u265E" if side == "white" else "\u2658"
        super().__init__("knight", side, row, colmn, shape)

    def moving(self, m):
        m = list(m)
        m[1] = int(m[1])
        temp_row = self.row
        temp_colmn = self.colmn
        deltas = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
        dx = abs(ord(m[0]) - ord(self.row))
        dy = abs(m[1] - self.colmn)
        if (dx, dy) not in [(1, 2), (2, 1)] or not (97 <= ord(m[0]) <= 104 and 1 <= m[1] <= 8):
            return False
        target_pieces = chess_board.black_pieces if self.side == "white" else chess_board.white_pieces
        own_pieces = chess_board.white_pieces if self.side == "white" else chess_board.black_pieces
        for p in own_pieces:
            if p.row == m[0] and p.colmn == m[1]:
                return False  
        for p in target_pieces:
            if p.row == m[0] and p.colmn == m[1]:
                del p
                break
        self.row = m[0]
        self.colmn = m[1]
        king_row, king_colmn = (chess_board.kw.row, chess_board.kw.colmn) if self.side == "white" else (chess_board.kb.row, chess_board.kb.colmn)
        if myfunction.is_king_checked_there(self.side, king_row, king_colmn):
            self.row = temp_row
            self.colmn = temp_colmn
            return False
        myfunction.last_move = False
        myfunction.safe_remove(list_for_en_passant_row)
        return True

    def can_move_to(self, mrow, mcolmn):
        mcolmn = int(mcolmn)
        dx = abs(ord(mrow) - ord(self.row))
        dy = abs(mcolmn - self.colmn)
        return (dx, dy) in [(1, 2), (2, 1)]
    

    def can_move_to_isnt_king_check(self, mrow, mcolmn):
        mcolmn = int(mcolmn)
        dx = abs(ord(mrow) - ord(self.row))
        dy = abs(mcolmn - self.colmn)
        king = chess_board.kw if self.side == "white" else chess_board.kb
        return (dx, dy) in [(1, 2), (2, 1)] and myfunction.is_king_checked_there(self.side, king.row, king.colmn)


    def __del__(self):
            print(f"your {self.name} is capthered")



boerd = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8',
 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8',
 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8',
 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8',
 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8',
 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']