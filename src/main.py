print("hello world")

def print_board():
    print("""
    - - - - - - -
    - - - - - - -
    - - - - - - -
    - - - - - - -
    - - - - - - -
    - - - - - - -
    """)

running = True
while (running):
    command = input()
    match command:
        case "newgame": print_board();
        case "quit": running = False

