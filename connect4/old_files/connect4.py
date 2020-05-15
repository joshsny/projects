# Imports
import numpy as np

class board():
    def __init__(self):
        # Initialize a 6 x 7 board
        self.init_board = np.zeros([6,7]).astype(str)
        self.init_board[self.init_board == "0.0"] = " "
        self.player = 0
        self.current_board = self.init_board

    def play(self, column):
        if self.current_board[0, column] != " ":
            return "Move is Invalid"
        else:
            row = 0; pos = " "
            while(pos == " "):
                if row == 6:
                    row += 1
                    break
                pos = self.current_board[row, column]
                row += 1
            if self.player == 0:
                self.current_board[row-2, column] = "o"
                self.player = 1
            elif self.player ==1:
                self.current_board[row-2, column] = "x"
                self.player = 0

    def check_winner(self):
        if self.player == 1:
            marker = "o"
        elif self.player == 0:
            marker = "x"
        
        for row in range(6):
            for col in range(7):
                if self.current_board[row, col] != " ":
                    # rows
                    try:
                        if self.current_board[row, col] == marker and self.current_board[row + 1, col] == marker and \
                            self.current_board[row + 2, col] == marker and self.current_board[row + 3, col] == marker:
                            #print("row")
                            return True
                    except IndexError:
                        next
                    # columns
                    try:
                        if self.current_board[row, col] == marker and self.current_board[row, col + 1] == marker and \
                            self.current_board[row, col + 2] == marker and self.current_board[row, col + 3] == marker:
                            #print("col")
                            return True
                    except IndexError:
                        next
                    # \ diagonal
                    try:
                        if self.current_board[row, col] == marker and self.current_board[row + 1, col + 1] == marker and \
                            self.current_board[row + 2, col + 2] == marker and self.current_board[row + 3, col + 3] == marker:
                            #print("\\")
                            return True
                    except IndexError:
                        next
                    # / diagonal
                    try:
                        if self.current_board[row, col] == marker and self.current_board[row + 1, col - 1] == marker and \
                            self.current_board[row + 2, col - 2] == marker and self.current_board[row + 3, col - 3] == marker \
                            and (col-3) >= 0:
                            #print("/")
                            return True
                    except IndexError:
                        next

    def valid_plays(self): # Returns all valid plays
        plays = []
        for col in range(7):
            if self.current_board[0, col] == " ":
                plays.append(col)
            return plays



# Testing out some plays
game = board()
print(game.valid_plays())
game.play(3); game.play(5)
game.play(3); game.play(6)
game.play(3); game.play(6)
game.play(4); game.play(6)
game.play(2); game.play(3)
print(game.current_board)
print(game.check_winner())


        

