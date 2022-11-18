board, count, turn = [["_", "_", "_", "_", "_", "_", "_"] for x in range(6)], [0]*7, '\33[34m' + "X" + '\33[0m' # creates board, initializes the amout in each stack so we can then know where to put a new coin at what y level
def print_board(board): print("\n"*10 + "\n".join(["|".join(x) for x in board]) + "\n0 1 2 3 4 5 6\n") #prints the board with some fancy stuff for rows and cols
def place_mark(): #recursive function, calls itself till there is a winner. Basically a while loop until the board_check function returns a winner
    global board, turn
    if (a := board_check()) == '\33[34m' + "X" + '\33[0m' or board_check() == '\33[33m' + "O" + '\33[0m': return print('\033[6m' + "The winner is " + a + '\033[0m') #print out whos the winner 
    while True: #repeats until a valid move is selected
        try: #basically we try to input the players input on the board and if it is out of range it will "raise an error"
            if 5 - count[(i := int(input(turn + " Pick Move: ")))] < 0: raise  # raises the error if out of bounds in the negative direction
            board[5 - count[i]][i], count[i] = turn, count[i] + 1
            break #breaks the while loop and allows the function to move on
        except: print("Invalid input!") #this is where if there is an error raised in the try statment we will make the player pick again by the while loop repeating
    print_board(board) #prints the board after a valid move
    board_check() #checks if there is any wins on the board and if there is the next recursive call of the place_mark function will end and print the winner
    turn = ('\33[34m' + "X" + '\33[0m' if turn == '\33[33m' + "O" + '\33[0m' else '\33[33m' + "O" + '\33[0m')
    place_mark() #calls this function again until there is a winner
def board_check(): #finds if there is a win
    if (a := "".join("".join(x) for x in [[board[row][col] if (board[row][col] != "_") and (board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3]) else "" for col in range(len(board[row])-3)] for row in range(len(board))]))!= "": return a
    if (a := "".join("".join(x) for x in [[board[row][col] if (board[row][col] != "_") and (board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col]) else "" for col in range(len(board[row]))] for row in range(len(board)-3)])) != "": return a
    if (a := "".join("".join(x) for x in [[board[row][col] if (board[row][col] != "_") and (board[row][col] == board[row+1][col-1] == board[row+2][col-2] == board[row+3][col-3]) else "" for col in range(3, len(board[row]))] for row in range(len(board)-3)])) != "": return a
    if (a := "".join("".join(x) for x in [[board[row][col] if (board[row][col] != "_") and (board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3]) else "" for col in range(len(board[row])-3)] for row in range(len(board)-3)])) != "": return a 
print_board(board) #the first time the board is printed
place_mark() #the inital recursive call that starts the game loop