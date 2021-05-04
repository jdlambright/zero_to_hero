from IPython.display import clear_output
import random


board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
game_on = True

def display_board(board):
    clear_output()
    print("   |   |   ")
    print(' ' + board[1] + ' ' + '|' + ' ' + board[2] + ' ' + '|' + ' ' + board[3] + ' ')
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(' ' + board[4] + ' ' + '|' + ' ' + board[5] + ' ' + '|' + ' ' + board[6] + ' ')
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(' ' + board[7] + ' ' + '|' + ' ' + board[8] + ' ' + '|' + ' ' + board[9] + ' ')
    print("   |   |   ")

def player_input():
    marker = " "
    while marker != "X" and marker != "O":
        marker = input("Player1: Choose X or O: ").upper()
    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")


def player_input():

    marker = " "
    while marker != "X" and marker != "O":
        marker = input("Player1: Choose X or O: ").upper()
    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")


def place_marker(board, marker, position):

    board[position] = marker


def win_check(board, mark):

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the bottom
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the top
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the left
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    return board[position] == " "