class Shogi():

    def __init__(self):
        self.board = [] 
        self.set_board()

        self.white_captures = []
        self.black_captures = []

        self.lifted_piece = "No piece lifted"
        self.lifted_piece_coordinates = ("", "")
        self.is_playing = True
        self.playerturn = "white"
        self.error = ""

        self.pruebita = [0, 0, 0, 0, 0]

    # Devuelve un string con el tablero y las capturas
    def board_print(self):
        screen = "\nCaptures-Black:\n "
        for col in range(len(self.black_captures)):
            screen += f"  {col} "
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
        for col in range(len(self.white_captures)):
            screen += f"  {col} "
        screen += "\n9:"
        for piece in range(len(self.white_captures)):
            screen += f"{self.white_captures[piece]} "
        return screen

    # Prepara el tablero vacio
    # Luego ejecuta place_pieces para poblarlo con las piezas iniciales
    def set_board(self):
        self.board = []
        for row in range(9):
            self.board.append([])
            for col in range(9):
                self.board[row].append("   ")
        self.place_pieces()

    # Puebla el tablero inicial con las piezas de ambos jugadores
    def place_pieces(self):
        row_1, row_2, row_3 = (0, 1, 2)
        pieces = [
            Lance, Knight, SilverGeneral, GoldGeneral,
            King, GoldGeneral, SilverGeneral, Knight, Lance]
        for color in ["black", "white"]:
            for col in range(9):
                self.board[row_3][col] = Pawn(color, (row_3, col))
                self.board[row_1][col] = pieces[col](color, (row_1, col))
            if color == "black":
                self.board[row_2][1] = Rook(color, (row_2, 1))
                self.board[row_2][7] = Bishop(color, (row_2, 7))
            else:
                self.board[row_2][1] = Bishop(color, (row_2, 1))
                self.board[row_2][7] = Rook(color, (row_2, 7))
            row_1, row_2, row_3 = (8, 7, 6)

    # Se ejecuta cuando se elige la pieza que se quiere mover
    # Verifica que los valores de fila y columna sean validos
    # Y que el lugar que se eligio contenga una pieza del color del jugador
    # Si la pieza tiene movimientos posibles o puede ser reintroducida
    # Levanta la pieza con lift_piece_for_movement
    def play_origin(self, row, col):
        self.error = ""
        if self.validate_origin_coordinates_values(row, col):
            row, col = int(row), int(col)
            if self.validate_origin_coordinates_location(row, col):
                self.lift_piece_for_movement(row, col)
                return True
        else:
            return False

    # Verifica que los valores de fila y columna de play_origin sean validos
    def validate_origin_coordinates_values(self, row, col):
        try:
            row = int(row)
            col = int(col)
        except Exception:
            self.error = (
                "Only Numbers are accepted, "
                "no letters or empty spaces!")
            return False
        if row < 0 or row > 9:
            self.error = "Row value is not between 0-9!"
            return False
        if (col < 0 or col > 8) and row < 9:
            self.error = "Column Value is not between 0-8!"
            return False
        if row == 9 and col > len(self.current_player_captures()) - 1:
            self.error = "Column value invalid for current captures!"
            return False
        return True

    # Devuelve las capturas del jugador actual
    def current_player_captures(self):
        if self.playerturn == "white":
            return self.white_captures
        elif self.playerturn == "black":
            return self.black_captures

    # Verifica el lugar seleccionado
    # Si contiene una pieza del color del jugador
    # Y si esa pieza puede ser movida o reintroducida en algun lugar
    def validate_origin_coordinates_location(self, row, col):
        if row == 9 and len(self.current_player_captures()[col].valid_drops(self.board)) < 1:
            self.error = "Cant drop this piece anywhere right now!"
            return False
        elif row == 9 and len(self.current_player_captures()[col].valid_drops(self.board)) > 0:
            return True
        if self.board[row][col] == "   ":
            self.error = "Thats an empty space!"
            return False
        if row < 9 and self.playerturn != self.board[row][col].color:
            self.error = "Thats not one of your pieces!"
            return False
        if len(self.board[row][col].valid_moves(self.board)) < 1:
            self.error = "You can't move that piece anywhere right now!"
            return False
        return True

    # Guarda la pieza elegida y sus coordenadas para su uso mas adelante
    def lift_piece_for_movement(self, row, col):
        if row == 9:
            self.lifted_piece = self.current_player_captures()[col]
        else:
            self.lifted_piece = self.board[row][col]
        self.lifted_piece_coordinates = (row, col)

    # Se ejecuta cuando se elige a donde se quiere mover o reintroducir una pieza
    # Verifica los valores de fila y columna
    # Mueve o reintroduce la pieza en el lugar seleccionado y pasa el turno
    def play_destination(self, row, col):
        self.error = ""
        if self.validate_destination_coordinates(row, col):
            self.move_piece(int(row), int(col))
            self.clean_lifted_piece_origin_location()
            if self.is_playing:
                self.next_turn()
            return True
        return False

    # Verifica los valores de fila y columna de play_destination
    def validate_destination_coordinates(self, row, col):
        try:
            row = int(row)
            col = int(col)
        except Exception:
            self.error = (
                "Only Numbers are accepted, "
                "no letters or empty spaces!")
            return False
        if row < 0 or row > 8:
            self.error = "Row value is not between 0-8!"
            return False
        if col < 0 or col > 8:
            self.error = "Column Value is not between 0-8!"
            return False
        if self.lifted_piece_coordinates[0] == 9:
            if (row, col) not in self.lifted_piece.valid_drops(self.board):
                self.error = "You cant drop this Piece there!"
                return False
            elif (row, col) in self.lifted_piece.valid_drops(self.board):
                return True
        if (row, col) not in self.lifted_piece.valid_moves(self.board):
            self.error = "That's not a valid movement!"
            return False
        return True

    # Mueve la pieza al lugar seleccionado
    # Borra la pieza seleccionada en lifted_piece
    def move_piece(self, row, col):
        if self.board[row][col] != "   ":
            self.capture_piece(row, col)
        self.board[row][col] = self.lifted_piece
        self.board[row][col].update_position(row, col)
        self.lifted_piece = "No piece lifted"

    # Si el lugar seleccionado tiene otra pieza, la captura
    # Si esa pieza era el rey, el juego termina
    def capture_piece(self, row, col):
        self.board[row][col].promoted = False
        self.board[row][col].captured = True
        self.board[row][col].color = self.playerturn
        self.current_player_captures().append(self.board[row][col])
        if self.board[row][col].__class__.__name__ == "King":
            self.is_playing = False

    # Borra la pieza reintroducida y las coordenadas en lifted_piece_cordinates
    def clean_lifted_piece_origin_location(self):
        row, col = self.lifted_piece_coordinates
        if row == 9:
            del self.current_player_captures()[col]
        else:
            self.board[row][col] = "   "
        self.lifted_piece_coordinates = ("", "")

    # Pasa el turno
    def next_turn(self):
        if self.playerturn == "white":
            self.playerturn = "black"
        else:
            self.playerturn = "white"


