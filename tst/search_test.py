import unittest
from src.board import Board
from src.search import Search


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

        # Search must recognize that it needs to play in column 1 or 4 to prevent connect 4...

        move = search.search(board, 3)

        self.assertIn(move, [1, 4])
