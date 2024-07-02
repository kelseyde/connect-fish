from src.board import Board
from src.search import Search
import random
import csv


def play_game(random_opening=False):
    board = Board()
    search = Search()

    if random_opening:
        for _ in range(random.choice(range(6))):
            col = random.choice(range(7))
            board.make_move(col)

    board.print_board()

    player = 1
    while True:

        col = int(input()) if player == 1 else search.search(board, 3, debug=True)
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


def play_multiplayer_game(player_1, player_2, think_time_s, debug=False):
    board = Board()

    for _ in range(random.choice([2, 4, 6])):
        col = random.choice(range(7))
        board.make_move(col)

    if debug:
        board.print_board()
    result = 0

    starting_player_id = random.choice([1, 2])
    starting_player = player_1 if starting_player_id == 1 else player_2

    current_player_id = starting_player_id
    current_player = starting_player

    while True:

        if len(board.generate_moves()) == 0:
            result = 0
            break

        col = current_player.search(board, think_time_s)
        if col < 0 or col > 6:
            print("Invalid column")
            continue

        result = board.make_move(col)
        if not result:
            print("Column is full")
            continue

        if debug:
            board.print_board()

        outcome = board.get_winner()
        if outcome != 0:
            result = current_player_id
            if debug:
                print(f"Player {result} wins!")
            break

        current_player = player_1 if current_player == player_2 else player_2
        current_player_id = 2 if current_player_id == 1 else 1

    return result


def self_play():
    while True:
        self_play_single()

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

