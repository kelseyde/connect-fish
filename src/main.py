from board.board import Board

running = True


def play_game():
    board = Board()
    board.print()

    player = 1
    while running:
        col = int(input())
        if col < 0 or col > 6:
            print("Invalid column")
            continue

        if not board.make_move(col):
            print("Column is full")
            continue

        board.print()

        winner = board.get_winner()
        if winner:
            print(f"Player {winner} wins!")
            break

        player = 2 if player == 1 else 1


while running:
    command = input()
    match command:
        case "newgame":
            play_game()
        case "quit":
            running = False
