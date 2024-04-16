import random

class ConnectFour:
    WIDTH = 7
    HEIGHT = 6
    
    def __init__(self) -> None:
        self.player = 0
        self.players = ["X", "O"]
        self.board = [[" " for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)]
        
    def __repr__(self) -> str:
        outstr = ""
        for row in self.board:
            outstr += str(row) + '\n'
        return outstr
    
    def play_game(self) -> str:
        """Plays the game of Connect Four for the Object

        Returns:
            str: returns the player that won the game
        """
        while True:
            print(self)
            column = int(input('Enter your column [1-7]: '))
            column -= 1
            if self.check_valid_move(column):
                self.place_move(column)
                if self.check_winner():
                    break
                self.change_player()
                self.place_move(self.get_ai_move())
                if self.check_winner():
                    break
                self.change_player()
        print(self)
        print(f'Player {self.player + 1} WINS!')
                
    def check_valid_move(self, col: int) -> bool:
        """Checks to see if the move is valid (i.e. there is room in the column)

        Args:
            col (int): The 0-based column of the board

        Returns:
            bool: True if a valid move
        """
        return self.board[0][col] == " "
    
    def place_move(self, col: int) -> None:
        """place_move() places a player's 'piece' in the valid column

        Args:
            col (int): The integer number (0 based) of the column
        """
        # Start at the bottom and go to the top
        for row in range(self.HEIGHT - 1, -1, -1):
            if self.board[row][col] == " ":
                self.board[row][col] = self.players[self.player]
                break
                
    def check_winner(self) -> bool:
        return (
            self.check_verticle() 
            or self.check_horizontal() 
            or self.check_up_right() 
            or self.check_down_right()
        )
    
    def check_verticle(self) -> bool:
        for col in range(self.WIDTH):
            num_pieces = 0
            for row in range(self.HEIGHT):
                if self.board[row][col] == self.players[self.player]:
                    num_pieces += 1
                    if num_pieces == 4: 
                        return True
                else:
                    num_pieces = 0
        return False
    
    def check_horizontal(self) -> bool:
        for row in range(self.HEIGHT):
            num_pieces = 0
            for col in range(self.WIDTH):
                if self.board[row][col] == self.players[self.player]:
                    num_pieces += 1
                    if num_pieces == 4: 
                        return True
                else:
                    num_pieces = 0
        return False
    
    def check_up_right(self):
        # /
        # [3][0] // [2][1] // [1][2] // [0][3]
        for row in range(3, self.HEIGHT):
            for col in range(self.WIDTH -3):
                if all(self.board[row - i][col + i] == self.players[self.player] for i in range(4)):
                    return True
        return False
    
    def check_down_right(self):
        # [0][0] // [1][1] // [2][2] // [3][3]
        # [1][0] // [2][1] // ...
        for row in range(self.HEIGHT - 3):
            for col in range(self.WIDTH - 3):
                if all(self.board[row + i][col + i] == self.players[self.player] for i in range(4)):
                    return(True)
        return False
                    
    def change_player(self) -> None:
        self.player = (self.player + 1) % 2
        
    def get_ai_move(self) -> int:
        column=random.randrange(self.WIDTH)
        while not self.check_valid_move(column):
            column=random.randrange(self.WIDTH)
        return column

def main():
    c4 = ConnectFour() 
    c4.play_game()
    
if __name__=="__main__":
    main()