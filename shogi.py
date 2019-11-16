class Shogi():

    def __init__(self):
        self.board = [] 
        self.set_board()

        self.white_captures = []
        self.black_captures = []

        self.lifted_piece = 0
        self.lifted_piece_coordinates = ("", "")
        self.is_playing = True
        self.playerturn = "white"
        self.error = ""

        self.pruebita = [0, 0, 0, 0, 0]

    def board_print(self):
        screen = "\nCaptures-Black:\n "
        for column in range(len(self.black_captures)):
            screen += f"  {column} "
        screen += "\n9:"
        for piece in range(len(self.black_captures)):
            screen += f"{self.black_captures[piece]} "
        screen += "\n\n   0   1   2   3   4   5   6   7   8  "
        screen += "\n +-----------------------------------+\n"
        for i in range(9):
            screen += f"{i}"
            for j in range(9):
                screen += ("|" + str(self.board[i][j]))
            screen += "|\n +---+---+---+---+---+---+---+---+---+\n"
        screen += "\nCaptures-White:\n "
        for column in range(len(self.white_captures)):
            screen += f"  {column} "
        screen += "\n9:"
        for piece in range(len(self.white_captures)):
            screen += f"{self.white_captures[piece]} "
        return screen

    def set_board(self):
        self.board = []
        for row in range(9):
            self.board.append([])
            for column in range(9):
                self.board[row].append("   ")
        self.place_pieces()

    def place_pieces(self):
        row_first, row_second, row_pawn = (0, 1, 2)
        first_row_pieces = [Lance, Knight, SilverGeneral, GoldGeneral, King, GoldGeneral, SilverGeneral, Knight, Lance]
        for color in ["black", "white"]:
            for column in range(9):
                self.board[row_pawn][column] = Pawn(color, (row_pawn, column))
                self.board[row_first][column] = first_row_pieces[column](color, (row_first, column))
            if color == "black":
                self.board[row_second][1], self.board[row_second][7] = (Rook(color, (row_second, 1)), Bishop(color, (row_second, 7)))
            else:
                self.board[row_second][1], self.board[row_second][7] = (Bishop(color, (row_second, 1)), Rook(color, (row_second, 7)))
            row_first, row_second, row_pawn = (8, 7, 6)

    def play_origin(self, row, column):
        self.error = ""
        if self.validate_origin_coordinates_values(row, column):
            if self.validate_origin_coordinates_location(int(row), int(column)):
                self.lift_piece_for_movement(int(row), int(column))
                return True
        else:
            return False

    def validate_origin_coordinates_values(self, row, column):
        try:
            row = int(row)
            column = int(column)
        except:
            self.error = "Only Numbers are accepted, no letters or empty spaces!"
            return False
        if row < 0 or row > 9:
            self.error = "Row value is not between 0-9!"
            return False
        if (column < 0 or column > 8) and row < 9:
            self.error = "Column Value is not between 0-8!"
            return False
        if row == 9 and column > len(self.current_player_captures()) - 1:
            self.error = "Column value invalid for current captures!"
            return False
        return True

    def current_player_captures(self):
        if self.playerturn == "white":
            return self.white_captures
        elif self.playerturn == "black":
            return self.black_captures

    def validate_origin_coordinates_location(self, row, column):
        if row == 9 and len(self.current_player_captures()[column].valid_drops(self.board)) < 1:
            self.error = "Cant drop this piece anywhere right now!"
            return False
        elif row == 9 and len(self.current_player_captures()[column].valid_drops(self.board)) > 0:
            return True
        if self.board[row][column] == "   ":
            self.error = "Thats an empty space!"
            return False
        if row < 9 and self.playerturn != self.board[row][column].color:
            self.error = "Thats not one of your pieces!"
            return False
        if len(self.board[row][column].valid_moves(self.board)) < 1:
            self.error = "You can't move that piece anywhere right now!"
            return False
        return True

    def lift_piece_for_movement(self, row, column):
        if row == 9:
            self.lifted_piece = self.current_player_captures()[column]
        else:
            self.lifted_piece = self.board[row][column]
        self.lifted_piece_coordinates = (row, column)

    def play_destination(self, row, column):
        self.error = ""
        if self.validate_destination_coordinates(row, column):
            self.move_piece(int(row), int(column))
            self.clean_lifted_piece_origin_location()
            if self.is_playing:
                #self.next_turn()
                pass
            return True
        return False

    def validate_destination_coordinates(self, row, column):
        try:
            row = int(row)
            column = int(column)
        except:
            self.error = "Only Numbers are accepted, no letters or empty spaces!"
            return False
        if row < 0 or row > 8:
            self.error = "Row value is not between 0-8!"
            return False
        if column < 0 or column > 8:
            self.error = "Column Value is not between 0-8!"
            return False
        if self.lifted_piece_coordinates[0] == 9:
            if (row, column) not in self.lifted_piece.valid_drops(self.board):
                self.error = "You cant drop this Piece there!"
                return False
            elif (row, column) in self.lifted_piece.valid_drops(self.board):
                return True
        if (row, column) not in self.lifted_piece.valid_moves(self.board):
            self.error = "That's not a valid movement!"
            return False
        return True

    def move_piece(self, row, column):
        if self.board[row][column] != "   ":
            self.board[row][column].promoted = False
            self.board[row][column].captured = True
            if self.playerturn == "white":
                self.board[row][column].color = "white"
                self.white_captures.append(self.board[row][column])
            elif self.playerturn == "black":
                self.board[row][column].color = "black"
                self.black_captures.append(self.board[row][column])
            if self.board[row][column].__class__.__name__ == "King":
                self.is_playing = False
        self.board[row][column] = self.lifted_piece
        self.board[row][column].update_position(row, column)
        self.lifted_piece = 0

    def clean_lifted_piece_origin_location(self):
        row, col = self.lifted_piece_coordinates
        if row == 9:
            del self.current_player_captures()[col]
        else:
            self.board[row][col] = "   "

    def next_turn(self):
        if self.playerturn == "white":
            self.playerturn = "black"
        else:
            self.playerturn = "white"

