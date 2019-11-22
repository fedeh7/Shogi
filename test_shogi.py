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
        row_1, row_2, row_3 = rows
        pieces = [
            Lance, Knight, SilverGeneral,
            GoldGeneral, King, GoldGeneral,
            SilverGeneral, Knight, Lance]
        reversed_row = [
            "   ", Bishop, "   ",
            "   ", "   ", "   ",
            "   ", Rook, "   "]
        if color == "black":
            reversed_row.reverse()
        for col in range(9):
            self.assertTrue(isinstance(self.game.board[row_3][col], Pawn))
            self.assertEqual(self.game.board[row_3][col].color, color)
            self.assertTrue(isinstance(self.game.board[row_1][col], pieces[col]))
            self.assertEqual(self.game.board[row_1][col].color, color)
            if self.game.board[row_2][col] != "   ":
                if color == "white":
                    self.assertTrue(isinstance(self.game.board[row_2][col], reversed_row[col]))
                    self.assertEqual(self.game.board[row_1][col].color, color)
                elif color == "black":
                    self.assertTrue(isinstance(self.game.board[row_2][col], reversed_row[col]))
                    self.assertEqual(self.game.board[row_1][col].color, color)

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
    def test_pawn_moves_unpromoted(self, color, valid, obstacle, capture):
        self.game.board = self.sample_board
        self.game.board[4][4] = Pawn(color, (4, 4))
        self.assertEqual(
            self.game.board[4][4].movement_unpromoted(self.game.board),
            valid)
        self.game.board[3][4] = self.game.board[5][4] = Pawn(color, (1, 1))
        self.assertEqual(
            self.game.board[4][4].movement_unpromoted(self.game.board),
            obstacle)
        self.game.board[3][4] = self.game.board[5][4] = Pawn("color", (1, 1))
        self.assertEqual(
            self.game.board[4][4].movement_unpromoted(self.game.board),
            capture)

    @parameterized.expand([
        ("white",
            [(0, 4), (1, 4), (2, 4), (3, 4)], [(2, 4), (3, 4)], [(1, 4), (2, 4), (3, 4)]),
        ("black",
            [(5, 4), (6, 4), (7, 4), (8, 4)], [(5, 4), (6, 4)], [(5, 4), (6, 4), (7, 4)]),
    ])
    def test_lance_moves_unpromoted(self, color, valid, obstacle, capture):
        self.game.board = self.sample_board
        self.game.board[4][4] = Lance(color, (4, 4))
        self.assertEqual(
            self.game.board[4][4].movement_unpromoted(self.game.board),
            valid)
        self.game.board[1][4] = self.game.board[7][4] = Pawn(color, (1, 1))
        self.assertEqual(
            self.game.board[4][4].movement_unpromoted(self.game.board),
            obstacle)
        self.game.board[1][4] = self.game.board[7][4] = Pawn("color", (1, 1))
        self.assertEqual(
            self.game.board[4][4].movement_unpromoted(self.game.board),
            capture)

    @parameterized.expand([
        ("white", [(2, 3), (2, 5)], [(2, 3)], [(2, 3), (2, 5)]),
        ("black", [(6, 3), (6, 5)], [(6, 3)], [(6, 3), (6, 5)]),
    ])
    def test_knight_moves_unpromoted(self, color, valid, obstacle, capture):
        self.game.board = self.sample_board
        self.game.board[4][4] = Knight(color, (4, 4))
        self.assertEqual(
            self.game.board[4][4].movement_unpromoted(self.game.board),
            valid)
        self.game.board[2][5] = self.game.board[6][5] = Pawn(color, (1, 1))
        self.assertEqual(
            self.game.board[4][4].movement_unpromoted(self.game.board),
            obstacle)
        self.game.board[2][5] = self.game.board[6][5] = Pawn("color", (1, 1))
        self.assertEqual(
            self.game.board[4][4].movement_unpromoted(self.game.board),
            capture)

    @parameterized.expand([
        ("white",
            [(3, 3), (3, 4), (3, 5), (5, 3), (5, 5)],
            [(3, 3), (3, 5), (5, 3), (5, 5)],
            [(3, 3), (3, 4), (3, 5), (5, 3), (5, 5)]),
        ("black",
            [(3, 3), (3, 5), (5, 3), (5, 4), (5, 5)],
            [(3, 3), (3, 5), (5, 3), (5, 5)],
            [(3, 3), (3, 5), (5, 3), (5, 4), (5, 5)]),
    ])
    def test_silvergeneral_moves_unpromoted(self, color, valid, obstacle, capture):
        self.game.board = self.sample_board
        self.game.board[4][4] = SilverGeneral(color, (4, 4))
        self.assertEqual(
            self.game.board[4][4].movement_unpromoted(self.game.board),
            valid)
        self.game.board[5][4] = self.game.board[3][4] = Pawn(color, (1, 1))
        self.assertEqual(
            self.game.board[4][4].movement_unpromoted(self.game.board),
            obstacle)
        self.game.board[5][4] = self.game.board[3][4] = Pawn("color", (1, 1))
        self.assertEqual(
            self.game.board[4][4].movement_unpromoted(self.game.board),
            capture)

    @parameterized.expand([
        ("white",
            [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 4)],
            [(3, 3), (3, 5), (4, 3), (4, 5)],
            [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 4)]),
        ("black",
            [(3, 4), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5)],
            [(4, 3), (4, 5), (5, 3), (5, 5)],
            [(3, 4), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5)]),
    ])
    def test_goldgeneral_moves(self, color, valid, obstacle, capture):
        self.game.board = self.sample_board
        self.game.board[4][4] = GoldGeneral(color, (4, 4))
        self.assertEqual(
            self.game.board[4][4].movement_unpromoted(self.game.board),
            valid)
        self.game.board[5][4] = self.game.board[3][4] = Pawn(color, (1, 1))
        self.assertEqual(
            self.game.board[4][4].movement_unpromoted(self.game.board),
            obstacle)
        self.game.board[5][4] = self.game.board[3][4] = Pawn("color", (1, 1))
        self.assertEqual(
            self.game.board[4][4].movement_unpromoted(self.game.board),
            capture)

    @parameterized.expand([
        ("white",
            [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 4)],
            [(3, 3), (3, 5), (4, 3), (4, 5)],
            [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 4)]),
        ("black",
            [(3, 4), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5)],
            [(4, 3), (4, 5), (5, 3), (5, 5)],
            [(3, 4), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5)]),
    ])
    def test_normal_pieces_promoted(self, color, valid, obstacle, capture):
        pieces = [Pawn, Lance, Knight, SilverGeneral]
        self.game.board = self.sample_board
        for piece in pieces:
            self.game.board[4][4] = piece(color, (4, 4))
            self.game.board[4][4].promote()
            self.assertEqual(self.game.board[4][4].movement_promoted(self.game.board), valid)
            self.game.board[5][4] = self.game.board[3][4] = Pawn(color, (1, 1))
            self.assertEqual(self.game.board[4][4].movement_promoted(self.game.board), obstacle)
            self.game.board[5][4] = self.game.board[3][4] = Pawn("color", (1, 1))
            self.assertEqual(self.game.board[4][4].movement_promoted(self.game.board), capture)

    @parameterized.expand([
        ("white",
            [(0, 4), (1, 4), (2, 4), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7), (4, 8), (5, 4), (6, 4), (7, 4), (8, 4)],
            [(0, 4), (1, 4), (2, 4), (3, 4), (4, 3), (4, 5), (5, 4), (6, 4), (7, 4), (8, 4)],
            [(0, 4), (1, 4), (2, 4), (3, 4), (4, 2), (4, 3), (4, 5), (4, 6), (5, 4), (6, 4), (7, 4), (8, 4)]),
        ("black",
            [(0, 4), (1, 4), (2, 4), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7), (4, 8), (5, 4), (6, 4), (7, 4), (8, 4)],
            [(0, 4), (1, 4), (2, 4), (3, 4), (4, 3), (4, 5), (5, 4), (6, 4), (7, 4), (8, 4)],
            [(0, 4), (1, 4), (2, 4), (3, 4), (4, 2), (4, 3), (4, 5), (4, 6), (5, 4), (6, 4), (7, 4), (8, 4)]),
    ])
    def test_rook_moves_unpromoted(self, color, valid, obstacle, capture):
        self.game.board = self.sample_board
        self.game.board[4][4] = Rook(color, (4, 4))
        self.assertEqual(
            self.game.board[4][4].movement_unpromoted(self.game.board),
            valid)
        self.game.board[4][2] = self.game.board[4][6] = Pawn(color, (1, 1))
        self.assertEqual(
            self.game.board[4][4].movement_unpromoted(self.game.board),
            obstacle)
        self.game.board[4][2] = self.game.board[4][6] = Pawn("color", (1, 1))
        self.assertEqual(
            self.game.board[4][4].movement_unpromoted(self.game.board),
            capture)

    @parameterized.expand([
        ("white",
            [(0, 4), (1, 4), (2, 4), (3, 3), (3, 4), (3, 5), (4, 0), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7), (4, 8), (5, 3), (5, 4), (5, 5), (6, 4), (7, 4), (8, 4)],
            [(0, 4), (1, 4), (2, 4), (3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5), (6, 4), (7, 4), (8, 4)],
            [(0, 4), (1, 4), (2, 4), (3, 3), (3, 4), (3, 5), (4, 2), (4, 3), (4, 5), (4, 6), (5, 3), (5, 4), (5, 5), (6, 4), (7, 4), (8, 4)]),
        ("black",
            [(0, 4), (1, 4), (2, 4), (3, 3), (3, 4), (3, 5), (4, 0), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7), (4, 8), (5, 3), (5, 4), (5, 5), (6, 4), (7, 4), (8, 4)],
            [(0, 4), (1, 4), (2, 4), (3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5), (6, 4), (7, 4), (8, 4)],
            [(0, 4), (1, 4), (2, 4), (3, 3), (3, 4), (3, 5), (4, 2), (4, 3), (4, 5), (4, 6), (5, 3), (5, 4), (5, 5), (6, 4), (7, 4), (8, 4)]),
    ])
    def test_rook_moves_promoted(self, color, valid, obstacle, capture):
        self.game.board = self.sample_board
        self.game.board[4][4] = Rook(color, (4, 4))
        self.game.board[4][4].promote()
        self.assertEqual(
            self.game.board[4][4].movement_promoted(self.game.board),
            valid)
        self.game.board[4][2] = self.game.board[4][6] = Pawn(color, (1, 1))
        self.assertEqual(
            self.game.board[4][4].movement_promoted(self.game.board),
            obstacle)
        self.game.board[4][2] = self.game.board[4][6] = Pawn("color", (1, 1))
        self.assertEqual(
            self.game.board[4][4].movement_promoted(self.game.board),
            capture)

    @parameterized.expand([
        ("white",
            [(0, 0), (0, 8), (1, 1), (1, 7), (2, 2), (2, 6), (3, 3), (3, 5), (5, 3), (5, 5), (6, 2), (6, 6), (7, 1), (7, 7), (8, 0), (8, 8)],
            [(3, 3), (3, 5), (5, 3), (5, 5), (6, 2), (6, 6), (7, 1), (7, 7), (8, 0), (8, 8)],
            [(2, 2), (2, 6), (3, 3), (3, 5), (5, 3), (5, 5), (6, 2), (6, 6), (7, 1), (7, 7), (8, 0), (8, 8)],),
        ("black",
            [(0, 0), (0, 8), (1, 1), (1, 7), (2, 2), (2, 6), (3, 3), (3, 5), (5, 3), (5, 5), (6, 2), (6, 6), (7, 1), (7, 7), (8, 0), (8, 8)],
            [(3, 3), (3, 5), (5, 3), (5, 5), (6, 2), (6, 6), (7, 1), (7, 7), (8, 0), (8, 8)],
            [(2, 2), (2, 6), (3, 3), (3, 5), (5, 3), (5, 5), (6, 2), (6, 6), (7, 1), (7, 7), (8, 0), (8, 8)],),
    ])
    def test_bishop_moves_unpromoted(self, color, valid, obstacle, capture):
        self.game.board = self.sample_board
        self.game.board[4][4] = Bishop(color, (4, 4))
        self.assertEqual(
            self.game.board[4][4].movement_unpromoted(self.game.board),
            valid)
        self.game.board[2][2] = self.game.board[2][6] = Pawn(color, (1, 1))
        self.assertEqual(
            self.game.board[4][4].movement_unpromoted(self.game.board),
            obstacle)
        self.game.board[2][2] = self.game.board[2][6] = Pawn("color", (1, 1))
        self.assertEqual(
            self.game.board[4][4].movement_unpromoted(self.game.board),
            capture)

    @parameterized.expand([
        ("white",
            [(0, 0), (0, 8), (1, 1), (1, 7), (2, 2), (2, 6), (3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5), (6, 2), (6, 6), (7, 1), (7, 7), (8, 0), (8, 8)],
            [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5), (6, 2), (6, 6), (7, 1), (7, 7), (8, 0), (8, 8)],
            [(2, 2), (2, 6), (3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5), (6, 2), (6, 6), (7, 1), (7, 7), (8, 0), (8, 8)],),
        ("black",
            [(0, 0), (0, 8), (1, 1), (1, 7), (2, 2), (2, 6), (3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5), (6, 2), (6, 6), (7, 1), (7, 7), (8, 0), (8, 8)],
            [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5), (6, 2), (6, 6), (7, 1), (7, 7), (8, 0), (8, 8)],
            [(2, 2), (2, 6), (3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5), (6, 2), (6, 6), (7, 1), (7, 7), (8, 0), (8, 8)],),
    ])
    def test_bishop_moves_promoted(self, color, valid, obstacle, capture):
        self.game.board = self.sample_board
        self.game.board[4][4] = Bishop(color, (4, 4))
        self.game.board[4][4].promote()
        self.assertEqual(
            self.game.board[4][4].movement_promoted(self.game.board),
            valid)
        self.game.board[2][2] = self.game.board[2][6] = Pawn(color, (1, 1))
        self.assertEqual(
            self.game.board[4][4].movement_promoted(self.game.board),
            obstacle)
        self.game.board[2][2] = self.game.board[2][6] = Pawn("color", (1, 1))
        self.assertEqual(
            self.game.board[4][4].movement_promoted(self.game.board),
            capture)

    def test_valid_method(self):
        unpromoted_valid = [(3, 4)]
        promoted_valid = [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 4)]
        self.game.board = self.sample_board
        self.game.board[4][4] = Pawn("white", (4, 4))
        self.assertEqual(
            self.game.board[4][4].valid_moves(self.game.board),
            unpromoted_valid)
        self.game.board[4][4].promote()
        self.assertEqual(
            self.game.board[4][4].valid_moves(self.game.board),
            promoted_valid)

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
    def test_king_goldengeneral_never_set_for_promotion(self, color, coordinates):
        pieces = [King, GoldGeneral]
        row, col = coordinates
        self.game.board = self.sample_board
        for piece in pieces:
            self.game.board[4][4] = piece(color, (4, 4))
            self.assertFalse(self.game.board[4][4].set_for_promotion)
            self.game.board[4][4].update_position(row, col)
            self.assertFalse(self.game.board[4][4].set_for_promotion)

    @parameterized.expand([
        ("white",
            [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)], [(1, 0), (1, 1)]),
        ("black",
            [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)], [(0, 1), (1, 1)]),
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
        ("white",
            [[(3, 4), (2, 4), (1, 4), (0, 4)], [(3, 4)]],
            [[(4, 3), (4, 2), (4, 1), (4, 0)], [(4, 3), (4, 2)]],
            [[(4, 5), (4, 6), (4, 7), (4, 8)], [(4, 5)]],
            [[(5, 4), (6, 4), (7, 4), (8, 4)], [(5, 4), (6, 4)]],),
        ("black",
            [[(3, 4), (2, 4), (1, 4), (0, 4)], [(3, 4), (2, 4)]],
            [[(4, 3), (4, 2), (4, 1), (4, 0)], [(4, 3)]],
            [[(4, 5), (4, 6), (4, 7), (4, 8)], [(4, 5), (4, 6)]],
            [[(5, 4), (6, 4), (7, 4), (8, 4)], [(5, 4)]]),
    ])
    def test_filter_moves_rook_method(self, color, coords_n, coords_w, coords_e, coords_s):
        moves_n, filtered_moves_n = coords_n
        moves_w, filtered_moves_w = coords_w
        moves_e, filtered_moves_e = coords_e
        moves_s, filtered_moves_s = coords_s
        self.game.board = self.sample_board
        self.game.board[4][4] = Rook(color, (4, 4))
        self.game.board[2][4] = Pawn("white", (2, 4))
        self.game.board[4][2] = Pawn("black", (4, 2))
        self.game.board[4][6] = Pawn("white", (4, 6))
        self.game.board[6][4] = Pawn("black", (6, 4))
        self.assertEqual(self.game.board[4][4].filter_moves(moves_n, self.game.board), filtered_moves_n)
        self.assertEqual(self.game.board[4][4].filter_moves(moves_w, self.game.board), filtered_moves_w)
        self.assertEqual(self.game.board[4][4].filter_moves(moves_e, self.game.board), filtered_moves_e)
        self.assertEqual(self.game.board[4][4].filter_moves(moves_s, self.game.board), filtered_moves_s)

    @parameterized.expand([
        ("white",
            [[(3, 3), (2, 2), (1, 1), (0, 0)], [(3, 3)]],
            [[(3, 5), (2, 6), (1, 7), (0, 8)], [(3, 5), (2, 6)]],
            [[(5, 3), (6, 2), (7, 1), (8, 0)], [(5, 3)]],
            [[(5, 5), (6, 6), (7, 7), (8, 8)], [(5, 5), (6, 6)]]),
        ("black",
            [[(3, 3), (2, 2), (1, 1), (0, 0)], [(3, 3), (2, 2)]],
            [[(3, 5), (2, 6), (1, 7), (0, 8)], [(3, 5)]],
            [[(5, 3), (6, 2), (7, 1), (8, 0)], [(5, 3), (6, 2)]],
            [[(5, 5), (6, 6), (7, 7), (8, 8)], [(5, 5)]]),
    ])
    def test_filter_moves_bishop_method(self, color, coords_nw, coords_ne, coords_sw, coords_se):
        moves_nw, filtered_moves_nw = coords_nw
        moves_ne, filtered_moves_ne = coords_ne
        moves_sw, filtered_moves_sw = coords_sw
        moves_se, filtered_moves_se = coords_se
        self.game.board = self.sample_board
        self.game.board[4][4] = Bishop(color, (4, 4))
        self.game.board[2][2] = Pawn("white", (2, 4))
        self.game.board[2][6] = Pawn("black", (4, 2))
        self.game.board[6][2] = Pawn("white", (4, 6))
        self.game.board[6][6] = Pawn("black", (6, 4))
        self.assertEqual(self.game.board[4][4].filter_moves(moves_nw, self.game.board), filtered_moves_nw)
        self.assertEqual(self.game.board[4][4].filter_moves(moves_ne, self.game.board), filtered_moves_ne)
        self.assertEqual(self.game.board[4][4].filter_moves(moves_sw, self.game.board), filtered_moves_sw)
        self.assertEqual(self.game.board[4][4].filter_moves(moves_se, self.game.board), filtered_moves_se)

    @parameterized.expand([
        ("white", [(7, 0), (7, 8)]),
        ("black", [(1, 0), (1, 8)]),
    ])
    def test_valid_drops_G_R_method(self, color, invalid_spaces):
        pieces = [GoldGeneral, Rook]
        empty_spaces = [
                    (1, 0), (1, 2), (1, 3),  (1, 4), (1, 5), (1, 6), (1, 8),
                    (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8),
                    (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8),
                    (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8),
                    (7, 0), (7, 2), (7, 3),  (7, 4), (7, 5), (7, 6), (7, 8)]
        for space in invalid_spaces:
            empty_spaces.remove(space)
        for piece in pieces:
            current_piece = piece(color, (4, 4))
            self.assertEqual(current_piece.valid_drops(self.game.board), empty_spaces)

    @parameterized.expand([
        ("white", [(7, 0), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 8)]),
        ("black", [(1, 0), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 8)]),
    ])
    def test_valid_drops_L_S_method(self, color, invalid_spaces):
        pieces = [Lance, SilverGeneral]
        empty_spaces = [
                    (1, 0), (1, 2), (1, 3),  (1, 4), (1, 5), (1, 6), (1, 8),
                    (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8),
                    (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8),
                    (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8),
                    (7, 0), (7, 2), (7, 3),  (7, 4), (7, 5), (7, 6), (7, 8)]
        for space in invalid_spaces:
            empty_spaces.remove(space)
        for piece in pieces:
            current_piece = piece(color, (4, 4))
            self.assertEqual(current_piece.valid_drops(self.game.board), empty_spaces)

    @parameterized.expand([
        ("white", [(1, 0), (1, 2), (1, 3),  (1, 4), (1, 5), (1, 6), (1, 8)]),
        ("black", [(7, 0), (7, 2), (7, 3),  (7, 4), (7, 5), (7, 6), (7, 8)]),
    ])
    def test_valid_drops_N_method(self, color, invalid_spaces):
        piece = Knight(color, (4, 4))
        empty_spaces = [
                    (1, 0), (1, 2), (1, 3),  (1, 4), (1, 5), (1, 6), (1, 8),
                    (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8),
                    (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8),
                    (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8),
                    (7, 0), (7, 2), (7, 3),  (7, 4), (7, 5), (7, 6), (7, 8)]
        for space in invalid_spaces:
            empty_spaces.remove(space)
        self.assertEqual(piece.valid_drops(self.game.board), empty_spaces)

    @parameterized.expand([
        ("white", (1, 4)),
        ("black", (7, 4)),
    ])
    def test_valid_drops_P_method(self, color, front_of_king):
        piece = Pawn(color, (4, 4))
        self.game.board[6][4] = self.game.board[2][4] = "   "
        self.game.board[6][3] = self.game.board[2][3] = "   "
        valid_spaces = [
                    (1, 3),  (1, 4),
                    (2, 3),  (2, 4),
                    (3, 3), (3, 4),
                    (4, 3), (4, 4),
                    (5, 3), (5, 4),
                    (6, 3), (6, 4),
                    (7, 3), (7, 4)]
        valid_spaces.remove(front_of_king)
        self.assertEqual(piece.valid_drops(self.game.board), valid_spaces)

    @parameterized.expand([
        ("white", "black", (5 ,4)),
        ("black", "white", (3, 4)),
    ])
    def test_pawn_drop_rules_method(self, color, enemy_color, front_of_king):
        invalid_spaces = [(0, 3), (1, 3), (2, 3), (3, 3), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3)]
        invalid_spaces.append(front_of_king)
        self.game.board = self.sample_board
        self.game.board[4][3] = Pawn(color, (4, 3))
        self.game.board[4][4] = King(enemy_color, (4, 4))
        empty_spaces = []
        pawn = Pawn(color, (0, 0))
        for row in range(9):
            for col in range(9):
                if self.game.board[row][col] == "   ":
                    pawn.position = (row, col)
                    if len(pawn.movement_unpromoted(self.game.board)) > 0:
                        empty_spaces.append((row, col))
        for space in invalid_spaces:
            self.assertFalse(space in pawn.pawn_drop_rules(self.game.board, empty_spaces))

    def test_board_print_method(self):
        expected_screen = "\nCaptures-Black:\n \n9:\n\n   0   1   2   3   4   5   6   7   8  \n +-----------------------------------+\n"
        for i in range(9):
            expected_screen += f"{i}"
            for j in range(9):
                expected_screen += ("|" + str(self.game.board[i][j]))
            expected_screen += "|\n +---+---+---+---+---+---+---+---+---+\n"
        expected_screen += "\nCaptures-White:\n \n9:"
        self.assertEqual(self.game.board_print(), expected_screen)

    @parameterized.expand([
        ("white", [("6", "0"), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 7), (6, 8), (7, 7), (8, 0), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 8)]),
        ("black", [("2", "0"), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 7), (2, 8), (1, 1), (0, 0), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 8)]),
    ])
    def test_play_origin_method_valid(self, color, coords):
        self.game.playerturn = color
        for coord in coords:
            row, col = coord
            self.assertTrue(self.game.play_origin(row, col))
            self.assertEqual(self.game.error, "")

    @parameterized.expand([
        ("white", [(10, 0), (0, 10), ("h", 2), (6, "h"), (2, 0), (7, 1), (8, 1), (8, 7), (4, 4)]),
        ("black", [(10, 0), (0, 10), ("h", 2), (6, "h"), (6, 0), (1, 7), (0, 1), (0, 7), (4, 4)]),
    ])
    def test_play_origin_method_invalid(self, color, coords):
        self.game.playerturn = color
        for coord in coords:
            row, col = coord
            self.assertFalse(self.game.play_origin(row, col))

    @parameterized.expand([
        ("white", [("6", "0"), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 7), (6, 8), (7, 7), (8, 0), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 8), (9, 0)]),
        ("black", [("2", "0"), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 7), (2, 8), (1, 1), (0, 0), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 8), (9, 0)]),
    ])
    def test_validate_origin_coordinates_values_method_valid(self, color, coords):
        piece = Rook(color, (0, 0))
        piece.captured = True
        self.game.white_captures.append(piece)
        self.game.black_captures.append(piece)
        self.game.playerturn = color
        for coord in coords:
            row, col = coord
            self.assertTrue(self.game.validate_origin_coordinates_values(row, col))
            self.assertEqual(self.game.error, "")

    @parameterized.expand([
        ("white", [(10, 4), (4, 10), ("h", 2), (9, 0)]),
        ("black", [(10, 0), (0, 10), ("h", 2), (9, 0)]),
    ])
    def test_validate_origin_coordinates_values_method_invalid(self, color, coords):
        invalid_row, invalid_col, invalid_int, invalid_capture = coords
        self.game.playerturn = color
        self.assertFalse(self.game.validate_origin_coordinates_values(invalid_row[0], invalid_row[1]))
        self.assertEqual(self.game.error, "Row value is not between 0-9!")
        self.assertFalse(self.game.validate_origin_coordinates_values(invalid_col[0], invalid_col[1]))
        self.assertEqual(self.game.error, "Column Value is not between 0-8!")
        self.assertFalse(self.game.validate_origin_coordinates_values(invalid_int[0], invalid_int[1]))
        self.assertEqual(self.game.error, "Only Numbers are accepted, no letters or empty spaces!")
        self.assertFalse(self.game.validate_origin_coordinates_values(invalid_capture[0], invalid_capture[1]))
        self.assertEqual(self.game.error, "Column value invalid for current captures!")

    def test_current_player_captures_method(self):
        self.game.playerturn = "white"
        white_piece = Rook("white", (0, 0))
        self.game.white_captures.append(white_piece)
        self.assertEqual(self.game.current_player_captures(), [white_piece])
        self.game.playerturn = "black"
        black_piece = Bishop("black", (0, 0))
        self.game.black_captures.append(black_piece)
        self.assertEqual(self.game.current_player_captures(), [black_piece])

    @parameterized.expand([
        ("white", [(9, 0), (6, 4), (7, 7)]),
        ("black", [(9, 0), (2, 4), (1, 1)]),
    ])
    def test_validate_origin_coordinates_location_method_valid(self, color, coords):
        piece = Rook(color, (0, 0))
        piece.captured = True
        self.game.white_captures.append(piece)
        self.game.black_captures.append(piece)
        self.game.playerturn = color
        for coord in coords:
            row, col = coord
            self.assertTrue(self.game.validate_origin_coordinates_location(row, col))
            self.assertEqual(self.game.error, "")

    @parameterized.expand([
        ("white", [(9, 0), (4, 4), (7, 1), (2, 4)]),
        ("black", [(9, 0), (4, 4), (1, 7), (6, 4)]),
    ])
    def test_validate_origin_coordinates_location_method_invalid(self, color, coords):
        piece = Pawn(color, (0, 0))
        piece.captured = True
        self.game.white_captures.append(piece)
        self.game.black_captures.append(piece)
        self.game.playerturn = color
        cant_drop, empty_space, cant_move, enemy_piece = coords 
        self.assertFalse(self.game.validate_origin_coordinates_location(cant_drop[0], cant_drop[1]))
        self.assertEqual(self.game.error, "Cant drop this piece anywhere right now!")
        self.assertFalse(self.game.validate_origin_coordinates_location(empty_space[0], empty_space[1]))
        self.assertEqual(self.game.error, "Thats an empty space!")
        self.assertFalse(self.game.validate_origin_coordinates_location(cant_move[0], cant_move[1]))
        self.assertEqual(self.game.error, "You can't move that piece anywhere right now!")
        self.assertFalse(self.game.validate_origin_coordinates_location(enemy_piece[0], enemy_piece[1]))
        self.assertEqual(self.game.error, "Thats not one of your pieces!")
    
    @parameterized.expand([
        ("white", [(9, 0), (6, 4)], ),
        ("black", [(9, 0), (2, 4)]),
    ])
    def test_lift_piece_method(self, color, coords):
        piece = Rook(color, (9, 0))
        self.game.white_captures.append(piece)
        self.game.black_captures.append(piece)
        self.game.playerturn = color
        for coord in coords:
            row, col = coord
            self.game.lift_piece_for_movement(row, col)
            if row == 9:
                self.assertEqual(self.game.lifted_piece, piece)
            else:
                self.assertEqual(self.game.lifted_piece, self.game.board[row][col])
            self.assertEqual(self.game.lifted_piece_coordinates, (row, col))
    
    @parameterized.expand([
        ("white", [(5, 0), (5, 4), (5, 8), (7, 6), (7, 0), (7, 2), (7, 3), (7, 4), (7, 5), (7, 8)]),
        ("black", [(3, 0), (3, 4), (3, 8), (1, 2), (1, 0), (1, 3), (1, 4), (1, 5), (1, 6), (1, 8)]),
    ])
    def test_play_destination_method_valid(self, color, coords):
        for coord in coords:
            row, col = coord
            self.game.playerturn = color
            if color == "white":
                self.game.play_origin(row + 1, col)
            elif color == "black":
                self.game.play_origin(row - 1, col)
            self.assertTrue(self.game.play_destination(row, col))
            self.assertEqual(self.game.error, "")

    @parameterized.expand([
        ("white", [(10, 0), (0, 10), ("h", 2), (6, "h"), (0, 0)]),
        ("black", [(10, 0), (0, 10), ("h", 2), (6, "h"), (8, 8)]),
    ])
    def test_play_destination_method_invalid(self, color, coords):
        for coord in coords:
            row, col = coord
            self.game.playerturn = color
            if color == "white":
                self.game.play_origin(6, 4)
            elif color == "black":
                self.game.play_origin(2, 4)
            self.assertFalse(self.game.play_destination(row, col))

    @parameterized.expand([
        ("white", [(6, 4), (10, 0), (0, 10), ("h", 2), (0, 0), (7, 8)]),
        ("black", [(2, 4), (10, 0), (0, 10), ("h", 2), (8, 8), (1, 8)]),
    ])
    def test_validate_destination_coordinates_method(self, color, coords):
        piece = Rook(color, (9, 0))
        piece.captured = True
        self.game.white_captures.append(piece)
        self.game.black_captures.append(piece)
        self.game.playerturn = color
        origin, invalid_row, invalid_col, invalid_int, invalid_move, invalid_drop = coords
        self.game.play_origin(origin[0], origin[1])
        self.assertFalse(self.game.validate_destination_coordinates(invalid_row[0], invalid_row[1]))
        self.assertEqual(self.game.error, "Row value is not between 0-8!")
        self.assertFalse(self.game.validate_destination_coordinates(invalid_col[0], invalid_col[1]))
        self.assertEqual(self.game.error, "Column Value is not between 0-8!")
        self.assertFalse(self.game.validate_destination_coordinates(invalid_int[0], invalid_int[1]))
        self.assertEqual(self.game.error, "Only Numbers are accepted, no letters or empty spaces!")
        self.assertFalse(self.game.validate_destination_coordinates(invalid_move[0], invalid_move[1]))
        self.assertEqual(self.game.error, "That's not a valid movement!")
        self.game.play_origin(9, 0)
        self.assertFalse(self.game.validate_destination_coordinates(invalid_drop[0], invalid_drop[1]))
        self.assertEqual(self.game.error, "You cant drop this Piece there!")

    @parameterized.expand([
        ("white", (6, 4), (5, 4)),
        ("black", (2, 4), (3, 4)),
    ])
    def test_move_piece_method(self, color, origin, destination):
        self.game.playerturn = color
        row_o, col_o = origin
        row_d, col_d = destination
        self.game.play_origin(origin[0], origin[1])
        self.assertEqual(self.game.board[row_o][col_o].position, (row_o, col_o))
        self.assertEqual(self.game.board[row_o][col_o], self.game.lifted_piece)
        self.assertEqual(self.game.lifted_piece_coordinates, (row_o, col_o))
        self.game.move_piece(row_d, col_d)
        self.assertEqual(self.game.board[row_d][col_d], self.game.board[row_o][col_o])
        self.assertEqual(self.game.lifted_piece, "No piece lifted")
        self.assertEqual(self.game.board[row_d][col_d].position, (row_d, col_d))

    @parameterized.expand([
        ("white", [(2, 4), (0, 0), (1, 7)], (0, 4)),
        ("black", [(6, 4), (8, 0), (7, 1)], (8, 4)),
    ])
    def test_capture_piece_method(self, color, coords, king):
        for coord in coords:
            row, col = coord
            self.game.playerturn = color
            self.game.capture_piece(row, col)
            self.assertEqual(self.game.board[row][col].color, color)
            self.assertTrue(self.game.board[row][col].captured)
            self.assertFalse(self.game.board[row][col].promoted)
            if color == "white":
                self.assertTrue(self.game.board[row][col] in self.game.white_captures)
            elif color == "black":
                self.assertTrue(self.game.board[row][col] in self.game.black_captures)
            self.assertTrue(self.game.is_playing)
        self.game.capture_piece(king[0], king[1])
        self.assertFalse(self.game.is_playing)
    
    @parameterized.expand([
        ("white", [(6, 4), (7, 7), (8, 3)]),
        ("black", [(2, 4), (1, 1), (0, 3)]),
    ])
    def test_clean_lifted_piece_origin_location_method(self, color, coords):
        piece = Rook(color, (9, 0))
        piece.captured = True
        self.game.playerturn = color
        self.game.current_player_captures().append(piece)
        for coord in coords:
            row, col = coord
            self.game.playerturn = color
            self.game.play_origin(row, col)
            self.assertEqual(self.game.board[row][col], self.game.lifted_piece)
            self.assertEqual(self.game.board[row][col].position, self.game.lifted_piece_coordinates)
            self.game.clean_lifted_piece_origin_location()
            self.assertEqual(self.game.board[row][col], "   ")
            self.assertEqual(self.game.lifted_piece_coordinates, ("", ""))
        self.game.play_origin(9, 0)
        self.assertEqual(piece, self.game.lifted_piece)
        self.assertEqual((9, 0), self.game.lifted_piece_coordinates)
        self.assertTrue(piece in self.game.current_player_captures())
        self.game.clean_lifted_piece_origin_location()
        self.assertEqual(("", ""), self.game.lifted_piece_coordinates)
        self.assertFalse(piece in self.game.current_player_captures())

    @parameterized.expand([
        ("white", "black"),
        ("black", "white"),
    ])
    def test_next_turn_method(self, current_player, next_player):
        self.game.playerturn = current_player
        self.game.next_turn()
        self.assertEqual(self.game.playerturn, next_player)


if __name__ == "__main__":
    unittest.main()