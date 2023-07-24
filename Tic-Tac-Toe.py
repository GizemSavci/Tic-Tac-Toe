print("Welcome to Tic Tac Toe Game!")
print(" /\\_/\\ ")
print("( o.o )")
print(" > ^ < ")
print("")
print("")
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
currentPlayer = "X"
winner = None
gameRunning = True

#Board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")    
    print(board[6] + " | " + board[7] + " | " + board[8])
#printBoard(board)

#Player Input
def PlayerInput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == " ":
        board[inp-1] = currentPlayer
    else:
        print("Oops! Player is already in that spot.")

#check
def checkhorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != " ":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != " ":
        winner = board[4]
        return True
    elif board[6] == board[7] == board[8] and board[6] != " ":
        winner = board[6]
        return True

    
def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != " ":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != " ":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != " ":
        winner = board[2]
        return True

    
def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != " ":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != " ":
        winner = board[2]
        return True

#switch player
def switchPlayer():
    global currentPlayer, gameRunning
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

def checkWin():
    global gameRunning
    if checkhorizontal(board) or checkVertical(board) or checkDiagonal(board):
        printBoard(board)
        print(f"The winner is {winner}")
        gameRunning = False

#tie check
def checkTie(board):
    global gameRunning
    if " " not in board:
        printBoard(board)
        print("It is a tie.")
        gameRunning = False

while gameRunning:
    printBoard(board)
    PlayerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()