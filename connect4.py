board=[] #creates board
count = [0,0,0,0,0,0,0] #initializes the amout in each stack so we can then know where to put a new coin at what y level
turn = '\33[34m' + "X" + '\33[0m' #initalizes the turn (starting x) with the color
for row in range(6): board.append(["_","_","_","_","_","_","_"]) #creates the board
def print_board(board): #prints the board with some fancy stuff for rows and cols
    n = 5
    for row in board:
        line = str(n) + "|"
        for col in row: line = line + col + "|"
        print(line)
        n-=1
    print("  0 1 2 3 4 5 6\n\n")
def place_mark(): #recursive function, calls itself till there is a winner. Basically a while loop until the boar_check function returns a winner
    global board, turn
    if board_check() == '\33[34m' + "X" + '\33[0m' or board_check() == '\33[33m' + "O" + '\33[0m': #if board_check returns a winner
        print('\033[6m' + "The winner is " + board_check() + '\033[0m') #print out whos the winner 
        return #end the recursive call
    while True: #repeats until a valid move is selected
        i = input(turn + " Pick Move: ") #gets input
        try: #basically we try to input the players input on the board and if it is out of range it will "raise an error"
            if 5 - count[int(i)] < 0: raise #raises the error if out of bounds in the negative direction 
            board[5 - count[int(i)]][int(i)] = turn #will raises the error if out of bounds in the positive direction
            count[int(i)] += 1 #adds a value to the y stack initiated on line 2, one again so we know where to place the next coin in the same coloumn
            break #breaks the while loop and allows the function to move on
        except: print("Invalid input!") #this is where if there is an error raised in the try statment we will make the player pick again by the while loop repeating
    print_board(board) #prints the board after a valid move
    board_check() #checks if there is any wins on the board and if there is the next recursive call of the place_mark function will end and print the winner
    if turn == '\33[34m' + "X" + '\33[0m': turn = '\33[33m' + "O" + '\33[0m' #changes the turn from x to o and o to x
    else: turn = '\33[34m' + "X" + '\33[0m' #changes the turn from x to o and o to x
    place_mark() #calls this function again until there is a winner
def board_check(): #finds if there is a win
    for row in range(len(board)): #horizontal
        for col in range(len(board[row])-3):
            if (board[row][col] != "_") and (board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3]): return board[row][col]
    for row in range(len(board)-3): #vertical
        for col in range(len(board[row])):
            if (board[row][col] != "_") and (board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col]): return board[row][col]
    for row in range(len(board)-3): #positive diagonal
        for col in range(3,len(board[row])):
            if (board[row][col] != "_") and (board[row][col] == board[row+1][col-1] == board[row+2][col-2] == board[row+3][col-3]): return board[row][col]
    for row in range(len(board)-3):
        for col in range(len(board[row])-3): #negative diagonal
            if (board[row][col] != "_") and (board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3]): return board[row][col]
print_board(board) #the first time the board is printed
place_mark() #the inital recursive call that starts the game loop