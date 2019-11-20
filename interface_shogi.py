from shogi import Shogi, Rook, Lance, Pawn


class Interface():

    def __init__(self):
        self.game = Shogi()
        self.turn_count = 0

    def start_playing(self):
        while self.game.is_playing:
            self.turn_count += 1
            self.input_origin_coordinates()
            self.input_destiny_coordinates()
        print(
            f"### Congratulations! {self.game.playerturn} Wins "
            f"in {self.turn_count} turns! ###".title())

    def input_origin_coordinates(self):
        input_correct = False
        while not input_correct:
            print(self.print_board())
            if self.game.error != "":
                print(f"---{self.game.error}---")
            row = input("Enter the Origin Row value(0-9): ")
            column = input("Enter the Origin Column value: ")
            if row == "exit" or column == "exit":
                self.game.is_playing = False
            if self.game.play_origin(row, column):
                input_correct = True
        return

    def input_destiny_coordinates(self):
        input_correct = False
        promote = ""
        while not input_correct:
            print(self.print_board())
            if self.game.error != "":
                print(f"---{self.game.error}---")
            row = input("Enter the Destination Row value(0-8): ")
            column = input("Enter the Destination Column value(0-8): ")
            if self.game.play_destination(row, column):
                input_correct = True
                if self.game.board[int(row)][int(column)].set_for_promotion:
                    while promote != "y" and promote != "n":
                        promote = input(
                            "Do you want to promote the piece?(y/n): ").lower()
                        if promote != "y" and promote != "n":
                            print("Enter 'y' or 'n'")
                    if promote == "y":
                        self.game.board[int(row)][int(column)].promote()
        return

    def print_board(self):
        screen = self.game.board_print()
        symbol = ""
        if self.game.playerturn == "white":
            symbol = "(\u039b)"
        elif self.game.playerturn == "black":
            symbol = "(V)"
        turn_indicator = (
            f"\n======== #{self.turn_count} "
            f"{self.game.playerturn}{symbol} Turn ========\n".title())
        screen += turn_indicator
        return screen

if __name__ == "__main__":
    interface = Interface()
    interface.start_playing()
