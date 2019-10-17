import random

# -------------Setting the board, players and hiding battleships-------------


# Board Ready!!

board = []

for x in range(0,5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print (" ".join(row))


        
# Player Ready!!

print("Let's play Battleship!")
player_1 = input("Enter your name: ")
print(player_1, " Get Ready!!!\n")


 

# Battleships Ready!!

def random_row(board):
    return random.randint(0, len(board)-1)

def random_col(board):
    return random.randint(0, len(board)-1)

ship_row_1 = random_row(board)
ship_col_1 = random_col(board)
#print(ship_row_1, ship_col_1)

ship_row_2 = random_row(board)
ship_col_2 = random_col(board)
#print(ship_row_2, ship_col_2)

print_board(board)


# ----------------------------Playing the game----------------------------



hit_count = 0

for turn in range(20):
    guess_row = int(input("\nGuess Row: (allowed values: 0-4) "))
    guess_col = int(input("Guess Col: (allowed values: 0-4)"))

    if (guess_row == ship_row_1 and guess_col == ship_col_1) or (guess_row == ship_row_2 and guess_col == ship_col_2):
            hit_count = hit_count + 1
            board[guess_row][guess_col] = "*"
            print ("\nCongratulations! ")
            if hit_count == 1:
                   print("You sunk first battleship!\n") 
            elif hit_count == 2:
                print("You sunk second battleship!\n")
                print_board(board)
                break
    else:
        if (guess_row < 0 or guess_row > 4)  or (guess_col < 0 or guess_col > 4):
                   print ("Oops, that's not even in the ocean.\n")
        elif(board[guess_row][guess_col] == "X"):
                   print ("You guessed that one already.\n")
        else:
            print ("You missed my battleship!\n")
            board[guess_row][guess_col] = "X"
        print (turn + 1, "turn")
    print_board(board)
    
if hit_count == 2:
    print("Congratulations ", player_1," You Win!!")
else:
    print("Sorry ", player_1," You Lose.")
print ("Ship 1 is hidden:")    
print (ship_row_1)
print (ship_col_1)

print ("Ship 2 is hidden:")    
print (ship_row_2)
print (ship_col_2)