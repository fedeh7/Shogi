import unittest

class TestShogi(unittest.TestCase):

    def test_setup(self):
        # tamaño tablero
        # tablero igual en todos los setup
        # fichas en su lugar
        return

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
        