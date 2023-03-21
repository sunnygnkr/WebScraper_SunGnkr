import random

from IPython.display import clear_output

game_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']


def display_Board(board):
    clear_output()
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('----------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('----------')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])


def player_input():
    playerInput = ''

    while not (playerInput == 'X' or playerInput == 'O'):
        playerInput = input('Player1 please enter either X or O: ').upper()

    player1 = playerInput

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return player1, player2  # returning as tuple to grab individual values

def cell_Input(board, pos, usrInput):
    board[pos] = usrInput

def is_GameWon(board, userInp):
    return ((board[1] == board[2] == board[3] == userInp) or
            (board[4] == board[5] == board[6] == userInp) or
            (board[7] == board[8] == board[9] == userInp) or
            (board[1] == board[4] == board[7] == userInp) or
            (board[2] == board[5] == board[8] == userInp) or
            (board[3] == board[6] == board[9] == userInp) or
            (board[1] == board[5] == board[9] == userInp) or
            (board[3] == board[5] == board[7] == userInp))

# if is_GameWon(game_board, 'O') or is_GameWon(game_board, 'X'):
#     gameWon = True
# else:
#     gameWon = False

def coin_Flip():
    flip = random.randint(0, 1)

    if flip == 0:
        return 'Player1'
    else:
        return 'Player2'


def isCellAvailable(board, pos):
    return board[pos] == ' '

def check_IsBoard_Full(board):

    for i in range(1, 10):
        if isCellAvailable(board, i):
            return False

    return True


def player_nextInp_Position(board):
    inputPosition = 0

    while (inputPosition not in range(1, 10)) or (isCellAvailable(board, inputPosition) == False):
        inputPosition = int(input('Please select a position between 1-9: '))

    return inputPosition


def playAgain():
    play_Again = input('Do you want to play again (Y/N): ').upper()

    return play_Again == 'Y'


# Actual game logic
print('Welcome to Tic_Tac_Toe game:\n')
# autoIndex = random.randint(1, 10)
while True:
    new_board = [' '] * 10
    player1_input, player2_input = player_input()

    turn = coin_Flip()
    print(turn + ' will go first')

    playGame = input('Ready to play? Y or N ->  ').upper()

    if playGame == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:
        # Check if it's player1 turn
        if turn == 'Player1':
            # display_Board(new_board)
            position = player_nextInp_Position(new_board)
            cell_Input(new_board, position, player1_input)
            display_Board(new_board)
            print('\n')

            # Check if game is a tie
            if check_IsBoard_Full(new_board):
                # display_Board(new_board)
                print("Game is tied")
                game_on = False

            # Check if player1 won the game
            else:
                if is_GameWon(new_board, player1_input):
                    display_Board(new_board)
                    print('Player1 has won the game')
                    game_on = False
                else:
                    turn = 'Player2'

        else:
            # display_Board(new_board)
            position2 = player_nextInp_Position(new_board)
            cell_Input(new_board, position2, player2_input)
            display_Board(new_board)
            print('\n')

            # Check if game is a tie
            if check_IsBoard_Full(new_board):
                display_Board(new_board)
                print("Game is tied")
                game_on = False

            # Check if player1 won the game
            else:
                if is_GameWon(new_board, player2_input):
                    display_Board(new_board)
                    print('Player2 has won the game')
                    game_on = False
                else:
                    turn = 'Player1'

    if not playAgain():
        break
