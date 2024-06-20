def evaluate(board):
    """
    Simple evaluation function placeholder until we implement neural networks:
    If one side has four-in-a-row, return a score of 1 million.
    Otherwise, count the number of two-in-a-rows and three-in-a-rows for each player, multiplied by a bonus of 1000 for
    three-in-a-rows and 500 for two-in-a-rows, and return the difference.
    """
    four_in_a_row_score = 1000000
    three_in_a_row_score = 1000
    two_in_a_row_score = 200

    winner = board.get_winner()
    if winner != 0:
        return four_in_a_row_score if winner == board.player else -four_in_a_row_score

    player_1_twos = count_two_in_a_row(board, 1)
    player_1_threes = count_three_in_a_row(board, 1)

    player_2_twos = count_two_in_a_row(board, 2)
    player_2_threes = count_three_in_a_row(board, 2)

    player_1_score = (player_1_twos * two_in_a_row_score) + (player_1_threes * three_in_a_row_score)
    player_2_score = (player_2_twos * two_in_a_row_score) + (player_2_threes * three_in_a_row_score)
    score = player_1_score - player_2_score

    return score if board.player == 1 else -score


def count_three_in_a_row(board, player):
    """
    Count the number of three-in-a-rows for the specified player, excluding those that are part of a four-in-a-row.
    """
    count = 0
    directions = [1, 7, 6, 8]
    bb = board.boards[player]

    for direction in directions:
        threes = (bb & (bb >> direction) & (bb >> (2 * direction))) & ~(bb >> (3 * direction)) & ~(bb << direction)
        while threes:
            count += 1
            threes &= threes - 1  # Clear the least significant bit set

    return count


def count_two_in_a_row(board, player):
    """
    Count the number of two-in-a-rows for the specified player, excluding those that are part of a three-in-a-row or four-in-a-row.
    """
    count = 0
    directions = [1, 7, 6, 8]
    bb = board.boards[player]

    for direction in directions:
        twos = (bb & (bb >> direction)) & ~(bb >> (2 * direction)) & ~(bb << direction)
        while twos:
            count += 1
            twos &= twos - 1  # Clear the least significant bit set

    return count
