import unittest
import unittest.mock
from parameterized import parameterized
from shogi import Shogi, Piece, Pawn, Lance, Knight, SilverGeneral, GoldGeneral, King, Bishop, Rook
from interface_shogi import Interface


class TestInterface(unittest.TestCase):
    
    def setUp(self):
        self.interface = Interface()
    
    def test_set_interface(self):
        self.assertEqual(self.interface.game.__class__.__name__, "Shogi")
        self.assertEqual(self.interface.turn_count, 0)

    def test_print_board(self):
        screen = self.interface.game.board_print()
        if self.interface.game.playerturn == "white":
            screen += f"\n========= #{self.interface.turn_count} {self.interface.game.playerturn}(\u039b) Turn =========\n".title()
        elif self.interface.game.playerturn == "black":
            screen += f"\n========= #{self.interface.turn_count} {self.interface.game.playerturn}(V) Turn =========\n".title()
        self.assertEqual(self.interface.print_board(), screen)
    

    @unittest.mock.patch("builtins.input", side_effect=["6", "4", "2", "4"])
    def test_input_origin_coordinates(self, mock):
        self.interface.game.playerturn = "white"
        self.interface.input_origin_coordinates()
        self.assertEqual(self.interface.game.lifted_piece.name, "P")
        self.assertEqual(self.interface.game.lifted_piece.color, "white")
        self.assertEqual(self.interface.game.lifted_piece_coordinates, (6, 4))
        self.interface.game.playerturn = "black"
        self.interface.input_origin_coordinates()
        self.assertEqual(self.interface.game.lifted_piece.name, "P")
        self.assertEqual(self.interface.game.lifted_piece.color, "black")
        self.assertEqual(self.interface.game.lifted_piece_coordinates, (2, 4))
    
    @unittest.mock.patch("builtins.input", side_effect=["5", "4", "3", "4"])
    def test_input_destiny_coordinates(self, mock):
        self.interface.game.playerturn = "white"
        self.interface.game.play_origin(6, 4)
        self.interface.input_destiny_coordinates()
        self.assertEqual(self.interface.game.lifted_piece, "No piece lifted")
        self.assertEqual(self.interface.game.lifted_piece_coordinates, ("", ""))
        self.interface.game.playerturn = "black"
        self.interface.game.play_origin(2, 4)
        self.interface.input_destiny_coordinates()
        self.assertEqual(self.interface.game.lifted_piece, "No piece lifted")
        self.assertEqual(self.interface.game.lifted_piece_coordinates, ("", ""))
    
    @unittest.mock.patch("builtins.input", side_effect=["2", "4", "y"])
    def test_input_destiny_coordinates_ask_to_promote(self, mock):
        piece = Pawn("white", (3, 4))
        self.interface.game.board[3][4] = piece
        self.interface.game.playerturn = "white"
        self.assertFalse(self.interface.game.board[3][4].promoted)
        self.interface.game.play_origin(3, 4)
        self.assertEqual(self.interface.game.lifted_piece, piece)
        self.interface.input_destiny_coordinates()
        self.assertTrue(self.interface.game.board[2][4].promoted)
        self.assertEqual(self.interface.game.board[2][4], piece)

    @unittest.mock.patch("builtins.input", side_effect=["0", "3"])
    def test_input_destiny_coordinates_forced_promotion(self, mock):
        piece = Pawn("white", (1, 3))
        self.interface.game.board[1][3] = piece
        self.interface.game.playerturn = "white"
        self.assertFalse(self.interface.game.board[1][3].promoted)
        self.interface.game.play_origin(1, 3)
        self.assertEqual(self.interface.game.lifted_piece, piece)
        self.interface.input_destiny_coordinates()
        self.assertTrue(self.interface.game.board[0][3].promoted)
        self.assertEqual(self.interface.game.board[0][3], piece)

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
        self.interface.start_playing()
        self.assertEqual(self.interface.turn_count, 5)

        



#def start_playing(self):

#def input_origin_coordinates(self):

#def input_destiny_coordinates(self):

#def print_board(self):












if __name__ == "__main__":
    unittest.main()