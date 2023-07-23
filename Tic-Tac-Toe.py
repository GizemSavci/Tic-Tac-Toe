print("Welcome to Tic Tac Toe Game!")
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
CurrentPlayer = "X"
Winner = None

#Board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")    
    print(board[0] + " | " + board[1] + " | " + board[2])
#printBoard(board)

#Player Input
def PlayerInput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == " ":
        board[inp-1] = CurrentPlayer
    else:
        print("Oops! Player is already in that spot.")