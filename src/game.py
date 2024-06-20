from src.board import Board
from src.search import Search


def play_game():
    board = Board()
    search = Search()
    board.print_board()

    player = 1
    while True:

        col = int(input()) if player == 1 else search.search(board, 5)
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
