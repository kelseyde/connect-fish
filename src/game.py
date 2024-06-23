from src.board import Board
from src.search import Search
import random

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

def self_play():
    while True:
        self_play_single()

def self_play_single():
    board = Board()
    search = Search()
    #board.print_board()

    player = 1

    for _ in range(6):
        col = random.choice(range(7))
        board.make_move(col)

    while True:

        col =  search.search(board, 0.5)
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