from board import Board, COLS
from ai import AI


class Game:
    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.turn = "X"

    def run(self):
        print("Connect Four — you are X.")
        if self.board.full():
            self.board.print()
            print("Draw.")
            return

        while True:
            self.board.print()
            if self.turn == "X":
                raw = input("Column (1-7), or q: ").strip().lower()
                if raw == "q":
                    print("Game ended.")
                    return
                try:
                    col = int(raw) - 1
                except ValueError:
                    print("Invalid input. Enter a column number (1-7) or 'q' to quit.")
                    continue
                if not 0 <= col < COLS:
                    print("Invalid column. Enter a number between 1 and 7.")
                    continue
                if self.board.is_col_full(col):
                    print("Column is full. Please choose another column.")
                    continue
            else:
                col = self.ai.choose_column(self.board)
                if col is None:
                    if self.board.full():
                        self.board.print()
                        print("Draw.")
                    else:
                        print("AI cannot make a move.")
                    return

            if self.board.drop(col, self.turn) is None:
                print("Column unavailable.")
                continue

            print(f"{self.turn} dropped in column {col + 1}.")

            if self.board.winner(self.turn):
                self.board.print()
                print(self.turn, "wins!")
                return
            if self.board.full():
                self.board.print()
                print("Draw.")
                return

            self.turn = "O" if self.turn == "X" else "X"
