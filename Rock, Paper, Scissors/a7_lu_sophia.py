# Sophia Lu, sjlu@usc.edu
# ITP 115, Spring 2021
# Assignment 7
# Description:
# This program plays rock, paper, scissors between the user and the computer

# importing random
import random

# defining displayMenu()
def displayMenu():
    print("\nWelcome! Let's play rock, paper, scissors.")
    print("The rules of the game are:")
    print("\tRock smashes scissors")
    print("\tScissors cut paper")
    print("\tPaper covers rock")
    print("\tIf both the choices are the same, it's a tie")

# defining computerChoice()
def computerChoice():
    computerChoice = random.randrange(0, 3)
    return computerChoice

# defining getPlayerChoice()
def getPlayerChoice():
    print("Please choose (0) for rock, (1) for paper or (2) for scissors")
    playerChoice = 4
    # while loop so user enters correct input
    while playerChoice != 0 and playerChoice != 1 and playerChoice != 2:
        playerChoice = int(input("> "))
    return playerChoice

# defining playRound()
def playRound(computerChoice, playerChoice):
    # output to user
    if playerChoice == 0:
        playerWord = "Rock"
    elif playerChoice == 1:
        playerWord = "Paper"
    elif playerChoice == 2:
        playerWord = "Scissors"
    print("You chose", playerWord)

    if computerChoice == 0:
        computerWord = "Rock"
    elif computerChoice == 1:
        computerWord = "Paper"
    elif computerChoice == 2:
        computerWord = "Scissors"
    print("The computer chose", computerWord)

    # defining winner
    if playerChoice == computerChoice:
        print("You tied, no one wins the round.")
        result = 0
    elif playerChoice == 0 and computerChoice == 1:
        print("Paper covers rock. The computer wins!")
        result = -1
    elif playerChoice == 0 and computerChoice == 2:
        print("Rock smashes scissors. You win!")
        result = 1
    elif playerChoice == 1 and computerChoice == 0:
        print("Paper covers rock. You win!")
        result = 1
    elif playerChoice == 1 and computerChoice == 2:
        print("Scissors cut paper. The computer wins!")
        result = -1
    elif playerChoice == 2 and computerChoice == 0:
        print("Rock smashes scissors. The computer wins!")
        result = -1
    elif playerChoice == 2 and computerChoice == 1:
        print("Paper cuts scissors. You win!")
        result = 1
    return result

# defining continueGame()
def continueGame():
    again = "j"
    while again != "y" and again != "n":
        again = input("Would you like to continue playing (y or n)? ").lower()
    if again == "y":
        play = True
    elif again == "n":
        play = False
    return play

# defining main
def main():
    # creating local variables to main()
    tieCount = 0
    playerWins = 0
    computerWins = 0
    repeat = True

    # while statement for game
    while repeat == True:

        # calling functions
        displayMenu()
        gameResult = playRound(computerChoice(), getPlayerChoice())

        # updating win count
        if gameResult == 0:
            tieCount += 1
        elif gameResult == 1:
            playerWins += 1
        else:
            computerWins += 1

        # calling continueGame() and updating while loop
        repeat = continueGame()

    # output to user
    print("\nYou won", playerWins, "game(s).")
    print("The computer won", computerWins, "game(s).")
    print("You tied with the computer", tieCount, "time(s).")
    print("\nThanks for playing!")

# calling main
main()