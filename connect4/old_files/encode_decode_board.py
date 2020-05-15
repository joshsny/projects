import numpy as np
from connect4 import board

# Encode the board representation as a tensor for the CNN
def encode_board(board):
    board_state = board.current_board
    encoded = np.zeros([6,7,3]).astype(int)
    encoder_dict = {"o": 0, "x": 1}
    for row in range(6):
        for col in range(7):
            if board_state[row, col] != " ":
                encoded[row, col, encoder_dict[board_state[row, col]]] = 1
            if board.player == 1:
                encoded[:,:,2] = 1 # Third channel set to 1 if it is the corresponding player to move

    return encoded

def decode_board(encoded):
    decoded = np.zeros([6,7]).astype(str)
    decoded[decoded == "0.0"] = " " # Initialise all points empty at first
    decoded_dict = {0: "o", 1: "x"}

    for row in range(6):
        for col in range(7):
            for k in range(2):
                if encoded[row, col, k] == 1:
                    decoded[row, col] = decoded_dict[k]
    
    cboard = board() # Initialise a game
    cboard.current_board = decoded # Set the current board to the decoded output
    cboard.player = encoded[0,0,2]
    return cboard

game1  = board()

game1.play(3); game1.play(5)

game1 = decode_board(encode_board(game1))
print(game1.current_board)

