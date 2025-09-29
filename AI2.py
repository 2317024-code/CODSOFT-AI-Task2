import math

board = [" " for _ in range(9)]

def printboard(board):
    for r in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(r) + " |")
        
def checkwin(board):
    wincombo = [
        [0,1,2], [3,4,5], [6,7,8], #row
        [0,3,6], [1,4,7], [2,5,8], #col
        [0,4,8], [2,4,6] #diag
    ]
    
    for c in wincombo:
        if board[c[0]] == board[c[1]] == board[c[2]] != " ":
            return board[c[0]]
    return None

def isfull(board):
    return " " not in board

def minmax(board, dep, alp, bet, ismax):
    winner = checkwin(board)
    if winner == "0":
        return 1
    elif winner == "X":
        return -1
    elif isfull(board):
        return 0
    
    if ismax:
        maxe = -math.inf
        for i in range(9):
           if board[i] == " ":
               board[i]  = "0"
               e = minmax(board, dep+1, alp, bet, False)
               board[i] = " "
               maxe = max(maxe, e)
               alp = max(alp, e)
               if bet <= alp:
                   break
        return maxe
    else:
        mine = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                e = minmax(board, dep+ 1, alp, bet, True)
                board[i] = " "
                mine = min(mine, e)
                bet = min(bet, e)
                if bet <= alp:
                    break
        return mine
    
#Best Way
def best_move(board):
    best_val = -math.inf
    m = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "0"
            move = minmax(board, 0, -math.inf, math.inf, False)
            board[i] = " "
            if move > best_val:
                best_val = move
                m = i
    return m

def play_game():
    print("Welcome")
    printboard(board)
    while True:
        h = int(input("Enter your move(1-9): ")) - 1
        if board[h] == " ":
            board[h] = "X"
        else:
            print("Invalid move. Try again.")
            continue
        
        printboard(board)
        if checkwin(board) == "X":
            print(" You win!")
            break
        elif isfull(board):
            print("It's a draw!")
            break
            
        print("AI is making a move..")
        ai = best_move(board)
        board[ai] = "0"
        printboard(board)
        if checkwin(board) == "0":
            print("AI wins")
            break
        elif isfull(board):
            print("It is a draw!")
            break

if __name__ == "__main__":
    play_game()