##########################################################################################
##########################################################################################
##########################################################################################

class Piece():
    def __init__(self, name, color, position):
        self.name = name
        self.color = color
        self.position = position
        self.promoted = False
        self.captured = False
        self.set_for_promotion = False

    def __repr__(self):
        promoted = ""
        if self.promoted == True:
            promoted += "+"
        else:
            promoted += " "
        if self.color == "white":
            return promoted + self.name + "\u2227"
        elif self.color == "black":
            return promoted + self.name + "\u2228"
        else:
            # This is only for testing
            return "-T*"

    def valid_moves(self, board):
        if self.promoted == False:
            print(f"Quantity of unpromoted valid moves: {self.movement_unpromoted(board)}")
            return self.movement_unpromoted(board)
        elif self.promoted == True:
            print(f"Quantity of promoted valid moves: {self.movement_promoted(board)}")
            return self.movement_promoted(board)
        return False

    def movement_unpromoted(self, board):
        return

    def movement_promoted(self, board):
        coordinates = [
            (self.position[0], self.position[1] - 1),
            (self.position[0], self.position[1] + 1),
            (self.position[0] - 1, self.position[1]),
            (self.position[0] + 1, self.position[1]),
        ]
        if self.color == "white":
            coordinates.append((self.position[0] - 1, self.position[1] - 1))
            coordinates.append((self.position[0] - 1, self.position[1] + 1))
        elif self.color == "black":
            coordinates.append((self.position[0] + 1, self.position[1] - 1))
            coordinates.append((self.position[0] + 1, self.position[1] + 1))
        return sorted(self.filter_moves(coordinates, board))

    def filter_moves(self, coordinates, board):
        filtered_moves = []
        for space in coordinates:
            row, column = space
            if row < 0 or row > 8 or column < 0 or column > 8:
                pass
            elif board[row][column] == "   ":
                filtered_moves.append(space)
            elif board[row][column].color != self.color:
                filtered_moves.append(space)
        return filtered_moves

    def promote(self):  # Cambiar self.promoted
        self.promoted = True
        self.set_for_promotion = False

    def update_position(self, row, column):
        self.position = (row, column)
        if not self.captured:
            if self.color == "white" and self.position[0] < 3 and not self.promoted:
                self.set_for_promotion = True
            elif self.color == "black" and 5 < self.position[0] < 9 and not self.promoted:
                self.set_for_promotion = True
        else:
            self.captured = False
            self.set_for_promotion = False

    #def valid_drops(self, board):
    #    return self.valid_drop_locations(board)

    def valid_drops(self, board):  # Terminar de proliijar, falta que tenga en cuenta las reglas
        empty_spaces = []                   # no se puede poner una ficha en un lugar q no se pueda mover
        valid_locations = []
        for row in range(9):                # tener en cuenta para PEON LANCE y KNIGHT
            for col in range(9):            # PEON no puede jaquear
                if board[row][col] == "   ":
                    empty_spaces.append((row, col))
        for coords in empty_spaces:
            self.position = coords
            if len(self.movement_unpromoted(board)) > 0:
                valid_locations.append(coords)
        return valid_locations
    
