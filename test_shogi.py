import unittest
from parameterized import parameterized
from shogi import Shogi, Piece, Pawn, Lance, Knight, SilverGeneral, GoldGeneral, King, Bishop, Rook

class TestShogi(unittest.TestCase):

    def setUp(self):
        self.game = Shogi()
        self.sample_board = [
            ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]]

    @parameterized.expand([
        (0,),
        (1,),
        (2,),
        (3,),
        (4,),
        (5,),
        (6,),
        (7,),
        (8,),
    ])
    def test_setup(self, row):
        self.assertTrue(self.game.is_playing)
        self.assertEqual(len(self.game.board), 9)
        self.assertEqual(len(self.game.board[row]), 9)
        self.assertEqual(self.game.error, "")
        self.assertEqual(self.game.white_captures, [])
        self.assertEqual(self.game.black_captures, [])
    
    @parameterized.expand([
        ("black", (0, 1, 2)),
        ("white", (8, 7, 6)),
        ])
    def test_board_valid(self, color, rows):
        king_row, rook_row, pawn_row = rows
        pieces = ["Lance", "Knight", "SilverGeneral", "GoldGeneral", "King", "GoldGeneral", "SilverGeneral", "Knight", "Lance"]
        reversed_row = ["   ", "Bishop", "   ", "   ", "   ", "   ", "   ", "Rook", "   "]
        if color == "black":
            reversed_row.reverse() 
        for col in range(9):
            self.assertTrue(self.game.board[pawn_row][col].__class__.__name__ == "Pawn")
            self.assertEqual(self.game.board[pawn_row][col].color, color)
            self.assertTrue(self.game.board[king_row][col].__class__.__name__ == pieces[col])
            self.assertEqual(self.game.board[king_row][col].color, color)
            if self.game.board[rook_row][col] != "   ":
                if color == "white":
                    self.assertTrue(self.game.board[rook_row][col].__class__.__name__ == reversed_row[col])
                    self.assertEqual(self.game.board[king_row][col].color, color)
                elif color == "black":
                    self.assertTrue(self.game.board[rook_row][col].__class__.__name__ == reversed_row[col])
                    self.assertEqual(self.game.board[king_row][col].color, color)

    @parameterized.expand([
        ("white", "\u2227", (7, 1)),
        ("black", "\u2228", (2, 4)),
    ])
    def test_pawn_creation(self, color, orientation, position):
        pawn = Pawn(color, position)
        self.assertEqual(pawn.color, color)
        self.assertEqual(pawn.name, "P")
        self.assertFalse(pawn.promoted)
        self.assertFalse(pawn.set_for_promotion)
        self.assertFalse(pawn.captured)
        self.assertEqual(str(pawn), f" P{orientation}")

    @parameterized.expand([
        ("white", "\u2227", (7, 1)),
        ("black", "\u2228", (2, 4)),
    ])
    def test_lance_creation(self, color, orientation, position):
        lance = Lance(color, position)
        self.assertEqual(lance.color, color)
        self.assertEqual(lance.name, "L")
        self.assertFalse(lance.promoted)
        self.assertFalse(lance.set_for_promotion)
        self.assertFalse(lance.captured)
        self.assertEqual(str(lance), f" L{orientation}")
    
    @parameterized.expand([
        ("white", "\u2227", (7, 1)),
        ("black", "\u2228", (2, 4)),
    ])
    def test_knight_creation(self, color, orientation, position):
        knight = Knight(color, position)
        self.assertEqual(knight.color, color)
        self.assertEqual(knight.name, "N")
        self.assertFalse(knight.promoted)
        self.assertFalse(knight.set_for_promotion)
        self.assertFalse(knight.captured)
        self.assertEqual(str(knight), f" N{orientation}")
    
    @parameterized.expand([
        ("white", "\u2227", (7, 1)),
        ("black", "\u2228", (2, 4)),
    ])
    def test_silvergeneral_creation(self, color, orientation, position):
        silvergeneral = SilverGeneral(color, position)
        self.assertEqual(silvergeneral.color, color)
        self.assertEqual(silvergeneral.name, "S")
        self.assertFalse(silvergeneral.promoted)
        self.assertFalse(silvergeneral.set_for_promotion)
        self.assertFalse(silvergeneral.captured)
        self.assertEqual(str(silvergeneral), f" S{orientation}")
    
    @parameterized.expand([
        ("white", "\u2227", (7, 1)),
        ("black", "\u2228", (2, 4)),
    ])
    def test_goldgeneral_creation(self, color, orientation, position):
        goldgeneral = GoldGeneral(color, position)
        self.assertEqual(goldgeneral.color, color)
        self.assertEqual(goldgeneral.name, "G")
        self.assertFalse(goldgeneral.promoted)
        self.assertFalse(goldgeneral.set_for_promotion)
        self.assertFalse(goldgeneral.captured)
        self.assertEqual(str(goldgeneral), f" G{orientation}")
    
    @parameterized.expand([
        ("white", "\u2227", (7, 1)),
        ("black", "\u2228", (2, 4)),
    ])
    def test_king_creation(self, color, orientation, position):
        king = King(color, position)
        self.assertEqual(king.color, color)
        self.assertEqual(king.name, "K")
        self.assertFalse(king.promoted)
        self.assertFalse(king.set_for_promotion)
        self.assertFalse(king.captured)
        self.assertEqual(str(king), f" K{orientation}")
    
    @parameterized.expand([
        ("white", "\u2227", (7, 1)),
        ("black", "\u2228", (2, 4)),
    ])
    def test_bishop_creation(self, color, orientation, position):
        bishop = Bishop(color, position)
        self.assertEqual(bishop.color, color)
        self.assertEqual(bishop.name, "B")
        self.assertFalse(bishop.promoted)
        self.assertFalse(bishop.set_for_promotion)
        self.assertFalse(bishop.captured)
        self.assertEqual(str(bishop), f" B{orientation}")
    
    @parameterized.expand([
        ("white", "\u2227", (7, 1)),
        ("black", "\u2228", (2, 4)),
    ])
    def test_rook_creation(self, color, orientation, position):
        rook = Rook(color, position)
        self.assertEqual(rook.color, color)
        self.assertEqual(rook.name, "R")
        self.assertFalse(rook.promoted)
        self.assertFalse(rook.set_for_promotion)
        self.assertFalse(rook.captured)
        self.assertEqual(str(rook), f" R{orientation}")

    @parameterized.expand([
        ("white", [(3, 4)], [], [(3, 4)]),
        ("black", [(5, 4)], [], [(5, 4)]),
    ])
    def test_pawn_moves_unpromoted(self, color, valid_moves, movement_hindered, move_to_capture):
        self.game.board = self.sample_board
        self.game.board[4][4] = Pawn(color, (4, 4))
        self.assertEqual(self.game.board[4][4].movement_unpromoted(self.game.board), valid_moves)
        self.game.board[3][4] = self.game.board[5][4] = Pawn(color, (1, 1))
        self.assertEqual(self.game.board[4][4].movement_unpromoted(self.game.board), movement_hindered)
        self.game.board[3][4] = self.game.board[5][4] = Pawn("test-color", (1, 1))
        self.assertEqual(self.game.board[4][4].movement_unpromoted(self.game.board), move_to_capture)
    
    @parameterized.expand([
        ("white", [(0, 4), (1, 4), (2, 4), (3, 4)], [(2, 4), (3, 4)], [(1, 4), (2, 4), (3, 4)]),
        ("black", [(5, 4), (6, 4), (7, 4), (8, 4)], [(5, 4), (6, 4)], [(5, 4), (6, 4), (7, 4)]),
    ])
    def test_lance_moves_unpromoted(self, color, valid_moves, movement_hindered, move_to_capture):
        self.game.board = self.sample_board
        self.game.board[4][4] = Lance(color, (4, 4))
        self.assertEqual(self.game.board[4][4].movement_unpromoted(self.game.board), valid_moves)
        self.game.board[1][4] = self.game.board[7][4] = Pawn(color, (1, 1))
        self.assertEqual(self.game.board[4][4].movement_unpromoted(self.game.board), movement_hindered)
        self.game.board[1][4] = self.game.board[7][4] = Pawn("test-color", (1, 1))
        self.assertEqual(self.game.board[4][4].movement_unpromoted(self.game.board), move_to_capture)

    @parameterized.expand([
        ("white", [(2, 3), (2, 5)], [(2, 3)], [(2, 3), (2, 5)]),
        ("black", [(6, 3), (6, 5)], [(6, 3)], [(6, 3), (6, 5)]),
    ])
    def test_knight_moves_unpromoted(self, color, valid_moves, movement_hindered, move_to_capture):
        self.game.board = self.sample_board
        self.game.board[4][4] = Knight(color, (4, 4))
        self.assertEqual(self.game.board[4][4].movement_unpromoted(self.game.board), valid_moves)
        self.game.board[2][5] = self.game.board[6][5] = Pawn(color, (1, 1))
        self.assertEqual(self.game.board[4][4].movement_unpromoted(self.game.board), movement_hindered)
        self.game.board[2][5] = self.game.board[6][5] = Pawn("test-color", (1, 1))
        self.assertEqual(self.game.board[4][4].movement_unpromoted(self.game.board), move_to_capture)
    
    @parameterized.expand([
        ("white", [(3, 3), (3, 4), (3, 5), (5, 3), (5, 5)], 
        [(3, 3), (3, 5), (5, 3), (5, 5)], 
        [(3, 3), (3, 4), (3, 5), (5, 3), (5, 5)]
        ),
        ("black", [(3, 3), (3, 5), (5, 3), (5, 4), (5, 5)], 
        [(3, 3), (3, 5), (5, 3), (5, 5)], 
        [(3, 3), (3, 5), (5, 3), (5, 4), (5, 5)]
        ),
    ])
    def test_silvergeneral_moves_unpromoted(self, color, valid_moves, movement_hindered, move_to_capture):
        self.game.board = self.sample_board
        self.game.board[4][4] = SilverGeneral(color, (4, 4))
        self.assertEqual(self.game.board[4][4].movement_unpromoted(self.game.board), valid_moves)
        self.game.board[5][4] = self.game.board[3][4] = Pawn(color, (1, 1))
        self.assertEqual(self.game.board[4][4].movement_unpromoted(self.game.board), movement_hindered)
        self.game.board[5][4] = self.game.board[3][4] = Pawn("test-color", (1, 1))
        self.assertEqual(self.game.board[4][4].movement_unpromoted(self.game.board), move_to_capture)
    
    @parameterized.expand([
        ("white", [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 4)], 
        [(3, 3),(3, 5), (4, 3), (4, 5)], 
        [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 4)]
        ),
        ("black", [(3, 4), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5)], 
        [(4, 3), (4, 5), (5, 3),(5, 5)], 
        [(3, 4), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5)]
        ),
    ])
    def test_goldgeneral_moves_unpromoted(self, color, valid_moves, movement_hindered, move_to_capture):
        self.game.board = self.sample_board
        self.game.board[4][4] = GoldGeneral(color, (4, 4))
        self.assertEqual(self.game.board[4][4].movement_unpromoted(self.game.board), valid_moves)
        self.game.board[5][4] = self.game.board[3][4] = Pawn(color, (1, 1))
        self.assertEqual(self.game.board[4][4].movement_unpromoted(self.game.board), movement_hindered)
        self.game.board[5][4] = self.game.board[3][4] = Pawn("test-color", (1, 1))
        self.assertEqual(self.game.board[4][4].movement_unpromoted(self.game.board), move_to_capture)
    
    @parameterized.expand([
        ("white", [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 4)], 
        [(3, 3),(3, 5), (4, 3), (4, 5)], 
        [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 4)]
        ),
        ("black", [(3, 4), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5)], 
        [(4, 3), (4, 5), (5, 3),(5, 5)], 
        [(3, 4), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5)]
        ),
    ])
    def test_pieces_promoted_to_goldgeneral(self, color, valid_moves, movement_hindered, move_to_capture):
        pieces = [Pawn, Lance, Knight, SilverGeneral]
        self.game.board = self.sample_board
        for piece in pieces:
            self.game.board[4][4] = piece(color, (4, 4))
            self.game.board[4][4].promote()
            self.assertEqual(self.game.board[4][4].movement_promoted(self.game.board), valid_moves)
            self.game.board[5][4] = self.game.board[3][4] = Pawn(color, (1, 1))
            self.assertEqual(self.game.board[4][4].movement_promoted(self.game.board), movement_hindered)
            self.game.board[5][4] = self.game.board[3][4] = Pawn("test-color", (1, 1))
            self.assertEqual(self.game.board[4][4].movement_promoted(self.game.board), move_to_capture)
        
    @parameterized.expand([
        ("white", [(0, 4), (1, 4), (2, 4), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7), (4, 8), (5, 4), (6, 4), (7, 4), (8, 4)], 
        [(0, 4), (1, 4), (2, 4), (3, 4), (4, 3), (4, 5),(5, 4), (6, 4), (7, 4), (8, 4)], 
        [(0, 4), (1, 4), (2, 4), (3, 4), (4, 2), (4, 3), (4, 5), (4, 6),(5, 4), (6, 4), (7, 4), (8, 4)]
        ),
        ("black", [(0, 4), (1, 4), (2, 4), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7), (4, 8), (5, 4), (6, 4), (7, 4), (8, 4)], 
        [(0, 4), (1, 4), (2, 4), (3, 4), (4, 3), (4, 5),(5, 4), (6, 4), (7, 4), (8, 4)], 
        [(0, 4), (1, 4), (2, 4), (3, 4), (4, 2), (4, 3), (4, 5), (4, 6),(5, 4), (6, 4), (7, 4), (8, 4)]
        ),
    ])
    def test_rook_moves_unpromoted(self, color, valid_moves, movement_hindered, move_to_capture):
        self.game.board = self.sample_board
        self.game.board[4][4] = Rook(color, (4, 4))
        self.assertEqual(self.game.board[4][4].movement_unpromoted(self.game.board), valid_moves)
        self.game.board[4][2] = self.game.board[4][6] = Pawn(color, (1, 1))
        self.assertEqual(self.game.board[4][4].movement_unpromoted(self.game.board), movement_hindered)
        self.game.board[4][2] = self.game.board[4][6] = Pawn("test-color", (1, 1))
        self.assertEqual(self.game.board[4][4].movement_unpromoted(self.game.board), move_to_capture)
    
    @parameterized.expand([
        ("white", [(0, 4), (1, 4), (2, 4), (3, 3), (3, 4), (3, 5), (4, 0), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7), (4, 8), (5, 3), (5, 4), (5, 5), (6, 4), (7, 4), (8, 4)], 
        [(0, 4), (1, 4), (2, 4), (3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5), (6, 4), (7, 4), (8, 4)], 
        [(0, 4), (1, 4), (2, 4), (3, 3), (3, 4), (3, 5), (4, 2), (4, 3), (4, 5), (4, 6), (5, 3), (5, 4), (5, 5), (6, 4), (7, 4), (8, 4)]
        ),
        ("black", [(0, 4), (1, 4), (2, 4), (3, 3), (3, 4), (3, 5), (4, 0), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7), (4, 8), (5, 3), (5, 4), (5, 5), (6, 4), (7, 4), (8, 4)], 
        [(0, 4), (1, 4), (2, 4), (3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5), (6, 4), (7, 4), (8, 4)], 
        [(0, 4), (1, 4), (2, 4), (3, 3), (3, 4), (3, 5), (4, 2), (4, 3), (4, 5), (4, 6), (5, 3), (5, 4), (5, 5), (6, 4), (7, 4), (8, 4)]
        ),
    ])
    def test_rook_moves_promoted(self, color, valid_moves, movement_hindered, move_to_capture):
        self.game.board = self.sample_board
        self.game.board[4][4] = Rook(color, (4, 4))
        self.game.board[4][4].promote()
        self.assertEqual(self.game.board[4][4].movement_promoted(self.game.board), valid_moves)
        self.game.board[4][2] = self.game.board[4][6] = Pawn(color, (1, 1))
        self.assertEqual(self.game.board[4][4].movement_promoted(self.game.board), movement_hindered)
        self.game.board[4][2] = self.game.board[4][6] = Pawn("test-color", (1, 1))
        self.assertEqual(self.game.board[4][4].movement_promoted(self.game.board), move_to_capture)

    @parameterized.expand([
        ("white", [(0, 0), (0, 8), (1, 1), (1, 7), (2, 2), (2, 6), (3, 3), (3, 5), (5, 3), (5, 5), (6, 2), (6, 6), (7, 1), (7, 7), (8, 0), (8, 8)], 
        [(3, 3), (3, 5), (5, 3), (5, 5), (6, 2), (6, 6), (7, 1), (7, 7), (8, 0), (8, 8)],
        [(2, 2), (2, 6), (3, 3), (3, 5), (5, 3), (5, 5), (6, 2), (6, 6), (7, 1), (7, 7), (8, 0), (8, 8)],
        ),
        ("black", [(0, 0), (0, 8), (1, 1), (1, 7), (2, 2), (2, 6), (3, 3), (3, 5), (5, 3), (5, 5), (6, 2), (6, 6), (7, 1), (7, 7), (8, 0), (8, 8)], 
        [(3, 3), (3, 5), (5, 3), (5, 5), (6, 2), (6, 6), (7, 1), (7, 7), (8, 0), (8, 8)],
        [(2, 2), (2, 6), (3, 3), (3, 5), (5, 3), (5, 5), (6, 2), (6, 6), (7, 1), (7, 7), (8, 0), (8, 8)],
        ),
    ])
    def test_bishop_moves_unpromoted(self, color, valid_moves, movement_hindered, move_to_capture):
        self.game.board = self.sample_board
        self.game.board[4][4] = Bishop(color, (4, 4))
        self.assertEqual(self.game.board[4][4].movement_unpromoted(self.game.board), valid_moves)
        self.game.board[2][2] = self.game.board[2][6] = Pawn(color, (1, 1))
        self.assertEqual(self.game.board[4][4].movement_unpromoted(self.game.board), movement_hindered)
        self.game.board[2][2] = self.game.board[2][6] = Pawn("test-color", (1, 1))
        self.assertEqual(self.game.board[4][4].movement_unpromoted(self.game.board), move_to_capture)
    
    @parameterized.expand([
        ("white", [(0, 0), (0, 8), (1, 1), (1, 7), (2, 2), (2, 6), (3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5), (6, 2), (6, 6), (7, 1), (7, 7), (8, 0), (8, 8)], 
        [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5), (6, 2), (6, 6), (7, 1), (7, 7), (8, 0), (8, 8)],
        [(2, 2), (2, 6), (3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5), (6, 2), (6, 6), (7, 1), (7, 7), (8, 0), (8, 8)],
        ),
        ("black", [(0, 0), (0, 8), (1, 1), (1, 7), (2, 2), (2, 6), (3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5), (6, 2), (6, 6), (7, 1), (7, 7), (8, 0), (8, 8)], 
        [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5), (6, 2), (6, 6), (7, 1), (7, 7), (8, 0), (8, 8)],
        [(2, 2), (2, 6), (3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5), (6, 2), (6, 6), (7, 1), (7, 7), (8, 0), (8, 8)],
        ),
    ])
    def test_bishop_moves_promoted(self, color, valid_moves, movement_hindered, move_to_capture):
        self.game.board = self.sample_board
        self.game.board[4][4] = Bishop(color, (4, 4))
        self.game.board[4][4].promote()
        self.assertEqual(self.game.board[4][4].movement_promoted(self.game.board), valid_moves)
        self.game.board[2][2] = self.game.board[2][6] = Pawn(color, (1, 1))
        self.assertEqual(self.game.board[4][4].movement_promoted(self.game.board), movement_hindered)
        self.game.board[2][2] = self.game.board[2][6] = Pawn("test-color", (1, 1))
        self.assertEqual(self.game.board[4][4].movement_promoted(self.game.board), move_to_capture)
    
    def test_valid_moves_method(self):
        unpromoted_valid_moves = [(3, 4)]
        promoted_valid_moves = [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 4)]
        self.game.board = self.sample_board
        self.game.board[4][4] = Pawn("white", (4, 4))
        self.assertEqual(self.game.board[4][4].valid_moves(self.game.board), unpromoted_valid_moves)
        self.game.board[4][4].promote()
        self.assertEqual(self.game.board[4][4].valid_moves(self.game.board), promoted_valid_moves)
        
    def test_promote_method(self):
        self.game.board = self.sample_board
        self.game.board[4][4] = Pawn("white", (4, 4))
        self.assertFalse(self.game.board[4][4].promoted)
        self.game.board[4][4].promote()
        self.assertTrue(self.game.board[4][4].promoted)
        self.assertFalse(self.game.board[4][4].set_for_promotion)
    
    def test_update_position_method(self):
        self.game.board = self.sample_board
        self.game.board[4][4] = Pawn("white", (4, 4))
        self.assertEqual(self.game.board[4][4].position, (4, 4))
        self.game.board[4][4].update_position(3, 4)
        self.assertEqual(self.game.board[4][4].position, (3, 4))
    
    @parameterized.expand([
        ("white", (2, 4)),
        ("black", (6, 4)),
    ])
    def test_check_if_valid_for_promotion(self, color, coordinates):
        row, col = coordinates
        self.game.board = self.sample_board
        self.game.board[4][4] = Pawn(color, (4, 4))
        self.assertFalse(self.game.board[4][4].set_for_promotion)
        self.game.board[4][4].update_position(row, col)
        self.assertTrue(self.game.board[4][4].set_for_promotion)
    
    @parameterized.expand([
        ("white", (2, 4)),
        ("black", (6, 4)),
    ])
    def test_king_goldengeneral_never_valid_for_promotion(self, color, coordinates):
        pieces = [King, GoldGeneral]
        row, col = coordinates
        self.game.board = self.sample_board
        for piece in pieces:
            self.game.board[4][4] = piece(color, (4, 4))
            self.assertFalse(self.game.board[4][4].set_for_promotion)
            self.game.board[4][4].update_position(row, col)
            self.assertFalse(self.game.board[4][4].set_for_promotion)

    @parameterized.expand([
        ("white", [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)], [(1, 0), (1, 1)]),
        ("black", [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)], [(0, 1), (1, 1)]),
    ])
    def test_filter_moves_normal_method(self, color, coords, filtered_coords):
        self.game.board = self.sample_board
        self.game.board[0][0] = King(color, (0, 0))
        self.game.board[0][1] = Pawn("white", (0, 1))
        self.game.board[1][0] = Pawn("black", (1, 0))
        self.assertEqual(self.game.board[0][0].filter_moves(coords, self.game.board), filtered_coords)

    @parameterized.expand([
        ("white", [(3, 4), (2, 4), (1, 4), (0, 4)], [(3, 3), (2, 3), (1, 3), (0, 3)], [(3, 4)], [(2, 3), (3, 3)]),
        ("black", [(5, 4), (6, 4), (7, 4), (8, 4)], [(5, 3), (6, 3), (7, 3), (8, 3)], [(5, 4), (6, 4)], [(5, 3)]),
    ])
    def test_filter_moves_lance_method(self, color, moves_1, moves_2, filtered_1, filtered_2):
        self.game.board = self.sample_board
        self.game.board[4][4] = Lance(color, (4, 4))
        self.game.board[4][3] = Lance(color, (4, 3))
        self.game.board[2][4] = Pawn("white", (2, 4))
        self.game.board[2][3] = Pawn("black", (2, 3))
        self.game.board[6][4] = Pawn("white", (6, 4))
        self.game.board[6][3] = Pawn("black", (6, 3))
        self.assertEqual(self.game.board[4][4].filter_moves(moves_1, self.game.board), filtered_1)
        self.assertEqual(self.game.board[4][3].filter_moves(moves_2, self.game.board), filtered_2)

    @parameterized.expand([
        ("white", [(3, 4), (2, 4), (1, 4), (0, 4)], [(3, 3), (2, 3), (1, 3), (0, 3)], [(3, 4)], [(2, 3), (3, 3)]),
        ("black", [(5, 4), (6, 4), (7, 4), (8, 4)], [(5, 3), (6, 3), (7, 3), (8, 3)], [(5, 4), (6, 4)], [(5, 3)]),
    ])
    def test_filter_moves_rook_method(self, color, moves_1, moves_2, filtered_1, filtered_2):
        self.game.board = self.sample_board
        self.game.board[4][4] = Lance(color, (4, 4))
        self.game.board[4][3] = Lance(color, (4, 3))
        self.game.board[2][4] = Pawn("white", (2, 4))
        self.game.board[2][3] = Pawn("black", (2, 3))
        self.game.board[6][4] = Pawn("white", (6, 4))
        self.game.board[6][3] = Pawn("black", (6, 3))
        self.assertEqual(self.game.board[4][4].filter_moves(moves_1, self.game.board), filtered_1)
        self.assertEqual(self.game.board[4][3].filter_moves(moves_2, self.game.board), filtered_2)
    # 32 funciones por hacer
    # 5 por dia daria 6 dias para terminar















