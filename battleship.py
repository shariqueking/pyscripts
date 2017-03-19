from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)   # creats 5x5 matrics


def print_board(board):
    for row in board:
        print(" ".join(row))   #use to replace , with " "


print("Let's play Battleship!")
print_board(board)


def random_row(board):
    return randint(0, len(board) - 1)    #give random value of rows


def random_col(board):
    return randint(0, len(board[0]) - 1)    #give random value of column


ship_row = random_row(board)
ship_col = random_col(board)
print (ship_row)                   #printing the ship_col and ship_row
print (ship_col)

for turn in range(4):                    # loop which give only 4 turn to player
    if turn == 3:
        print("Game Over")

    else:
        print("Turn", turn + 1)         # display user the count of the turn
        guess_row = int(input("Guess Row:"))     #taking inputs from user
        guess_col = int(input("Guess Col:"))

        if guess_row == ship_row and guess_col == ship_col:    #checking for win
            print("Congratulations! You sunk my battleship!")
            break                                                 # if win the break
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):   #checking for out of range guess
                print("Oops, that's not even in the ocean.")
            elif (board[guess_row][guess_col] == "X"):         # check already guessed guess
                print("You guessed that one already.")
            else:
                print("You missed my battleship!")
                board[guess_row][guess_col] = "X"     # printing  X in place of O ,if guess is wrong

                print_board(board)