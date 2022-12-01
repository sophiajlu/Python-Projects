# Sophia Lu, sjlu@usc.edu
# ITP 115, Spring 2021
# Assignment 8
# Description:
# This program creates a two player Tic Tac Toe game

# importing TicTacToeHelper
import TicTacToeHelper

# creating functions
# def isValidMove():

def isValidMove(boardList, spot):
    # checking if the number entered is still in the board
    if spot in boardList:
        valid = True
    else:
        valid = False
    return valid

def updateBoard(boardList, spot, playerLetter):
    boardList[int(spot)] = playerLetter

# game play if x is first player
def playXGame():
    initialBoard = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    moveCounter = 0
    checkWinner = "n"
    while checkWinner == "n":
        # printing board
        TicTacToeHelper.printUglyBoard(initialBoard)
        # player x turn
        if moveCounter % 2 == 0:
            turn = "x"
            validity = False
            while validity == False:
                space = input("Player x, pick a spot: ")
                validity = isValidMove(initialBoard, space)
                if validity == False:
                    print("Invalid move, please try again.")
                else:
                    # calling updateBoard() function
                    updateBoard(initialBoard, space, turn)
        # player o turn
        elif moveCounter % 2 == 1:
            turn = "o"
            validity = False
            while validity == False:
                space = input("Player o, pick a spot: ")
                validity = isValidMove(initialBoard, space)
                if validity == False:
                    print("Invalid move, please try again.")
                else:
                    # calling updateBoard() function
                    updateBoard(initialBoard, space, turn)
        # updating counter in while loop
        moveCounter += 1
        # checking for winner in each round
        checkWinner = TicTacToeHelper.checkForWinner(initialBoard, moveCounter)

    # exiting the while loop
    TicTacToeHelper.printUglyBoard(initialBoard)
    print("\nGame Over!")
    # printing who won
    if checkWinner == "x":
        print("Player x is the winner!")
    elif checkWinner == "y":
        print("Player o is the winner!")
    elif checkWinner == "s":
        print("Stalemate reached!")

# game play is o if first player
def playOGame():
    initialBoard = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    moveCounter = 0
    checkWinner = "n"
    while checkWinner == "n":
        # printing board
        TicTacToeHelper.printUglyBoard(initialBoard)
        # player x turn
        if moveCounter % 2 == 0:
            turn = "o"
            validity = False
            while validity == False:
                space = input("Player o, pick a spot: ")
                validity = isValidMove(initialBoard, space)
                if validity == False:
                    print("Invalid move, please try again.")
                else:
                    # calling updateBoard() function
                    updateBoard(initialBoard, space, turn)
        # player o turn
        elif moveCounter % 2 == 1:
            turn = "x"
            validity = False
            while validity == False:
                space = input("Player x, pick a spot: ")
                validity = isValidMove(initialBoard, space)
                if validity == False:
                    print("Invalid move, please try again.")
                else:
                    # calling updateBoard() function
                    updateBoard(initialBoard, space, turn)
        # updating counter in while loop
        moveCounter += 1
        # checking for winner in each round
        checkWinner = TicTacToeHelper.checkForWinner(initialBoard, moveCounter)

    # exiting the while loop
    TicTacToeHelper.printUglyBoard(initialBoard)
    print("\nGame Over!")
    # printing who won
    if checkWinner == "x":
        print("Player x is the winner!")
    elif checkWinner == "y":
        print("Player o is the winner!")
    elif checkWinner == "s":
        print("Stalemate reached!")


# creating main:
def main():
    print("Welcome to Tic Tac Toe!")
    again = "y"
    # while loop for repepating entire game
    while again.lower() == "y":
        # decide who the first player is
        firstPlayer = input("Which player would like to go first (x/o)? ").lower()
        while firstPlayer != "x" and firstPlayer != "o":
            print("Invalid input.")
            firstPlayer = input("Which player would like to go first (x/o)? ").lower()
        if firstPlayer == "x":
            playXGame()
        elif firstPlayer == "o":
            playOGame()

        # updating while loop
        again = input("Would you like to play another round (y/n)? ")
    print("Goodbye!")


# calling main:
main()