class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__("P", color, position)
    
    def movement_unpromoted(self, board):
        coordinates = []
        if self.color == "white":
            coordinates.append((self.position[0] - 1, self.position[1]))
        if self.color == "black":
            coordinates.append((self.position[0] + 1, self.position[1]))
        return self.filter_moves(coordinates, board)

    def valid_drops(self, board):  # Terminar de proliijar, falta que tenga en cuenta las reglas
        empty_spaces = []                   # no se puede poner una ficha en un lugar q no se pueda mover
        valid_locations = []
        for row in range(9):                # tener en cuenta para PEON LANCE y KNIGHT
            for col in range(9):            # PEON no puede jaquear
                if board[row][col] == "   ":
                    empty_spaces.append((row, col))
        for coords in empty_spaces:
            self.position = coords
            if len(self.movement_unpromoted(board)) > 0:
                valid_locations.append(coords)
        return self.pawn_drop_rules(board, valid_locations)
    
    def pawn_drop_rules(self, board, valid_locations):
        for row in range(9):
            for col in range(9):
                if board[row][col] != "   ":
                    if board[row][col].name == "P" and board[row][col].color == self.color:
                        if not board[row][col].promoted:
                            for coords in valid_locations:
                                if coords[1] == col:
                                    valid_locations.remove(coords)
                    if board[row][col].name == "K" and board[row][col].color != self.color:
                        if self.color == "white" and (row + 1, col) in valid_locations:
                            valid_locations.remove((row + 1, col))
                        elif self.color == "black" and (row + 1, col) in valid_locations:
                            valid_locations.remove((row + 1, col))
        return valid_locations
    
    def update_position(self, row, column):
        self.position = (row, column)
        if not self.captured:
            if self.color == "white" and self.position[0] < 3 and not self.promoted:
                if self.position[0] == 0:
                    self.promote()
                    self.set_for_promotion = False
                else:
                    self.set_for_promotion = True
            elif self.color == "black" and 5 < self.position[0] < 9 and not self.promoted:
                if self.position[0] == 8:
                    self.promote()
                    self.set_for_promotion = False
                else:
                    self.set_for_promotion = True
        else:
            self.captured = False
            self.set_for_promotion = False

