import unittest
from src.board import Board


class BoardTest(unittest.TestCase):

    def test_empty_board(self):
        board = Board()
        for row in range(6):
            for col in range(7):
                self.assertEqual(0, board.get_player_at(row, col))

    def test_get_free_index(self):
        board = Board()
        self.assertEqual(0, board.get_free_index(0))
        self.assertEqual(7, board.get_free_index(1))
        self.assertEqual(14, board.get_free_index(2))
        self.assertEqual(21, board.get_free_index(3))
        self.assertEqual(28, board.get_free_index(4))
        self.assertEqual(35, board.get_free_index(5))
        self.assertEqual(42, board.get_free_index(6))

    def test_make_move(self):
        board = Board()
        self.assertTrue(board.make_move(0))
        self.assertEqual(1, board.get_player_at(0, 0))
        self.assertTrue(board.make_move(1))
        self.assertEqual(2, board.get_player_at(0, 1))

    def test_make_move_in_full_column(self):
        board = Board()
        for _ in range(6):
            self.assertTrue(board.make_move(0))
            self.assertTrue(board.make_move(1))
            self.assertTrue(board.make_move(2))
            self.assertTrue(board.make_move(3))
            self.assertTrue(board.make_move(4))
            self.assertTrue(board.make_move(5))
            self.assertTrue(board.make_move(6))
            board.print_board()
        self.assertFalse(board.make_move(0))
        self.assertFalse(board.make_move(1))
        self.assertFalse(board.make_move(2))
        self.assertFalse(board.make_move(3))
        self.assertFalse(board.make_move(4))
        self.assertFalse(board.make_move(5))
        self.assertFalse(board.make_move(6))

    def test_unmake_move(self):
        board = Board()
        self.assertFalse(board.unmake_move())
        self.assertEqual(1, board.player)
        board.make_move(0)
        self.assertEqual(2, board.player)
        self.assertEqual(1, board.get_player_at(0, 0))
        self.assertEqual([0], board.move_history)
        self.assertTrue(board.unmake_move())
        self.assertEqual(1, board.player)
        self.assertEqual(0, board.get_player_at(0, 0))
        self.assertEqual([], board.move_history)

    def test_generate_moves_empty_board(self):
        board = Board()
        self.assertEqual([0, 1, 2, 3, 4, 5, 6], board.generate_moves())

    def test_generate_moves_full_board(self):
        board = Board()
        for _ in range(6):
            board.make_move(0)
            board.make_move(1)
            board.make_move(2)
            board.make_move(3)
            board.make_move(4)
            board.make_move(5)
            board.make_move(6)
        self.assertEqual([], board.generate_moves())

    def test_generate_moves_partially_full_board(self):
        board = Board()
        # Fill column 0 completely
        board.make_move(0)
        board.make_move(0)
        board.make_move(0)
        board.make_move(0)
        board.make_move(0)
        board.make_move(0)
        # Fill column 3 partially
        board.make_move(3)
        board.make_move(3)
        board.make_move(3)
        # Fill column 6 completely
        board.make_move(6)
        board.make_move(6)
        board.make_move(6)
        board.make_move(6)
        board.make_move(6)
        board.make_move(6)
        board.print_board()
        self.assertEqual([1, 2, 3, 4, 5], board.generate_moves())

    def test_four_in_a_row_vertical(self):
        board = Board()
        self.assertEqual(0, board.get_winner())
        board.make_move(0)
        self.assertEqual(0, board.get_winner())
        board.make_move(1)
        self.assertEqual(0, board.get_winner())
        board.make_move(0)
        self.assertEqual(0, board.get_winner())
        board.make_move(1)
        self.assertEqual(0, board.get_winner())
        board.make_move(0)
        self.assertEqual(0, board.get_winner())
        board.make_move(1)
        self.assertEqual(0, board.get_winner())
        board.make_move(0)
        self.assertEqual(1, board.get_winner())
        board.print_board()

    def test_four_in_a_row_horizontal(self):
        board = Board()
        self.assertEqual(0, board.get_winner())
        board.make_move(0)
        self.assertEqual(0, board.get_winner())
        board.make_move(0)
        self.assertEqual(0, board.get_winner())
        board.make_move(1)
        self.assertEqual(0, board.get_winner())
        board.make_move(1)
        self.assertEqual(0, board.get_winner())
        board.make_move(2)
        self.assertEqual(0, board.get_winner())
        board.make_move(2)
        self.assertEqual(0, board.get_winner())
        board.make_move(3)
        self.assertEqual(1, board.get_winner())
        board.print_board()

    def test_four_in_a_row_diagonal_bottom_left_top_right(self):
        board = Board()
        self.assertEqual(0, board.get_winner())
        board.make_move(0)
        board.make_move(1)
        board.make_move(1)
        board.make_move(2)
        board.make_move(3)
        board.make_move(2)
        board.make_move(2)
        board.make_move(3)
        board.make_move(3)
        board.make_move(4)
        self.assertEqual(0, board.get_winner())
        board.make_move(3)
        self.assertEqual(1, board.get_winner())
        board.print_board()

    def test_four_in_a_row_diagonal_top_left_bottom_right(self):
        board = Board()
        board.make_move(3)
        board.make_move(2)
        board.make_move(2)
        board.make_move(1)
        board.make_move(1)
        board.make_move(0)
        board.make_move(1)
        board.make_move(0)
        board.make_move(0)
        board.make_move(3)
        self.assertEqual(0, board.get_winner())
        board.make_move(0)
        self.assertEqual(1, board.get_winner())
        board.print_board()

    def test_four_in_a_row_diagonal_does_not_wrap_around(self):
        """
        0, 30, 36, 42

        """

        board = Board()
        board.make_move(4)
        board.make_move(0)
        board.make_move(5)
        board.make_move(6)
        board.make_move(4)
        board.make_move(5)
        board.make_move(6)
        board.make_move(4)

        self.assertEqual(0, board.get_winner())
