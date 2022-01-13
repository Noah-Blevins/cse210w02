# TIC-TAC-TOE
#
# Noah Blevins
#
# CSE210
#
# January 12, 2022

from shutil import move
from typing import Type


def createBoard(symbolsString):
    board = f'''{symbolsString[0]}|{symbolsString[1]}|{symbolsString[2]}\n-+-+-\n{symbolsString[3]}|{symbolsString[4]}|{symbolsString[5]}\n-+-+-\n{symbolsString[6]}|{symbolsString[7]}|{symbolsString[8]}'''
    
    print(board)

def gameSetup():
    symbolsString = []
    for i in range(9):
        symbolsString.append(i + 1)
    return symbolsString


def checkEndCondition(symbolsString, turnCount):
    if symbolsString[0] == symbolsString[1] == symbolsString[2]:
        return True
    elif symbolsString[3] == symbolsString[4] == symbolsString[5]:
        return True
    elif symbolsString[6] == symbolsString[7] == symbolsString[8]:
        return True
    elif symbolsString[0] == symbolsString[3] == symbolsString[6]:
        return True
    elif symbolsString[1] == symbolsString[4] == symbolsString[7]:
        return True
    elif symbolsString[2] == symbolsString[5] == symbolsString[8]:
        return True
    elif symbolsString[0] == symbolsString[4] == symbolsString[8]:
        return True
    elif symbolsString[2] == symbolsString[4] == symbolsString[6]:
        return True
    elif turnCount == 9:
        return True
    else:
        return False    


def makeMove(board, moveCounter):
    playerNumber = moveCounter%2 + 1
    pickingMove = True
    while pickingMove:
        try:
            moveLocation = int(input(f"Player {playerNumber}, make your move: ")) - 1
            if board[moveLocation] != 'X' and board[moveLocation] != 'O':
                if playerNumber == 1:
                    board[moveLocation] = 'X'
                elif playerNumber == 2:
                    board[moveLocation] = 'O'
                pickingMove = False
            else:
                print('Please choose an open spot.')
        except IndexError as index_error:
            print("Please choose a valid open spot.")
        except ValueError as value_error:
            print("Please choose a valid open spot.")

def endGame(moveCount):
    if moveCount == 9:
        print("Cat! No winners today!")
    else:
        player = (moveCount - 1)%2 + 1
        print(f"Player {player} wins! Good job!")


def main():
    print("Welcome to Tic-Tac-Toe!")
    
    moveCounter = 0
    
    board = gameSetup()
    
    gameRunning = True
    
    while gameRunning:
        createBoard(board)
        makeMove(board, moveCounter)
        moveCounter += 1
        gameOver = checkEndCondition(board, moveCounter)
        if gameOver == True:
            gameRunning = False
    
    endGame(moveCounter)
    
if __name__ == "__main__":
    main()
        