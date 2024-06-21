class Board:
    """
    The 6x7 Connect 4 board is represented as a bitboard in the following format:

        5 12 19 26 33 40 47
        4 11 18 25 32 39 46
        3 10 17 24 31 38 45
        2  9 16 23 30 37 44
        1  8 15 22 29 36 43
        0  7 14 21 28 35 42

    This representation allows us to quickly compute the bit index for a given row and column: index = col * 7 + row.
    It also allows us to check for four-in-a-row by shifting the bitboard by 1, 7, 6, and 8 bits in each direction.
    """

    def __init__(self):
        """
        Initialize an empty 7x6 Connect 4 board.
        """

        # Whose turn is it (player 1 or 2)
        self.player = 1

        # 0 = all occupied tiles,
        # 1 = player 1 occupied tiles,
        # 2 = player 2 occupied tiles.
        self.boards = [0, 0, 0]

        # Record the move history.
        self.move_history = []

    def make_move(self, col):
        """
        Make a move in the given column.
        """
        index = self.get_free_index(col)
        if index != -1:
            move_mask = 1 << index
            # Add the move to the occupied board and the player board.
            self.boards[0] |= move_mask
            self.boards[self.player] |= move_mask
            self.move_history.append(col)
            self.player = 1 if self.player == 2 else 2
            return True
        return False

    def unmake_move(self):
        """
        Undo the last move made on the board.
        """
        if self.move_history:
            last_col = self.move_history.pop()
            index = self.get_occupied_index(last_col)
            if index != -1:
                self.player = 1 if self.player == 2 else 2
                move_mask = 1 << index
                # Remove the move from the occupied board and the player board.
                self.boards[0] &= ~move_mask
                self.boards[self.player] &= ~move_mask
                return True
        return False

    def generate_moves(self):
        """
        Generate all legal moves for the current board state.
        """
        moves = []
        if self.get_winner() != 0:
            return moves
        for col in range(7):
            if self.get_free_index(col) != -1:
                # If the column has a free tile, add it to the list of legal moves.
                moves.append(col)
        return moves

    def get_winner(self):
        """
        Check if the current board has four-in-a-row; return the winning player or 0 if there is no winner.
        """

        # Always check the player who has just moved first, as this method is likely to be called just after make_move,
        # and therefore the player who has just moved is the most likely to have won.
        us = 1 if self.player == 2 else 2
        them = 2 if self.player == 2 else 1

        if self.is_won(us):
            return us
        elif self.is_won(them):
            return them
        return 0

    def is_won(self, player):
        """
        Check if the specified player has four-in-a-row on the board.
        Given our board representation the directions to check for four-in-a-row are:
            - Horizontal: 1
            - Vertical: 7
            - Diagonal (top-left to bottom-right): 6
            - Diagonal (top-right to bottom-left): 8
        We shift the bitboard in each direction three times and check if the result is not zero.
        The unused bits on the right side of each row are important, as they prevent the bitboard
        from wrapping around to the left side of the board, which would cause false positives.
        If not zero, then the player has four-in-a-row.
        """
        bb = self.boards[player]
        directions = [1, 7, 6, 8]
        for direction in directions:
            if (bb & (bb >> direction)) & \
                     (bb >> 2 * direction) & \
                     (bb >> 3 * direction):
                return True
        return False

    def get_free_index(self, col):
        """
        Get the bit index of the next free position in the specified column, or return -1 if the column is full.
        """
        for row in range(6):
            pos = self.get_index(row, col)
            # Check if the position is empty
            if not self.boards[0] & (1 << pos):
                return pos
        return -1

    def get_occupied_index(self, col):
        """
        Get the bit index of the highest occupied position in the specified column, or return -1 if the column is empty.
        """
        for row in range(5, -1, -1):
            pos = self.get_index(row, col)
            # Check if the position is occupied
            if self.boards[0] & (1 << pos):
                return pos
        return -1

    def get_player_at(self, row, col):
        """
        Get the player occupying the specified position.
        """
        pos = self.get_index(row, col)
        if self.boards[1] & (1 << pos):
            return 1
        elif self.boards[2] & (1 << pos):
            return 2
        return 0

    def get_index(self, row, col):
        """
        Get the bit index of the specified position.
        """
        return col * 7 + row

    def print_board(self):
        """
        Display the board with colors: player 1 (red) and player 2 (yellow).
        """
        red = '\033[91m●\033[0m'
        yellow = '\033[93m●\033[0m'
        empty = '.'

        board_str = ""
        for row in range(5, -1, -1):
            for col in range(7):
                pos = self.get_index(row, col)
                if self.boards[1] & (1 << pos):
                    board_str += red + " "
                elif self.boards[2] & (1 << pos):
                    board_str += yellow + " "
                else:
                    board_str += empty + " "
            board_str += "\n"

        # Add a column footer
        board_str += "0 1 2 3 4 5 6\n"

        print(board_str)
