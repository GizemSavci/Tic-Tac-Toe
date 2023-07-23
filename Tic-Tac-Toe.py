print("Welcome to Tic Tac Toe Game!")
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")    
    print(board[0] + " | " + board[1] + " | " + board[2])

printBoard(board)
