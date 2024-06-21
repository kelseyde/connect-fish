from src.game import play_game

print("🐟🐟🐟 Welcome to ConnectFish 🐟🐟🐟")

running = True

while running:
    command = input()
    match command:
        case "newgame":
            play_game()
        case "quit":
            running = False