# Clase Padre para todas las piezas
class Piece():
    def __init__(self, name, color, position):
        self.name = name
        self.color = color
        self.position = position
        self.promoted = False
        self.captured = False
        self.set_for_promotion = False

    # Evalua como se va a representar la pieza en el tablero
    def __repr__(self):
        promoted = ""
        if self.promoted:
            promoted += "+"
        else:
            promoted += " "
        if self.color == "white":
            return promoted + self.name + "\u2227"
        elif self.color == "black":
            return promoted + self.name + "\u2228"

    # Devuelve el conjunto de movimientos validos para la promocion actual
    def valid_moves(self, board):
        if not self.promoted:
            return self.movement_unpromoted(board)
        elif self.promoted:
            return self.movement_promoted(board)
        return False

    # Calcula los movimientos validos sin promocion
    # Cada pieza tiene sus propios movimientos definidos en su propia clase
    def movement_unpromoted(self, board):
        return

    # Calcula los movimientos validos con promocion a GoldGeneral
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

    # Filtra los movimientos validos anteriores
    # Quita espacios imposibles, y espacios ocupados por fichas aliadas
    def filter_moves(self, coordinates, board):
        filtered_moves = []
        for space in coordinates:
            row, col = space
            if row < 0 or row > 8 or col < 0 or col > 8:
                pass
            elif board[row][col] == "   ":
                filtered_moves.append(space)
            elif board[row][col].color != self.color:
                filtered_moves.append(space)
        return filtered_moves

    # Promociona la pieza, y le quita la posibilidad de promocion
    def promote(self):
        self.promoted = True
        self.set_for_promotion = False

    # Actualiza la posision interna de la pieza para calcular sus movimientos
    # Si es aplicable, se le posibilita a la pieza ser promocionada
    def update_position(self, row, col):
        self.position = (row, col)
        if not self.captured:
            unpromoted = not self.promoted
            white = self.color == "white"
            black = self.color == "black"
            if white and self.position[0] < 3 and unpromoted:
                self.set_for_promotion = True
            elif black and 5 < self.position[0] < 9 and unpromoted:
                self.set_for_promotion = True
        else:
            self.captured = False
            self.set_for_promotion = False

    # Busca los espacios donde es posible reintroducir la pieza
    def valid_drops(self, board):
        empty_spaces = []
        valid_locations = []
        for row in range(9):
            for col in range(9):
                if board[row][col] == "   ":
                    empty_spaces.append((row, col))
        for coords in empty_spaces:
            self.position = coords
            if len(self.movement_unpromoted(board)) > 0:
                valid_locations.append(coords)
        return valid_locations


