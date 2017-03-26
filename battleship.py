from random import randint                        #importina a randint method

board = []

for x in range(5):
    board.append(["O"] * 5)                       #CREATE 5*5 MATRIX


def print_board(board):                           #define a method print_board
    for row in board:
        print (" ".join(row))                     #USE TO REPLACE , WITH "


print ("Let's play Battleship!")
print_board(board)                                #calling print_board


def random_row(board):                            #makin a function random_row
    return randint(0,len(board) - 1)


def random_col(board):                            #making a function random_col
    return randint(0,len(board[0]) - 1)


ship_row = random_row(board)                      #assign values to variables as ship_row and ship_col
ship_col = random_col(board)
print (ship_row)
print (ship_col)

for turn in range(4):                            #creating a loop which gives user 4 tries to guess the location of ship
    if turn == 3:
        print ("Over")

    else:
        print ("Turn", turn + 1)
        guess_row = int(input("Guess Row"))
        guess_col = int(input("Guess_Col"))

        if guess_row == ship_row and guess_col == ship_col:
            print ("Congratulations! You sunk my battleship!")
            break
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print ("Oops, its not even in the ocean.")
            elif (board[guess_row][guess_col]=="x"):
                print ("You quizzed dat already.")
            else:
                print ("You missed my battleship")
                board[guess_row][guess_col]="x"
                print_board(board)