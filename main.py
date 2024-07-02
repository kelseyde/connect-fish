from src.game import play_game
import src.train.generator as generator

print("🐟🐟🐟 Welcome to ConnectFish 🐟🐟🐟")

running = True

while running:
    command = input()
    match command:
        case "newgame":
            play_game()
        case "generate":
            generator.generate_training_positions()
        case "quit":
            running = False
        case _:
            raise TypeError("Unknown command")

