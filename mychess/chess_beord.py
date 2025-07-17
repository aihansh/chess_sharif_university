import class_of_pieses
import myfunction


p1w = class_of_pieses.pawn("white", "a", 2)
p2w = class_of_pieses.pawn("white", "b", 2)
p3w = class_of_pieses.pawn("white", "c", 2)
p4w = class_of_pieses.pawn("white", "d", 2)
p5w = class_of_pieses.pawn("white", "e", 2)
p6w = class_of_pieses.pawn("white", "f", 2)
p7w = class_of_pieses.pawn("white", "g", 2)
p8w = class_of_pieses.pawn("white", "h", 2)
k1w = class_of_pieses.knight("white", "b", 1)
k2w = class_of_pieses.knight("white", "g", 1)
b1w = class_of_pieses.bishop("white", "c", 1)
b2w = class_of_pieses.bishop("white", "f", 1)
r1w = class_of_pieses.rook("white", "a", 1)
r2w = class_of_pieses.rook("white", "h", 1)
kw = class_of_pieses.king("white", "d", 1)
qw = class_of_pieses.queen("white", "e", 1)
white_pieces = [p1w, p2w, p3w, p4w, p5w, p6w, p7w, p8w,\
                k1w, k2w, b1w, b2w, r1w, r2w, kw, qw]
pawn_list_white = [p1w, p2w, p3w, p4w, p5w, p6w, p7w, p8w]
p1b = class_of_pieses.pawn("black", "a", 7)
p2b = class_of_pieses.pawn("black", "b", 7)
p3b = class_of_pieses.pawn("black", "c", 7)
p4b = class_of_pieses.pawn("black", "d", 7)
p5b = class_of_pieses.pawn("black", "e", 7)
p6b = class_of_pieses.pawn("black", "f", 7)
p7b = class_of_pieses.pawn("black", "g", 7)
p8b = class_of_pieses.pawn("black", "h", 7)
k1b = class_of_pieses.knight("black", "b", 8)
k2b = class_of_pieses.knight("black", "g", 8)
b1b = class_of_pieses.bishop("black", "c", 8)
b2b = class_of_pieses.bishop("black", "f", 8)
r1b = class_of_pieses.rook("black", "a", 8)
r2b = class_of_pieses.rook("black", "h", 8)
kb = class_of_pieses.king("black", "d", 8)
qb = class_of_pieses.queen("black", "e", 8)
black_pieces = [p1b, p2b, p3b, p4b, p5b, p6b, p7b, p8b,\
                k1b, k2b, b1b, b2b, r1b, r2b, kb, qb] 
pawn_list_black = [p1b, p2b, p3b, p4b, p5b, p6b, p7b, p8b]