# Peon
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

    def valid_drops(self, board):
        empty_spaces = []
        valid_locations = []
        for row in range(9):
            for col in range(9):
                if board[row][col] == "   ":
                    empty_spaces.append((row, col))
        for coords in empty_spaces:
            self.position = coords
            if len(self.movement_unpromoted(board)) > 0:
                valid_locations.append(coords)
        return self.pawn_drop_rules(board, valid_locations)

    # Reglas especiales para la reintroduccion del peon
    # No puede reintroducirse en la misma columna que otro peon sin promocion
    # No puede reintroducirse haciendo jaque al rey oponente
    def pawn_drop_rules(self, board, valid_locations):
        invalid_locations = []
        for row in range(9):
            for col in range(9):
                if board[row][col] != "   ":
                    if board[row][col].name == "P" and board[row][col].color == self.color:
                        if not board[row][col].promoted:
                            for coords in valid_locations:
                                cond1 = coords[1] == col
                                cond2 = coords not in invalid_locations
                                if cond1 and cond2:
                                    invalid_locations.append(coords)
                    if board[row][col].name == "K" and board[row][col].color != self.color:
                        if self.color == "white" and (row + 1, col) in valid_locations and (row + 1, col) not in invalid_locations:
                            invalid_locations.append((row + 1, col))
                        elif self.color == "black" and (row - 1, col) in valid_locations and (row - 1, col) not in invalid_locations:
                            invalid_locations.append((row - 1, col))
        for coords in invalid_locations:
            valid_locations.remove(coords)
        return valid_locations

    # Ademas de actualizar la posicion interna
    # Promociona al peon si llega a la ultima fila posible
    def update_position(self, row, col):
        self.position = (row, col)
        unpromoted = not self.promoted
        white, black = self.color == "white", self.color == "black"
        if not self.captured:
            if white and self.position[0] < 3 and unpromoted:
                if self.position[0] == 0:
                    self.promote()
                    self.set_for_promotion = False
                else:
                    self.set_for_promotion = True
            elif black and 5 < self.position[0] < 9 and unpromoted:
                if self.position[0] == 8:
                    self.promote()
                    self.set_for_promotion = False
                else:
                    self.set_for_promotion = True
        else:
            self.captured = False
            self.set_for_promotion = False


# Lancero
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
            row, col = space
            if row < 0 or row > 8 or col < 0 or col > 8:
                pass
            elif board[row][col] == "   ":
                filtered_moves.append(space)
            elif board[row][col].color != self.color:
                filtered_moves.append(space)
                if not self.promoted:
                    break
            elif not self.promoted:
                break
        return sorted(filtered_moves)

    # Ademas de actualizar la posicion interna
    # Promociona al lancero si llega a la ultima fila posible
    def update_position(self, row, col):
        self.position = (row, col)
        unpromoted = not self.promoted
        white, black = self.color == "white", self.color == "black"
        if not self.captured:
            if white and self.position[0] < 3 and unpromoted:
                if self.position[0] == 0:
                    self.promote()
                    self.set_for_promotion = False
                else:
                    self.set_for_promotion = True
            elif black and 5 < self.position[0] < 9 and unpromoted:
                if self.position[0] == 8:
                    self.promote()
                    self.set_for_promotion = False
                else:
                    self.set_for_promotion = True
        else:
            self.captured = False
            self.set_for_promotion = False


