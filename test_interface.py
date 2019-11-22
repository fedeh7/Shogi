import unittest
import unittest.mock
from parameterized import parameterized
from shogi import Shogi, Pawn
from interface_shogi import Interface


class TestInterface(unittest.TestCase):

    def setUp(self):
        self.play = Interface()

    def test_set_interface(self):
        self.assertTrue(isinstance(self.play.game, Shogi))
        self.assertEqual(self.play.turn_count, 0)

    def test_print_board(self):
        screen = self.play.game.board_print()
        symbol = ""
        if self.play.game.playerturn == "white":
            symbol = "(\u039b)"
        elif self.play.game.playerturn == "black":
            symbol = "(V)"
        turn_indicator = (
            f"\n======== #{self.play.turn_count} "
            f"{self.play.game.playerturn}{symbol} Turn ========\n".title())
        screen += turn_indicator
        self.assertEqual(self.play.print_board(), screen)

    @unittest.mock.patch("builtins.input", side_effect=["6", "4", "2", "4"])
    def test_input_origin_coordinates(self, mock):
        self.play.game.playerturn = "white"
        self.play.input_origin_coordinates()
        self.assertEqual(self.play.game.lifted_piece.name, "P")
        self.assertEqual(self.play.game.lifted_piece.color, "white")
        self.assertEqual(self.play.game.lifted_piece_coordinates, (6, 4))
        self.play.game.playerturn = "black"
        self.play.input_origin_coordinates()
        self.assertEqual(self.play.game.lifted_piece.name, "P")
        self.assertEqual(self.play.game.lifted_piece.color, "black")
        self.assertEqual(self.play.game.lifted_piece_coordinates, (2, 4))

    @unittest.mock.patch("builtins.input", side_effect=["5", "4", "3", "4"])
    def test_input_destiny_coordinates(self, mock):
        self.play.game.playerturn = "white"
        self.play.game.play_origin(6, 4)
        self.play.input_destiny_coordinates()
        self.assertEqual(self.play.game.lifted_piece, "No piece lifted")
        self.assertEqual(self.play.game.lifted_piece_coordinates, ("", ""))
        self.play.game.playerturn = "black"
        self.play.game.play_origin(2, 4)
        self.play.input_destiny_coordinates()
        self.assertEqual(self.play.game.lifted_piece, "No piece lifted")
        self.assertEqual(self.play.game.lifted_piece_coordinates, ("", ""))

    @unittest.mock.patch("builtins.input", side_effect=["2", "4", "y"])
    def test_input_destiny_coordinates_ask_to_promote(self, mock):
        piece = Pawn("white", (3, 4))
        self.play.game.board[3][4] = piece
        self.play.game.playerturn = "white"
        self.assertFalse(self.play.game.board[3][4].promoted)
        self.play.game.play_origin(3, 4)
        self.assertEqual(self.play.game.lifted_piece, piece)
        self.play.input_destiny_coordinates()
        self.assertTrue(self.play.game.board[2][4].promoted)
        self.assertEqual(self.play.game.board[2][4], piece)

    @unittest.mock.patch("builtins.input", side_effect=["0", "3"])
    def test_input_destiny_coordinates_forced_promotion(self, mock):
        piece = Pawn("white", (1, 3))
        self.play.game.board[1][3] = piece
        self.play.game.playerturn = "white"
        self.assertFalse(self.play.game.board[1][3].promoted)
        self.play.game.play_origin(1, 3)
        self.assertEqual(self.play.game.lifted_piece, piece)
        self.play.input_destiny_coordinates()
        self.assertTrue(self.play.game.board[0][3].promoted)
        self.assertEqual(self.play.game.board[0][3], piece)

    @unittest.mock.patch(
        "builtins.input",
        side_effect=[
            "6", "2", "5", "2",
            "2", "0", "3", "0",
            "7", "1", "2", "6", "y",
            "3", "0", "4", "0",
            "2", "6", "0", "4"
            ])
    def test_start_playing_white_wins(self, mock):
        self.play.start_playing()
        self.assertEqual(self.play.turn_count, 5)
        self.assertFalse(self.play.game.is_playing)

    @unittest.mock.patch(
        "builtins.input",
        side_effect=[
            "6", "0", "5", "0",
            "2", "6", "3", "6",
            "5", "0", "4", "0",
            "1", "7", "6", "2", "y",
            "4", "0", "3", "0",
            "6", "2", "8", "4",
            ])
    def test_start_playing_black_wins(self, mock):
        self.play.start_playing()
        self.assertEqual(self.play.turn_count, 6)
        self.assertFalse(self.play.game.is_playing)

if __name__ == "__main__":
    unittest.main()
