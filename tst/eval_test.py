import unittest

from src.board import Board
import src.eval as eval


class EvalTest(unittest.TestCase):

    def test_connect_4_for_us(self):
        board = Board()
        board.make_move(0)
        board.make_move(1)
        board.make_move(0)
        board.make_move(5)
        board.make_move(0)
        board.make_move(3)
        board.make_move(0)
        score = -eval.evaluate(board)
        self.assertEqual(eval.FOUR_IN_A_ROW_SCORE, score)

    def test_connect_4_for_them(self):
        board = Board()
        board.make_move(0)
        board.make_move(1)
        board.make_move(0)
        board.make_move(5)
        board.make_move(0)
        board.make_move(3)
        board.make_move(0)
        board.make_move(2)
        score = eval.evaluate(board)
        self.assertEqual(eval.FOUR_IN_A_ROW_SCORE, score)

    def test_two_in_a_row(self):
        board = Board()
        board.make_move(0)
        board.make_move(1)
        board.make_move(0)
        score = -eval.evaluate(board)
        self.assertEqual(eval.TWO_IN_A_ROW_SCORE, score)

    def test_three_in_a_row(self):
        board = Board()
        board.make_move(0)
        board.make_move(1)
        board.make_move(0)
        board.make_move(6)
        board.make_move(0)
        score = -eval.evaluate(board)
        self.assertEqual(eval.THREE_IN_A_ROW_SCORE, score)

    def test_two_vs_three_in_a_row(self):
        board = Board()
        board.make_move(0)
        board.make_move(1)
        board.make_move(0)
        board.make_move(1)
        board.make_move(0)
        score = -eval.evaluate(board)
        self.assertEqual(eval.THREE_IN_A_ROW_SCORE - eval.TWO_IN_A_ROW_SCORE, score)

    def test_two_vs_two_in_a_row(self):
        board = Board()
        board.make_move(0)
        board.make_move(1)
        board.make_move(0)
        board.make_move(1)
        score = -eval.evaluate(board)
        self.assertEqual(0, score)

    def test_three_vs_three_in_a_row(self):
        board = Board()
        board.make_move(0)
        board.make_move(1)
        board.make_move(0)
        board.make_move(1)
        board.make_move(0)
        board.make_move(1)
        score = -eval.evaluate(board)
        self.assertEqual(0, score)

    def test_two_twos_vs_three_in_a_row(self):
        board = Board()
        board.make_move(0)
        board.make_move(1)
        board.make_move(0)
        board.make_move(1)
        board.make_move(0)
        board.make_move(3)
        board.make_move(6)
        board.make_move(3)
        board.make_move(4)
        score = -eval.evaluate(board)
        self.assertEqual(eval.THREE_IN_A_ROW_SCORE - (2 * eval.TWO_IN_A_ROW_SCORE), score)

    def test_four_in_a_row_diagonal(self):
        board = Board()
        board.make_move(0)
        board.make_move(1)
        board.make_move(1)
        board.make_move(2)
        board.make_move(2)
        board.make_move(3)
        board.make_move(2)
        board.make_move(3)
        board.make_move(3)
        board.make_move(4)
        board.make_move(3)
        board.print_board()
        score = -eval.evaluate(board)
        self.assertEqual(eval.FOUR_IN_A_ROW_SCORE, score)

