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
            column = int(input('Enter your column [1-7]: '))
            column -= 1
            if self.check_valid_move(column):
                self.place_move(column)
                if self.check_winner():
                    break
                self.change_player()
                while not self.check_valid_move(column=self.get_ai_move()):
                    pass
                self.place_move(column)
                self.change_player()
                
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
        pass
    def change_player(self) -> None:
        self.player = (self.player + 1) % 2
    def get_ai_move(self) -> int:
        return random.random(self.WIDTH)

def main():
    c4 = ConnectFour() 
    print(c4)
    
if __name__=="__main__":
    main()