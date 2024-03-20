import random


class ConnectFour:
    def __init__(self):
        self.rows = 6
        self.cols = 7
        self.board = [[" " for _ in range(self.cols)] for _ in range(self.rows)]
        self.players = ["X", "O"]
        self.current_player = 0

    def print_board(self):
        for row in self.board:
            print("|", end="")
            for cell in row:
                print(cell, end="|")
            print()

    def is_valid_move(self, col):
        return self.board[0][col] == " "

    def drop_piece(self, col, player):
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col] == " ":
                self.board[row][col] = player
                return

    def check_winner(self, player):
        # Check horizontal
        for row in self.board:
            for col in range(self.cols - 3):
                if all(cell == player for cell in row[col : col + 4]):
                    return True

        # Check vertical
        for col in range(self.cols):
            for row in range(self.rows - 3):
                if all(self.board[row + i][col] == player for i in range(4)):
                    return True

        # Check diagonal (down-right)
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if all(self.board[row + i][col + i] == player for i in range(4)):
                    return True

        # Check diagonal (up-right)
        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                if all(self.board[row - i][col + i] == player for i in range(4)):
                    return True

        return False

    def get_valid_moves(self):
        return [col for col in range(self.cols) if self.is_valid_move(col)]

    def play_game(self):
        while True:
            self.print_board()

            if self.current_player == 0:
                col = int(
                    input(
                        f"Player {self.players[self.current_player]}, choose a column (0-6): "
                    )
                )
                if not 0 <= col < self.cols or not self.is_valid_move(col):
                    print("Invalid move. Try again.")
                    continue
            else:
                col = self.get_ai_move()
                print(f"AI chooses column {col}")

            self.drop_piece(col, self.players[self.current_player])
            if self.check_winner(self.players[self.current_player]):
                self.print_board()
                if self.current_player == 0:
                    print(f"Player {self.players[self.current_player]} wins!")
                else:
                    print("AI wins!")
                break

            if all(cell != " " for row in self.board for cell in row):
                self.print_board()
                print("It's a tie!")
                break

            self.current_player = (self.current_player + 1) % 2

    def get_ai_move(self):
        return random.choice(self.get_valid_moves())


# Start the game
game = ConnectFour()
game.play_game()
``