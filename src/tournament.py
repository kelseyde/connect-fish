from src import game


def run(player_1, player_2, num_games=100, think_time_s=1):
    p1_wins = 0
    p2_wins = 0
    draws = 0
    for i in range(num_games):
        result = game.play_multiplayer_game(player_1, player_2, think_time_s)
        if result == 1:
            p1_wins += 1
        elif result == 2:
            p2_wins += 1
        elif result == 0:
            draws += 1
        print(f"Score after game {i + 1}: p1 wins {p1_wins}, p2 wins {p2_wins}, draws {draws}")
    print(f"Final score: p1 wins {p1_wins}, p2 wins {p2_wins}, draws {draws}")


run(game.Search(), game.Search(), num_games=1000, think_time_s=0.2)