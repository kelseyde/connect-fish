from src.game import play_game, self_play

print("🐟🐟🐟 Welcome to ConnectFish 🐟🐟🐟")

running = True

while running:
    command = input()
    match command:
        case "newgame":
            play_game()
        case "selfplay":
            print("Select mode: 'demo' or 'gendat'")
            command = input()
            assert(command in ['gendat', 'demo'], "Error: Unknown command")
            self_play(command)
        case "quit":
            running = False
        case _:
            raise TypeError("Unknown command")

