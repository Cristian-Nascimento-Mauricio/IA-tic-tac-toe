import copy, math , random


def didAnyoneWin(board):

    # Verificar linhas
    for row in range(3):
        if board[row][0] != "" and board[row][0] == board[row][1] == board[row][2]:
            return board[row][0]

    # Verificar colunas
    for col in range(3):
        if board[0][col] != "" and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col] 

            
    # Verificar diagonal principal
    if board[0][0] != "" and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0] 

    # Verificar diagonal secundária
    if board[0][2] != "" and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2] 

    if len(voidSpace(board)) != 0:
        return False

    return "draw"

def voidSpace(board):
    list = []

    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                list.append([row,col])

    return list            


def bestAction(board,player="O",winner="O",loser="X"):

    possibilityMove = voidSpace(board)
    bestMove = None
    bestValue = None

    for possibility in possibilityMove:
        board[possibility[0]][possibility[1]] = player
        value = miniMax(board,player,winner,loser)
        board[possibility[0]][possibility[1]] = ""

        if bestValue is None:
            bestMove = possibility
            bestValue = value
        elif player == winner:
            if value > bestValue:
                bestValue = value
                bestMove = possibility
        elif player == loser:    
            if value < bestValue:
                bestValue = value
                bestMove = possibility


    return bestMove


def futureMove(board,pos,player="O"):
    copyBoard = copy.deepcopy(board)  
    copyBoard[pos[0]][pos[1]] = player
    return copyBoard



def miniMax(board,player="O",winner="O",loser="X"):

    playerWinner = didAnyoneWin(board)

    if playerWinner: 
        if playerWinner == loser:
            return -1
        elif playerWinner == winner:
            return 1
        else:
            return 0    

    player = "X" if player == "O" else "O"

    possibilityMove = voidSpace(board)
    bestValue = None

    for possibility in possibilityMove:
        board[possibility[0]][possibility[1]] = player
        value = miniMax(board,player,winner,loser)
        board[possibility[0]][possibility[1]] = ""

        if bestValue is None:
            bestValue = value
        elif player == winner:
            if value > bestValue:
                bestValue = value
        elif player == loser:    
            if value < bestValue:
                bestValue = value

    return bestValue