class Lance(Piece):
    def __init__(self, color, position):
        super().__init__("L", color, position)
    
    def movement_unpromoted(self, board):
        coordinates = []
        current_row = self.position[0]
        if self.color == "white":
            current_row -= 1
            while current_row >= 0:
                coordinates.append((current_row, self.position[1]))
                current_row -= 1
        if self.color == "black":
            current_row += 1
            while current_row <= 8:
                coordinates.append((current_row, self.position[1]))
                current_row += 1
        return self.filter_moves(coordinates, board)
    
    def filter_moves(self, coordinates, board):
        filtered_moves = []
        for space in coordinates:
            row, column = space
            if row < 0 or row > 8 or column < 0 or column > 8:
                pass
            elif board[row][column] == "   ":
                filtered_moves.append(space)
            elif board[row][column].color != self.color:
                filtered_moves.append(space)
                if not self.promoted:
                    break
            elif not self.promoted:
                break
        return sorted(filtered_moves)

    def update_position(self, row, column):
        self.position = (row, column)
        if not self.captured:
            if self.color == "white" and self.position[0] < 3 and not self.promoted:
                if self.position[0] == 0:
                    self.promote()
                    self.set_for_promotion = False
                else:
                    self.set_for_promotion = True
            elif self.color == "black" and 5 < self.position[0] < 9 and not self.promoted:
                if self.position[0] == 8:
                    self.promote()
                    self.set_for_promotion = False
                else:
                    self.set_for_promotion = True
        else:
            self.captured = False
            self.set_for_promotion = False

class Knight(Piece):
    def __init__(self, color, position):
        super().__init__("N", color, position)
    
    def movement_unpromoted(self, board):
        coordinates = []
        if self.color == "white":
            coordinates.append((self.position[0] - 2, self.position[1] - 1))
            coordinates.append((self.position[0] - 2, self.position[1] + 1))
        elif self.color == "black":
            coordinates.append((self.position[0] + 2, self.position[1] - 1))
            coordinates.append((self.position[0] + 2, self.position[1] + 1))
        return sorted(self.filter_moves(coordinates, board))

    def update_position(self, row, column):
        self.position = (row, column)
        if not self.captured:
            if self.color == "white" and self.position[0] < 3 and not self.promoted:
                if self.position[0] == 0 or self.position[0] == 1:
                    self.promote()
                    self.set_for_promotion = False
                else:
                    self.set_for_promotion = True
            elif self.color == "black" and 5 < self.position[0] < 9 and not self.promoted:
                if self.position[0] == 8 or self.position[0] == 7:
                    self.promote()
                    self.set_for_promotion = False
                else:
                    self.set_for_promotion = True
        else:
            self.captured = False
            self.set_for_promotion = False

class SilverGeneral(Piece):
    def __init__(self, color, position):
        super().__init__("S", color, position)

    def movement_unpromoted(self, board):
        coordinates = [
            (self.position[0] - 1, self.position[1] - 1),
            (self.position[0] - 1, self.position[1] + 1),
            (self.position[0] + 1, self.position[1] - 1),
            (self.position[0] + 1, self.position[1] + 1),
        ]
        if self.color == "white":
            coordinates.append((self.position[0] - 1, self.position[1]))
        elif self.color == "black":
            coordinates.append((self.position[0] + 1, self.position[1]))
        return sorted(self.filter_moves(coordinates, board))

class GoldGeneral(Piece):
    def __init__(self, color, position):
        super().__init__("G", color, position)

    def movement_unpromoted(self, board):
        return self.movement_promoted(board)

    def promote(self):
        self.promoted = False

    def update_position(self, row, column):
        self.position = (row, column)
        self.captured = False
        self.set_for_promotion = False

class King(Piece):
    def __init__(self, color, position):
        super().__init__("K", color, position)

    def movement_unpromoted(self, board):
        coordinates = [
            (self.position[0] - 1, self.position[1] - 1),
            (self.position[0] - 1, self.position[1]),
            (self.position[0] - 1, self.position[1] + 1),
            (self.position[0], self.position[1] + 1),
            (self.position[0], self.position[1] - 1),
            (self.position[0] + 1, self.position[1] - 1),
            (self.position[0] + 1, self.position[1]),
            (self.position[0] + 1, self.position[1] + 1),
        ]
        return sorted(self.filter_moves(coordinates, board))

    def movement_promoted(self, board):
        return self.movement_unpromoted(board)

    def promote(self):
        self.promoted = False

    def update_position(self, row, column):
        self.position = (row, column)
        self.captured = False
        self.set_for_promotion = False

