from shogi import Shogi, Rook, Lance, Pawn


class Interface():


    def __init__(self):
        self.game = 0
        self.turn_count = 0
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
        #self.game.board = self.sample_board
        #self.game.board[4][4] = Lance("white", (4, 4))
        #self.game.board[2][4] = Lance("white", (4, 4))
        x = Pawn("black", (0, 0))
        x.captured = True
        self.game.playerturn = "black"
        self.game.white_captures.append(x)
        print(self.game.white_captures[0].valid_drops(self.game.board))
        while self.game.is_playing:
            self.turn_count += 1
            self.input_origin_coordinates()
            self.input_destiny_coordinates()
        print(f"### Congratulations! {self.game.playerturn} Wins! ###".title())
    
    def input_origin_coordinates(self):
        input_correct = False
        while not input_correct:
            self.print_board()
            print(f"========= #{self.turn_count} {self.game.playerturn} Turn =========\n".title())
            if self.game.error != "":
                print(f"---{self.game.error}---")
            row = input("Enter the Origin Row value(0-9): ")
            column = input("Enter the Origin Column value: ")
            if self.game.play_origin(row, column):
                input_correct = True
        return

    def input_destiny_coordinates(self):
        input_correct = False
        promote = ""
        while not input_correct:
            self.print_board()
            print(f"========= #{self.turn_count} {self.game.playerturn} Turn =========\n".title())
            if self.game.error != "":
                print(f"---{self.game.error}---")
            row = input("Enter the Destination Row value(0-8): ")
            column = input("Enter the Destination Column value(0-8): ")
            if self.game.play_destination(row, column):
                input_correct = True
                if self.game.board[int(row)][int(column)].set_for_promotion:
                    while promote != "y" and promote != "n":
                        promote = input("Do you want to promote the piece?(y/n): ").lower()
                        if promote != "y" and promote != "n":
                            print("Enter 'y' or 'n'")
                    if promote == "y":
                        self.game.board[int(row)][int(column)].promote()


        return
    
    def print_board(self):
        print(self.game.board_print())

if __name__ == "__main__":
    interface = Interface()
    interface.start_playing()