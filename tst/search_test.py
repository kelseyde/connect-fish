import time
import unittest
from src.board import Board
from src.search import Search
import src.eval as eval


class SearchTest(unittest.TestCase):

    def test_search_chooses_connect_4(self):
        board = Board()
        search = Search()

        board.make_move(0)
        board.make_move(1)
        board.make_move(0)
        board.make_move(1)
        board.make_move(0)
        board.make_move(1)
        board.print_board()

        # Search must recognize that it can win by playing in column 0...

        move = search.search(board, 3)

        self.assertEqual(0, move)

    def test_search_must_prevent_unstoppable_connect_4(self):
        board = Board()
        search = Search()

        board.make_move(3)
        board.make_move(5)
        board.make_move(2)
        board.print_board()

        # Search must recognize that it needs to play in column 1 or 4 to prevent connect 4...

        move = search.search(board, 3, debug=True)

        self.assertIn(move, [1, 4])

    def test_search_identifies_lost_position_in_two_moves(self):
        board = Board()
        search = Search()

        board.make_move(3)
        board.make_move(5)
        board.make_move(2)
        board.make_move(6)
        board.make_move(1)
        board.print_board()

        search.timeout = time.time() + 1000000000

        score = search.search_to_depth(board, 0, 2, debug=False)
        self.assertEqual(-eval.FOUR_IN_A_ROW_SCORE, score)

        score = search.search_to_depth(board, 0, 3, debug=False)
        self.assertEqual(-eval.FOUR_IN_A_ROW_SCORE, score)

        score = search.search_to_depth(board, 0, 4, debug=False)
        self.assertEqual(-eval.FOUR_IN_A_ROW_SCORE, score)

        score = search.search_to_depth(board, 0, 5, debug=False)
        self.assertEqual(-eval.FOUR_IN_A_ROW_SCORE, score)

        score = search.search_to_depth(board, 0, 6, debug=False)
        self.assertEqual(-eval.FOUR_IN_A_ROW_SCORE, score)

        score = search.search_to_depth(board, 0, 7, debug=False)
        self.assertEqual(-eval.FOUR_IN_A_ROW_SCORE, score)
