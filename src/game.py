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

def self_play(mode, N_games = 10):
    match mode:
        case 'gendat':
            # PATH CURRENTLY HARDCODED
            TRAIN_DAT_PATH = "dat/training.csv"
            with open(TRAIN_DAT_PATH, 'w+') as f_obj:
                for _ in range(N_games):
                    self_play_single(file_object = f_obj)
        case 'demo':
            for _ in range(N_games):
                self_play_single()
        case _:
            raise TypeError("Unknown command")

def self_play_single(file_object = -1):
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

        # If the game was not interrupted, save the position to the training data
        if file_object !=-1:
            savedat(file_object, board, player)

def savedat(file_object, board, next_player):
    csvwriter = csv.writer(file_object)
    boards = board.get_boards()
    csvwriter.writerow(boards + [next_player])
    # Flush to store data even if program crashes 
    file_object.flush()