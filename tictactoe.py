"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

"""Returns True if board is empty"""
def isEmpty(board):
    for row in board:
        for col in row:
            if col != EMPTY:
                return False
    return True

"""Returns True if board is full"""
def isFull(board):
    for row in board:
        for col in row:
            if col == EMPTY:
                return False
    return True

"""Returns the count of a given piece"""
def countPiece(board, piece):
    count = 0
    for row in board:
        for col in row:
            if col == piece:
                count += 1
    return count

"""Returns player who has the next turn on a board."""               
def player(board):
    if isFull(board): 
        return "terminal board reached"
    if isEmpty(board): # board is empty - X makes the first move
        return X
    if countPiece(board, X) > countPiece(board, O): # if number of X pieces on board greater than O pieces, then O moves
        return O
    elif countPiece(board, X) == countPiece(board, O): # if number of X pieces equals number of O pieces, X moves
        return X
            
    raise NotImplementedError

"""Returns set of all possible actions (i, j) available on the board."""
def actions(board):

    allMoves = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                allMoves.add((i,j))
    return allMoves
    raise NotImplementedError

"""Returns the board that results from making move (i, j) on the board."""
def result(board, action):
    new_state = copy.deepcopy(board)
    row, col = action
    thisPlayer = player(board)

    if action not in actions(board):
        raise Exception("action is invalid")
    
    new_state[row][col] = thisPlayer

    return new_state

    raise NotImplementedError

''' Returns True if there is a winner by 3 in a row'''
def rowWinner(board):
    rowItems = set()
    countItems = 0
    rows = len(board)
    rowLength = len(board[0])
    
    for row in range(rows):
        for col in range(rowLength):
            if board[row][col] == EMPTY:
                continue
            else:
                rowItems.add(board[row][col])
                countItems += 1
        if len(rowItems) == 1 and countItems == rowLength:
            return rowItems.pop()
        rowItems = set()
        countItems = 0
    return False

''' Returns True if there is a winner by 3 in a column'''
def colWinner(board):
    colItems = set()
    countItems = 0
    rows = len(board)
    rowLength = len(board[0])
    
    for row in range(rows):
        for col in range(rowLength):
            if board[col][row] == EMPTY:
                continue
            else:
                colItems.add(board[col][row])
                countItems += 1
        if len(colItems) == 1 and countItems == rowLength:
            return colItems.pop()
        colItems = set()
        countItems = 0
    return False

''' Returns True if there is a winner by 3 in either diagonal'''    
def diagWinner(board):
    diagItems = set()
    countItems = 0
    boardLen = len(board)

    for i in range(boardLen):
        if board[i][i] == EMPTY:
            continue
        else:
            diagItems.add(board[i][i])
            countItems += 1
    if len(diagItems) == 1 and countItems == boardLen:
        return diagItems.pop()
    diagItems = set()
    countItems = 0    
    for i in range(boardLen):
        if board[i][boardLen - i - 1] == EMPTY:
            continue
        else:
            diagItems.add(board[i][boardLen - i - 1])
            countItems += 1
    if len(diagItems) == 1 and countItems == boardLen:
        return diagItems.pop()
    return False

"""Returns the winner of the game, if there is one."""        
def winner(board):
    if rowWinner(board) is not False:
        return rowWinner(board)
    elif colWinner(board) is not False:
        return colWinner(board)
    elif diagWinner(board) is not False:
        return diagWinner(board)
    else:
        return None

    raise NotImplementedError

"""Returns True if game is over (by full board - no winner, or by full board - with winner), False otherwise."""
def terminal(board):
    if isFull(board):
        return True
    if winner(board):
        return True
    else:
        return False
    raise NotImplementedError

"""Returns 1 if X has won the game, -1 if O has won, 0 otherwise."""
def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    
    raise NotImplementedError

def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

"""Returns the optimal action for the current player on the board."""
def minimax(board):
    if terminal(board):
        return None
    elif player(board) == X:
        plays = []
        for action in actions(board):
            plays.append([min_value(result(board, action)), action])
        return sorted(plays, key=lambda x: x[0], reverse = True)[0][1]

    elif player(board) == O:
        plays = []
        for action in actions(board):
            plays.append([max_value(result(board, action)), action])
        return sorted(plays, key=lambda x: x[0])[0][1]
        

