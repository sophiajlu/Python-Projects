# Sophia Lu, sjlu@usc.edu
# ITP 115, Spring 2021
# Assignment 5
# Description:
# This program counts how many times a letter/character appears in a sentence
# This program also plays a game where the user gains points by rolling a winning number on a 20 sided dice

# importing random
import random

# PART 1

# creating variables
specialCount = 0
alphabet = "abcdefghijklmnopqrstuvwxyz"

# display to user
print("PART 1 - Character Counter")

# user input
sentence = input("Please enter a sentence: ")

# ouput to user
print("\nHere is the character distribution:")
print()

# for loop for special characters
for character in sentence:
    if character.lower() not in alphabet and not character == " ":
            specialCount += 1
if specialCount == 0:
    print("special character: NONE")
else:
    print("special characters:", (specialCount * "*"))

# for loop for alphabet
for letter in alphabet:
    letterCount = 0
    for character in sentence:
        # branching
        if character.lower() == letter:
            letterCount += 1
    if letterCount == 0:
        print(letter + ": NONE")
    else:
        print(letter + ":", (letterCount * "*"))

# PART 2
print("\nPART 2 - D20 Dice Game")

# creating variables
total_score = 0
caseOne = range(2, 21, 2)
caseTwo = range(1, 20, 2)
caseThree = range(5, 11)
caseFour = range(10, 21, 2)
caseFive = range(3, 21, 3)

# Outer Loop
for round in range(1, 11):
    dice = random.randrange(1, 21)
    game = random.randrange(1, 6)
    win = False
    print("\nYou are playing for case", game, "\nYou will win for the following numbers:")
# Branching
    # Case 1 - any even number
    if game == 1:
        for number in caseOne:
            print(number, end=" ")
        print()
        print("\nNow rolling ...\nYou rolled a", str(dice) + "!")
        if dice % 2 == 0:
            win = True

    # Case 2 - any odd number
    elif game == 2:
        for number in caseTwo:
            print(number, end=" ")
        print()
        print("\nNow rolling ...\nYou rolled a", str(dice) + "!")
        if dice % 2 == 1:
            win = True

    # Case 3 - any number 5 to 10 inclusive
    elif game == 3:
        for number in caseThree:
            print(number, end=" ")
        print()
        print("\nNow rolling ...\nYou rolled a", str(dice) + "!")
        if dice >= 5 and dice <= 10:
            win = True

    # Case 4 - greater than 10 and multiples of 2
    elif game == 4:
        for number in caseFour:
            print(number, end=" ")
        print()
        print("\nNow rolling ...\nYou rolled a", str(dice) + "!")
        if dice >= 10 and dice % 2 == 0:
            win = True

    # Case 5 - multiples of 3
    elif game == 5:
        for number in caseFive:
            print(number, end=" ")
        print()
        print("\nNow rolling ...\nYou rolled a", str(dice) + "!")
        if dice % 3 == 0:
            win = True

    # Calculating points
    if win == True:
        total_score += 50
        print("You won 50 points! :)")
    else:
        print("You didn't win :(")

# output to user
print("\nYour total score is:", total_score)
print("Thanks for playing!")


