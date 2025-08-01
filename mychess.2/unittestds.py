
#from ds

import unittest
from unittest.mock import patch
import game
import chess_board
import board
import class_of_pieces

class TestChessGame(unittest.TestCase):
    
    def setUp(self):
        # Reset the board state before each test
        chess_board.white_pieces = []
        chess_board.black_pieces = []
        # Initialize with some pieces for testing
        self.white_pawn = chess_board.p1w = class_of_pieces.pawn("white", "a", 2)
        self.black_pawn = chess_board.p1b = class_of_pieces.pawn("black", "a", 7)
        chess_board.white_pieces = [self.white_pawn]
        chess_board.black_pieces = [self.black_pawn]
    
    @patch('builtins.input', side_effect=['yes', 'yes'])
    def test_game_initialization(self, mock_input):
        with patch('game.reeding_request') as mock_reeding:
            mock_reeding.return_value = True
            game.request0 = 'yes'
            # This will run the main game loop until break
            with self.assertRaises(SystemExit):
                game.reeding_request("pawn in a2 move to a4", "white")
    
    def test_reeding_request_valid_move(self):
        result = game.reeding_request("pawn in a2 move to a3", "white")
        self.assertTrue(result)
    
    def test_reeding_request_invalid_format(self):
        result = game.reeding_request("invalid command", "white")
        self.assertFalse(result)
    
    @patch('builtins.input', return_value='q')
    def test_promotion_pawn(self, mock_input):
        # Place a pawn at promotion square
        pawn = class_of_pieces.pawn("white", "a", 7)
        chess_board.white_pieces.append(pawn)
        result = pawn.moving("a8")
        self.assertTrue(result)
        # Should have promoted to queen
    
    def test_castling_request(self):
        # Setup castling conditions
        chess_board.kw = class_of_pieces.king("white", "e", 1)
        chess_board.r1w = class_of_pieces.rook("white", "a", 1)
        chess_board.r2w = class_of_pieces.rook("white", "h", 1)
        chess_board.white_pieces.extend([chess_board.kw, chess_board.r1w, chess_board.r2w])
        
        result = game.reeding_request("long castel", "white")
        self.assertTrue(result)
        # King should have moved to c1, rook to d1

if __name__ == '__main__':
    unittest.main()