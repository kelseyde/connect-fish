import unittest
from src.board.board import Board


class BoardTest(unittest.TestCase):

    def test_empty_board(self):
        board = Board()
        for row in range(6):
            for col in range(7):
                self.assertEqual(0, board.get_player_at(row, col))

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
            board.print()
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
        board.make_move(0)
        self.assertEqual(1, board.get_player_at(0, 0))
        self.assertEqual([0], board.move_history)
        self.assertTrue(board.unmake_move())
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
        for _ in range(6):
            board.make_move(0)
            board.make_move(1)
            if _ % 2 == 0:
                # leave column 2 partially filled
                board.make_move(2)
            board.make_move(3)
            board.make_move(4)
            board.make_move(5)
            # leave column 6 empty
        self.assertEqual([2, 6], board.generate_moves())

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
        board.print()

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
        board.print()

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
        board.print()

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
        board.print()


