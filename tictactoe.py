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


def player(board):
    """
    Returns player who has the next turn on a board.
    In the initial board state, X gets the first move. The player alternates with each additional move.
    Any return value is acceptable if a terminal board is provided as input
    """
    # Count # of moves made
    filled = 0
    for i, row in enumerate(board):
        for j, element in enumerate(row):
            if element != EMPTY:
                filled += 1

    # If terminal board is input, return None.
    # if terminal(board):
    #     return None
    # If an even number of moves have been made, it's X's turn
    if filled % 2 == 0:
        return X
    # If an odd number of moves have been made, it's O's turn
    else:
        return O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    Each action should be represented as a tuple (i,j) where i is the row of the move and j is the row of the move.
    Any return value is acceptable if a terminal board is input.
    """
    # if terminal(board):
    #     return None
    set_of_actions = set()
    for i, row in enumerate(board):
        for j, element in enumerate(row):
            if element == EMPTY:
                action = (i, j)
                set_of_actions.add(action)
    return set_of_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    Raise exception if 'action' isn't a valid action for the board
    """
    board_copy = copy.deepcopy(board)
    i, j = action
    valid = [0, 1, 2]
    if board_copy[i][j] != EMPTY or i not in valid or j not in valid:
        raise Exception("Invalid move")
    else:
        board_copy[i][j] = player(board)
        return board_copy



def winner(board):
    # Tries to find a winner in one of the three rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return row[0]

    # Tries to find a winner in one of the three columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            return board[0][col]

    # Tries to find a winner in one of the diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] != EMPTY:
        return board[2][0]

    # If there is no winner, return None
    return None

def terminal(board):
    complete = True
    for row in board:
        for element in row:
            if element == EMPTY:
                complete = False
    if winner(board) == X or winner(board) == O:
        return True

    if complete:
        return True

    return False



def utility(board):

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action (i,j) for the current player on the board.
    If the board is terminal, return None
    If multiple moves are equally optimal, any one of them is acceptable.
    """
    if terminal(board):
        return None
    if player(board) == X:
        best_value = -999999
        best_action = None
        for action in actions(board):
            minimum = min_value(result(board, action))
            if minimum > best_value:
                best_value = minimum
                best_action = action
        return best_action
    elif player(board) == O:
        best_value = 999999
        best_action = None
        maximum = None
        for action in actions(board):
            maximum = max_value(result(board, action))
            if maximum < best_value:
                best_value = maximum
                best_action = action
        return best_action

    return None

def max_value(state):
    v = -999999
    if terminal(state):
        return utility(state)
    for action in actions(state):
        v = max(v, min_value(result(state, action)))
    return v

def min_value(state):
    v = 999999
    if terminal(state):
        return utility(state)
    for action in actions(state):
        v = min(v, max_value(result(state, action)))
    return v
