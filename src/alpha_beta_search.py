from src.eval import evaluate
from time import time, strftime, localtime
import random

MAX_VALUE = float('inf')
MIN_VALUE = -float('inf')


class Search:

    def __init__(self):
        self.max_depth = 42
        self.best_move = -1
        self.best_move_current_depth = -1
        self.timeout = -1

    def search(self, board, seconds, debug=False):
        """
        Do an iterative deepening search: search to depth 1, then 2, then 3, and so on, until time runs out.
        """

        start = time()
        self.timeout = start + seconds
        if debug:
            print(f"Searching for {seconds} seconds, timeout at {strftime('%Y-%m-%d %H:%M:%S', localtime(self.timeout))}")

        current_depth = 1
        self.best_move = -1
        self.best_move_current_depth = -1

        # Keep searching to greater depths until we run out of time.
        while time() < self.timeout and current_depth < self.max_depth:

            if debug:
                print(f"Searching to depth {current_depth}")

            alpha = MIN_VALUE
            beta = MAX_VALUE

            # Reset the best move at the current depth.
            self.best_move_current_depth = -1

            # Start a search limited to the current depth.
            self.search_to_depth(board, 0, current_depth, alpha, beta, debug=debug)

            # If we completed the search, update the best move.
            if self.best_move_current_depth >= 0:
                self.best_move = self.best_move_current_depth
            current_depth += 1

        if self.best_move < 0:
            print("Time ran out, selecting a random move")
            return self.random_move(board)

        return self.best_move

    def search_to_depth(self, board, depth_from_root, depth_remaining, alpha, beta, debug=False):
        """
        Do a minimax search: find the move that maximises our score, limited to a certain depth.
        """

        # Exit early if we run out of time
        if time() > self.timeout:
            return 0

        # Generate all legal moves in the position
        moves = board.generate_moves()

        # If there are no legal moves - or if we reach the maximum search depth - evaluate the position
        if len(moves) == 0 or depth_remaining == 0:
            return evaluate(board)

        # Loop through all the legal moves.
        for move in moves:

            # Make the move on the board, search the resulting position, and then unmake the move.
            board.make_move(move)
            score = -self.search_to_depth(board, depth_from_root + 1, depth_remaining - 1, -beta, -alpha, debug=debug)
            board.unmake_move()

            # If score >= beta, this position is 'too good' - the opponent won't let us get here
            # as they have better options earlier in the search tree. Therefore, there's no point
            # searching any further down this branch.
            if score >= beta:
                board.print_board()
                print(f"Pruning move {move} at depth {depth_from_root}")
                return score

            # If the score is better than our current best score, update the best score.
            if score > alpha:
                alpha = score

                # If we are at the root of the search tree, update the best move.
                if depth_from_root == 0:
                    self.best_move_current_depth = move

        return alpha

    def random_move(self, board):
        moves = board.generate_moves()
        if len(moves) == 0:
            return -1
        else:
            return random.choice(moves)
