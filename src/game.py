from src.board import Board
from src.search import Search
import random
import csv

def play_game():
    board = Board()
    search = Search()
    board.print_board()

    player = 1
    while True:

        col = int(input()) if player == 1 else search.search(board, 3)
        if col < 0 or col > 6:
            print("Invalid column")
            continue

        result = board.make_move(col)
        if not result:
            print("Column is full")
            continue

        board.print_board()

        winner = board.get_winner()
        if winner:
            print(f"Player {winner} wins!")
            break

        player = 2 if player == 1 else 1


def self_play_single(think_time=1, debug=False):
    board = Board()
    search = Search()

    player = 1
    result = 0

    random_opening_offset = random.choice([2, 4, 6])
    for _ in range(random_opening_offset):
        col = random.choice(range(7))
        board.make_move(col)

    while True:

        if len(board.generate_moves()) == 0:
            result = 0
            break

        col = search.search(board, think_time, debug=debug)
        if col < 0 or col > 6:
            print("Invalid column")
            continue

        board.make_move(col)

        if debug:
            board.print_board()

        winner = board.get_winner()
        if winner:
            result = winner
            if debug:
                print(f"Player {winner} wins!")
            break

        player = 2 if player == 1 else 1

    return board, result

