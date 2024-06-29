from src.game import play_game, self_play

print("🐟🐟🐟 Welcome to ConnectFish 🐟🐟🐟")

running = True

while running:
    command = input()
    match command:
        case "newgame":
            play_game(random_opening=False)
        case "selfplay":
            self_play()
        case "quit":
            running = False
