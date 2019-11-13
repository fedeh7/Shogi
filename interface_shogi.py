from shogi import Shogi


class Interface():


    def __init__(self):
        self.game = 0
        self.origin_row = 0
        self.origin_column = 0
        self.destiny_row = 0
        self.destiny_column = 0

    def print_interface_instructions(self):
        print(
            """
            \u2227
            \u039b
            ## Interface Instructions ##
            -Only numbers are accepted in inputs, no letters or spaces
            -Remember that Row 9 Holds your captured pieces, drop them on the board using 9 on Origin Row
            -Rows and columns of the board go from 0 to 8
            -(\u039b) Represents white pieces
            -(V) Represents black pieces
            ############################
            """
        )
    def start_playing(self):
        self.print_interface_instructions()
        self.game = Shogi()
        while self.game.is_playing:
            print(f"{self.game.playerturn} Turn\n")
            self.input_origin_coordinates()
            self.input_destiny_coordinates()
    
    def input_origin_coordinates(self):
        input_correct = False
        while not input_correct:
            self.print_board()
            row = input("Enter the Origin Row value(0-9): ")
            column = input("Enter the Origin Column value: ")
            if self.game.play_origin(row, column):
                input_correct = True
            else:
                print(self.game.error)
        return

    def input_destiny_coordinates(self):
        input_correct = False
        while not input_correct:
            self.print_board()
            row = input("Enter the Destination Row value(0-8): ")
            column = input("Enter the Destination Column value(0-8): ")
            if self.game.play_destination(row, column):
                input_correct = True
            else:
                if self.game.error != "":
                    print(self.game.error)
                else:
                    print("Values have to be between 0 and 8, no letters please")
        return
    
    def print_board(self):
        print(self.game.board_print())
        """printer = "\n"
        for i in range(9):
            for j in range(9):
                printer += (" " + str(self.game.board[i][j]))
            printer = printer + "\n"
        print("the board is: \n", printer)"""

if __name__ == "__main__":
    interface = Interface()
    interface.print_interface_instructions()
    interface.start_playing()