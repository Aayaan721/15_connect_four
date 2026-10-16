import random
from board import COLS


class AI:
    def choose_column(self, board, me="O", opponent="X"):
        legal = [c for c in range(COLS) if not board.is_col_full(c)]
        if not legal:
            return None

        # 1. Take immediate winning move if available
        for c in legal:
            r = board.drop(c, me)
            if board.winner(me):
                board.grid[r][c] = "."
                return c
            board.grid[r][c] = "."

        # 2. Block opponent's immediate winning move
        for c in legal:
            r = board.drop(c, opponent)
            if board.winner(opponent):
                board.grid[r][c] = "."
                return c
            board.grid[r][c] = "."

        # 3. Fallback to legal move
        return random.choice(legal)
