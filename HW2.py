# Created on Dec, 2019
# Хрестики нулики 0.1

import random

CHOOSE_POSITION = 'Please choose your start position, select between: (1-9): '
CONGRAT = ', Congratulations! You won this game!'
DRAW = 'The game ended in a draw...win friedships'
EMPTY = ''
FIRST_TURN = 'Player 1, Start the game, please choose x or o: '
LINE = "-------------"
O_MARKER = 'o'
P1 = 'Player 1'
P2 = 'Player 2'
PLAY_AGAIN_CHOICE = 'Could you play again? Enter y for confirm or n to decline new game '
SLASH = "|"
SPACE = '$'
INITIAL_WELLCOME = 'Welcome to the best Tic Tac Toe!'
X_MARKER = 'x'
Y ='y'
YOUR_TURN = ", it's your turn!"

def printGameBoard(gameboard):
    gameboard =  gameboard
    print (LINE)
    for i in range(3):
        print( SLASH, gameboard[0+i*3], SLASH, gameboard[1+i*3], SLASH, gameboard[2+i*3], SLASH)
    print(LINE)

def playerInput():
    marker = EMPTY
    while marker != X_MARKER and marker !=O_MARKER:
        marker = input(FIRST_TURN)
    player_1 = marker
    if player_1 == X_MARKER:
        player_2 = O_MARKER
    else:
        player_2 = X_MARKER
    return (player_1, player_2)

def makeTurn(gameboard, marker, position):
    gameboard[position-1] = marker
    return gameboard

def ifWonCheck(gameboard, marker):
    j=0
    for i in range(3):
        return ((gameboard[0+i*3] == gameboard[1+i*3] == gameboard[2+i*3] == marker) or
        (gameboard[i+j*3] == gameboard[i+(j+1)*3] == gameboard[i+(j+2)*3] == marker) or
        (gameboard[0+j*3] == gameboard[1+(j+1)*3] == gameboard[2+(j+2)*3] == marker) or
        (gameboard[2+j*3] == gameboard[1+(j+1)*3] == gameboard[0+(j+2)*3] == marker))

def spaceCheck(gameboard, position):
    return gameboard[position-1] == SPACE

def isFullGameboard(gameboard):
    for i in range(1,10):
        if spaceCheck(gameboard, i):
            return False
    return True #перевірка чи дошка заповнена#

def chooseFirstTurn():
    randInt = random.randint(0,1)
    if randInt == 0:
        return P1
    else:
        return P2

def playerChoice(gameboard):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not spaceCheck(gameboard, position):
        print ('Значення повинно знаходитись в межах 1-9, зробіть свій вибір...')
        try:
            position = int(input(CHOOSE_POSITION))
        except ValueError:
            print ('Помилкове значення')
            position = 0
    return position

def rePlay():
    return input(PLAY_AGAIN_CHOICE).startswith(Y)

def playTheGame(gameboard,turn,playerMarker):
    printGameBoard(gameboard) #показати ігрове поле  # Тепер черга гравця.
    print(turn)
    position = playerChoice(gameboard)
    makeTurn(gameboard,playerMarker,position)
    if ifWonCheck(gameboard,playerMarker): #Перевірка чи гра завершилась пермогою гравця 2
        printGameBoard(gameboard)
        print(turn+ CONGRAT)
        return False
    elif isFullGameboard(gameboard):
        printGameBoard(gameboard)
        print(DRAW)
        return False
    else:
        return turn

if __name__ == '__main__':
    print(INITIAL_WELLCOME)
    while True:
        gameboard = ([SPACE] * 10)[1:]
        print ('Вдалої гри')
        printGameBoard(gameboard)
        player1Marker, player2Marker = playerInput()
        turn = chooseFirstTurn()
        print(turn + YOUR_TURN)
        gameOn = True
        while gameOn: # зупуск гри
            if turn == P1: #Чергра гравця 1
                gameOn = playTheGame(gameboard,turn,player1Marker)
                if turn == gameOn:
                    turn = P2
                else:
                    continue
            elif turn == P2:
                gameOn = playTheGame(gameboard,turn,player2Marker)
                if turn == gameOn:
                    turn = P1
                else:
                    continue
        if not rePlay():
            break


