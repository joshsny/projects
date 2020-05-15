import numpy as np
import pygame
import sys

# Initialize global variables
ROW_COUNT = 6
COLUMN_COUNT = 7

BLUE = (0, 0, 255) # Colour for game
BLACK = (0,0,0)


def createBoard(): # Initializes an empty board
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def dropPiece(board, row, col, piece): # Drops a piece on the board
    board[row, col] = piece    

def isValidLocation(board, col): # Determines if a column has any free entries
    return board[ROW_COUNT-1][col] == 0

def getRow(board, col): # Gets the first available row for a given column
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def printBoard(board): # Changes orientation of numpy matrix for printing the board correctly
    print(np.flip(board, 0))

def winningMove(board, piece):
    # Check for winning move in a niave way (by brute force)
    
    # Check horizontal locations
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check for rightwards diagonal
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check for leftwards diagonal
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

    return False

def drawBoard(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, (r+1)*SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int((c+0.5)*SQUARESIZE), int((r+1.5)*SQUARESIZE)), radius)

board = createBoard()
printBoard(board)
game_over = False
turn = 0

# Initialize PyGame game
pygame.init()

SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE

size = (width, height)

radius = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)
drawBoard(board)
pygame.display.update()

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Quit the game when the user requests it
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("")
            # Ask for Player 1 (P1) input
            # if turn == 0:
            #     col = int(input("Player 1 make selection (0-6):"))
# 
            #     if isValidLocation(board, col):
            #         row = getRow(board, col)
            #         dropPiece(board, row, col, 1)
# 
            #         if winningMove(board, 1): # Check if move wins
            #             game_over = True
            #             print("Player 1 wins!")
            #         else:
            #             printBoard(board)
            #             turn += 1
            #             turn = turn % 2
# 
            # # Ask for Player 2 (P2) input
            # else:
            #     col = int(input("Player 2 make selection (0-6):"))
# 
            #     if isValidLocation(board, col):
            #         row = getRow(board, col)
            #         dropPiece(board, row, col, 2)
            #         
            #         if winningMove(board, 2): # Check if move wins
            #             game_over = True
            #             print("Player 2 wins!")
            #         else:
            #             printBoard(board)
            #             turn += 1
            #             turn = turn % 2