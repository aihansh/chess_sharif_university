import chess_beord


class player():
    def __init__(self, side):
        self.side = side

    def move(self):
        pass

class white(player):
    def __init__(self, name, side = None):
        self.name = name
        if side == None:
            side = "white"
            self.side = side
        player.__init__(self, self.side)




class black(player):
    def __init__(self, name, side = None):
        self.name = name
        if side == None:
           side = "black"
           self.side = side
        player.__init__(self, self.side)



def chanse(player1, player2):
    from random import randint
    coin = randint(0,1)
    if coin == 0 :
        player1 = white("player1")
        player2 = black("player2")
    else:
        plater1 = black("player1")
        player2 = white("player2")
    return plater1, player2
