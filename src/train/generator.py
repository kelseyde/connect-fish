import csv
import random

from src.board import Board
from src.game import self_play_single

TRAINING_DATA_PATH = "data/training.csv"


def generate_training_positions(
        file_path=TRAINING_DATA_PATH,
        num_games=None,
        think_time=0.025,
        positions_per_game=5,
        debug=False):
    """
    Generate training data by playing self-play games and saving the positions to a CSV file.
    """
    with open(file_path, 'a') as file:
        game_count = 0
        position_count = 0
        while True:
            if num_games and game_count >= num_games:
                break
            board, result = self_play_single(think_time=think_time, debug=debug)
            game_count += 1
            positions = extract_positions(board, result, positions_per_game)
            save_positions(file, positions)
            position_count += len(positions)
            print(f"game {game_count}, positions {position_count}")
        print("training data generation complete.")


def extract_positions(board, result, positions_per_game):
    """
    Extract 'positions_per_game' training positions from a game. The positions are selected randomly from the game
    to ensure a variety of positions being included in training.
    """
    training_positions = []
    start_board = Board()
    move_indices = range(0, len(board.move_history))
    random_indices = random.sample(move_indices, positions_per_game)

    for index, move in enumerate(board.move_history):
        start_board.make_move(move)
        if index in random_indices:
            bbs = start_board.boards
            p1_bb, p2_bb = bbs[1], bbs[2]
            side_to_move = start_board.player
            moves_to_go = len(board.move_history) - len(start_board.move_history)
            score = format_score(result, side_to_move, moves_to_go)
            training_positions.append((p1_bb, p2_bb, side_to_move, score))
    return training_positions


def save_positions(file, positions):
    """
    Convert the training positions to a comma-separated row and write them to the CSV file.
    """
    writer = csv.writer(file)
    rows = [(p1, p2, stm, score) for p1, p2, stm, score in positions]
    writer.writerows(rows)
    file.flush()


def format_score(result, side_to_move, moves_to_go):
    """
    Format the score in terms of how many moves until the result was reached.
    So +41 means the side to move wins in 1 move (since there are a maximum 42 moves),
    while -2 means the side to move loses in 40 moves, and so on.
    """
    if result == 0:  # Draw
        return 0
    base_score = 1 if result == side_to_move else -1
    return (42 - moves_to_go) * base_score