# Caballero
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

    # Ademas de actualizar la posicion interna
    # Promociona al caballero si llega a la ultima fila posible
    def update_position(self, row, col):
        self.position = (row, col)
        unpromoted = not self.promoted
        white, black = self.color == "white", self.color == "black"
        if not self.captured:
            if white and self.position[0] < 3 and unpromoted:
                if self.position[0] == 0 or self.position[0] == 1:
                    self.promote()
                    self.set_for_promotion = False
                else:
                    self.set_for_promotion = True
            elif black and 5 < self.position[0] < 9 and unpromoted:
                if self.position[0] == 8 or self.position[0] == 7:
                    self.promote()
                    self.set_for_promotion = False
                else:
                    self.set_for_promotion = True
        else:
            self.captured = False
            self.set_for_promotion = False


# General de plata
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


# General de oro
class GoldGeneral(Piece):
    def __init__(self, color, position):
        super().__init__("G", color, position)

    def movement_unpromoted(self, board):
        return self.movement_promoted(board)

    # El General de oro no se promociona
    def promote(self):
        self.promoted = False

    # El general de oro no tiene posibilidad de promocion
    def update_position(self, row, col):
        self.position = (row, col)
        self.captured = False
        self.set_for_promotion = False


# Rey
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

    # El rey no se promociona
    def promote(self):
        self.promoted = False

    # El rey no tiene posibilidad de promocion
    def update_position(self, row, col):
        self.position = (row, col)
        self.captured = False
        self.set_for_promotion = False


# Alfil
class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__("B", color, position)

    def movement_unpromoted(self, board):
        coordinates_nw = []
        coordinates_ne = []
        coordinates_sw = []
        coordinates_se = []
        coordinates_final = []
        row, col = self.position
        for value in range(1, 9):
            coordinates_nw.append((row - value, col - value))
            coordinates_ne.append((row - value, col + value))
            coordinates_sw.append((row + value, col - value))
            coordinates_se.append((row + value, col + value))
        coordinates_final += self.filter_moves(coordinates_nw, board)
        coordinates_final += self.filter_moves(coordinates_ne, board)
        coordinates_final += self.filter_moves(coordinates_sw, board)
        coordinates_final += self.filter_moves(coordinates_se, board)
        return sorted(coordinates_final)

    def movement_promoted(self, board):
        coordinates = []
        row, col = self.position
        coordinates += self.filter_moves([(row + 1, col)], board)
        coordinates += self.filter_moves([(row - 1, col)], board)
        coordinates += self.filter_moves([(row, col - 1)], board)
        coordinates += self.filter_moves([(row, col + 1)], board)
        coordinates += self.movement_unpromoted(board)
        return sorted(coordinates)

    def filter_moves(self, coordinates, board):
        filtered_moves = []
        for space in coordinates:
            row, col = space
            if row < 0 or row > 8 or col < 0 or col > 8:
                pass
            elif board[row][col] == "   ":
                filtered_moves.append(space)
            elif board[row][col].color != self.color:
                filtered_moves.append(space)
                break
            else:
                break
        return filtered_moves


# Torre
class Rook(Piece):
    def __init__(self, color, position):
        super().__init__("R", color, position)

    def movement_unpromoted(self, board):
        coordinates_up = []
        coordinates_down = []
        coordinates_left = []
        coordinates_right = []
        coordinates_final = []
        row, col = self.position
        for value in range(1, 9):
            coordinates_down.append((row + value, col))
            coordinates_up.append((row - value, col))
            coordinates_right.append((row, col + value))
            coordinates_left.append((row, col - value))
        coordinates_final += self.filter_moves(coordinates_up, board)
        coordinates_final += self.filter_moves(coordinates_down, board)
        coordinates_final += self.filter_moves(coordinates_left, board)
        coordinates_final += self.filter_moves(coordinates_right, board)
        return sorted(coordinates_final)

    def movement_promoted(self, board):
        coordinates = []
        row, col = self.position
        coordinates += self.filter_moves([(row + 1, col + 1)], board)
        coordinates += self.filter_moves([(row - 1, col - 1)], board)
        coordinates += self.filter_moves([(row + 1, col - 1)], board)
        coordinates += self.filter_moves([(row - 1, col + 1)], board)
        coordinates += self.movement_unpromoted(board)
        return sorted(coordinates)

    def filter_moves(self, coordinates, board):
        filtered_moves = []
        for space in coordinates:
            row, col = space
            if row < 0 or row > 8 or col < 0 or col > 8:
                pass
            elif board[row][col] == "   ":
                filtered_moves.append(space)
            elif board[row][col].color != self.color:
                filtered_moves.append(space)
                break
            else:
                break
        return filtered_moves

