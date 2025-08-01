#from gpt
import unittest

# کلاس ساده Piece برای تست
class Piece:
    def __init__(self, name, row, colmn):
        self.name = name
        self.row = row
        self.colmn = colmn

    # متد moving به صورت خیلی ساده فقط جای جدید را قبول می‌کند و قطعه را جابجا می‌کند
    def moving(self, pos):
        # pos یک لیست یا تاپل مثل ['e', 4]
        new_row, new_col = pos
        # اینجا می‌توان منطق حرکت درست را گذاشت، اینجا فقط جابجایی ساده است
        self.row = new_row
        self.colmn = new_col
        return True

# تابع process_command که از قبل تعریف کردیم
def process_command(command, pieces):
    command = command.strip().lower()

    if command == "out":
        return "exit"

    if command == "castle" or command == "castling":
        # فرض کنیم قلعه موفق است
        return True

    parts = command.split()
    if len(parts) == 6 and parts[1] == "in" and parts[3] == "move" and parts[4] == "to":
        piece_name = parts[0]
        start_pos = parts[2]
        end_pos = parts[5]

        start_row = start_pos[0]
        start_col = int(start_pos[1])
        end_row = end_pos[0]
        end_col = int(end_pos[1])

        target_piece = None
        for p in pieces:
            if p.name == piece_name and p.row == start_row and p.colmn == start_col:
                target_piece = p
                break

        if not target_piece:
            return False

        if target_piece.moving([end_row, end_col]):
            return True
        else:
            return False

    return False

# کلاس تست با unittest
class TestProcessCommand(unittest.TestCase):
    def setUp(self):
        # ساختن چند قطعه برای تست
        self.pawn = Piece('pawn', 'e', 2)
        self.knight = Piece('knight', 'g', 1)
        self.pieces = [self.pawn, self.knight]

    def test_exit_command(self):
        self.assertEqual(process_command("out", self.pieces), "exit")

    def test_castle_command(self):
        self.assertTrue(process_command("castle", self.pieces))
        self.assertTrue(process_command("castling", self.pieces))

    def test_valid_move(self):
        result = process_command("pawn in e2 move to e4", self.pieces)
        self.assertTrue(result)
        self.assertEqual(self.pawn.row, 'e')
        self.assertEqual(self.pawn.colmn, 4)

    def test_invalid_piece_position(self):
        result = process_command("pawn in e3 move to e4", self.pieces)  # pawn اینجا e3 نیست
        self.assertFalse(result)

    def test_invalid_command_format(self):
        result = process_command("move pawn e2 to e4", self.pieces)  # فرمت اشتباه
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()