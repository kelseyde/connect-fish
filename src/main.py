from board.board import Board

running = True

board = Board()
board.make_move(0)
board.make_move(1)
board.make_move(2)
board.make_move(2)
board.print()

while (running):
    command = input()
    match command:
        case "newgame": print_board();
        case "quit": running = False