class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__("B", color, position)

    def movement_unpromoted(self, board):
        coordinates_nw = []
        coordinates_ne = []
        coordinates_sw = []
        coordinates_se = []
        coordinates_final = []
        for value in range(1, 9):
            coordinates_nw.append((self.position[0] - value, self.position[1] - value))
            coordinates_ne.append((self.position[0] - value, self.position[1] + value))
            coordinates_sw.append((self.position[0] + value, self.position[1] - value))
            coordinates_se.append((self.position[0] + value, self.position[1] + value))
        coordinates_final += self.filter_moves(coordinates_nw, board)
        coordinates_final += self.filter_moves(coordinates_ne, board)
        coordinates_final += self.filter_moves(coordinates_sw, board)
        coordinates_final += self.filter_moves(coordinates_se, board)
        return sorted(coordinates_final)

    def movement_promoted(self, board):
        coordinates = []
        coordinates += self.filter_moves([(self.position[0] + 1, self.position[1])], board)
        coordinates += self.filter_moves([(self.position[0] - 1, self.position[1])], board)
        coordinates += self.filter_moves([(self.position[0], self.position[1] - 1)], board)
        coordinates += self.filter_moves([(self.position[0], self.position[1] + 1)], board)
        coordinates += self.movement_unpromoted(board)
        return sorted(coordinates)

    def filter_moves(self, coordinates, board):
        filtered_moves = []
        for space in coordinates:
            row, column = space
            if row < 0 or row > 8 or column < 0 or column > 8:
                pass
            elif board[row][column] == "   ":
                filtered_moves.append(space)
            elif board[row][column].color != self.color:
                filtered_moves.append(space)
                break
            else:
                break
        return filtered_moves

class Rook(Piece):
    def __init__(self, color, position):
        super().__init__("R", color, position)

    def movement_unpromoted(self, board):
        coordinates_up = []
        coordinates_down = []
        coordinates_left = []
        coordinates_right = []
        coordinates_final = []
        for value in range(1, 9):
            coordinates_down.append((self.position[0] + value, self.position[1]))
            coordinates_up.append((self.position[0] - value, self.position[1]))
            coordinates_right.append((self.position[0], self.position[1] + value))
            coordinates_left.append((self.position[0], self.position[1] - value))
        coordinates_final += self.filter_moves(coordinates_up, board)
        coordinates_final += self.filter_moves(coordinates_down, board)
        coordinates_final += self.filter_moves(coordinates_left, board)
        coordinates_final += self.filter_moves(coordinates_right, board)
        return sorted(coordinates_final)
    
    def movement_promoted(self, board):
        coordinates = []
        coordinates += self.filter_moves([(self.position[0] + 1, self.position[1] + 1)], board)
        coordinates += self.filter_moves([(self.position[0] - 1, self.position[1] - 1)], board)
        coordinates += self.filter_moves([(self.position[0] + 1, self.position[1] - 1)], board)
        coordinates += self.filter_moves([(self.position[0] - 1, self.position[1] + 1)], board)
        coordinates += self.movement_unpromoted(board)
        return sorted(coordinates)
    
    def filter_moves(self, coordinates, board):
        filtered_moves = []
        for space in coordinates:
            row, column = space
            if row < 0 or row > 8 or column < 0 or column > 8:
                pass
            elif board[row][column] == "   ":
                filtered_moves.append(space)
            elif board[row][column].color != self.color:
                filtered_moves.append(space)
                break
            else:
                break
        return filtered_moves

