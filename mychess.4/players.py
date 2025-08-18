import chess_board


class player():
    def __init__(self, side):
        self.side = side
    def move(self):
        pass

class white(player):
    def __init__(self, name, situation = None, side = None ):
        self.situation = situation
        self.name = name
        if side == None:
            side = "white"
            self.side = side
        player.__init__(self, self.side)




class black(player):
    def __init__(self, name, situation = None, side = None):
        self.situation = situation
        self.name = name
        if side == None:
           side = "black"
           self.side = side
        player.__init__(self, self.side)