"""
    def test_move_white(self):
        # mover una ficha de blancas
        # chequear que el tablero se actualice correctamente
        return

    def test_move_black(self):
        # lo mismo que withe pero con black
        return

    def test_capture_white(self):
        # capturar una ficha
        # chequear tablero
        # chequear fichas capturadas
        return

    def test_capture_black(self):
        # igual que para blanco
        return

    def test_drop_white(self):
        # invocar una ficha comida para blanco
        # chequear el tablero y las fichas comidas
        # chequear que la ficha se invoque en su version sin promocionar
        return

    def test_drop_black(self):
        # igual que para blanco
        return

    def test_check_white(self):
        # chequea que el rey  este amenazado
        # chequea que si hay movimientos posibles para salir del check
        return

    def test_check_black(self):
        # igual que para blanco
        return

    def test_checkmate_white(self):
        # chequea que el rey esta amenazado
        # chequear que cualquier movimiento del rey resulte en estar amenazado
        return

    def test_checkmate_black(self):
        # igual que para blanco
        return
    
    def test_win(self):
        return

#####################################################################
#####################################################################

    =======Funciones de shogi=======

    def board_print(self):
    
    def set_board(self):

    def place_pieces(self):

    def play_origin(self, row, column):
    
    def validate_origin_coordinates_values(self, row, column):
    
    def current_player_captures(self):
    
    def validate_origin_coordinates_location(self, row, column):
    
    def lift_piece_for_movement(self, row, column):
    
    def play_destination(self, row, column):
    
    def validate_destination_coordinates(self, row, column):
    
    def move_piece(self, row, column):
    
    def clean_lifted_piece_origin_location(self):
    
    def next_turn(self):
    
#####################################################################
#####################################################################

    =======Funciones de piezas=======

    ---------------def valid_moves(self, board):
    
    ----------------def movement_unpromoted(self, board):
    
    --------------def movement_promoted(self, board):
    
    def filter_moves(self, coordinates, board):
    
    ----------------def promote(self):
    
    -----------------def update_position(self, row, column):
    
    def valid_drops(self, board):
    
    def pawn_drop_rules(self, board, valid_locations):








"""

if __name__ == "__main__":
    unittest.main()