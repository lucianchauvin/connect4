board=[]
count = [0,0,0,0,0,0,0]
turn = '\33[34m' + "X" + '\33[0m'
for row in range(6): board.append(["_","_","_","_","_","_","_"])
def print_board(board):
    n = 5
    for row in board:
        line = str(n) + "|"
        for col in row: line = line + col + "|"
        print(line)
        n-=1
    print("  0 1 2 3 4 5 6\n\n")
def place_mark():
    global board, turn
    if board_check() == '\33[34m' + "X" + '\33[0m' or board_check() == '\33[33m' + "O" + '\33[0m':
        print('\033[6m' + "The winner is " + board_check() + '\033[0m')
        return
    while True:
        i = input(turn + " Pick Move: ")
        try:
            if 5- count[int(i)] < 0: raise
            board[5 - count[int(i)]][int(i)] = turn
            count[int(i)] += 1
            break
        except: print("Invalid input!") 
    print_board(board) 
    board_check()
    if turn == '\33[34m' + "X" + '\33[0m': turn = '\33[33m' + "O" + '\33[0m' 
    else: turn = '\33[34m' + "X" + '\33[0m'
    place_mark()
def board_check():
    for row in range(len(board)): 
        for col in range(len(board[row])-3):
            if (board[row][col] != "_") and (board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3]): return board[row][col]
    for row in range(len(board)-3): 
        for col in range(len(board[row])):
            if (board[row][col] != "_") and (board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col]): return board[row][col]
    for row in range(len(board)-3):
        for col in range(3,len(board[row])):
            if (board[row][col] != "_") and (board[row][col] == board[row+1][col-1] == board[row+2][col-2] == board[row+3][col-3]): return board[row][col]
    for row in range(len(board)-3):
        for col in range(len(board[row])-3):
            if (board[row][col] != "_") and (board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3]): return board[row][col]
print_board(board)
place_mark()