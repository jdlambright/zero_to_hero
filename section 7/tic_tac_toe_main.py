from IPython.display import clear_output
import random


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
    if board[position] != "X" or board[position] != "O":
        return True
    else:
        return False


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) \n'))

    return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')
BOARD= ["x","1","2","3","4","5","6","7","8","9"]
display_board(BOARD)

while True:
    BOARD= [" "]*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter y or n. ')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        while game_on:
            if turn == 'Player 1':
                display_board(BOARD)
                position = player_choice(BOARD)
                place_marker(BOARD, player1_marker, position)

                if win_check(BOARD, player1_marker):
                    display_board(BOARD)
                    print('Congratulations! You have won the game!')
                    game_on = False
                else:
                    if full_board_check(BOARD):
                        display_board(BOARD)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 2'

            else:
                # Player2's turn.

                display_board(BOARD)
                position = player_choice(BOARD)
                place_marker(BOARD, player2_marker, position)

                if win_check(BOARD, player2_marker):
                    display_board(BOARD)
                    print('Player 2 has won!')
                    game_on = False
                else:
                    if full_board_check(BOARD):
                        display_board(BOARD)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 1'

    if not replay():
        break

        t2Kj72Gr