# Sophia Lu, sjlu@usc.edu
# ITP-115, Spring 2021
# Assignment 6
# Description:
# this program asks users to guess a jumbled word and encrypts/decrypts a user's message

# importing random
import random

# PART 1 - Word Jumble Game
# creating list
wordsList = ["penguin", "bread", "plant", "ship", "rain"]

# picking word
word = random.choice(wordsList)

# turning word into a list
wordLetters = list(word)

# variables
length = len(word)
jumbledList = [] # empty list
guesses = 1
points = 10

# for loop for jumbling letters
for number in range(length):
    letter = random.choice(wordLetters)
    jumbledList.append(letter)
    wordLetters.remove(letter)


# convert list back into string
jumbledWord = "".join(jumbledList)

# output to user and user input
print("The jumbled word is \"" + jumbledWord + "\"")
guess = input("Please enter your guess (-1 if you want a hint): ")

# while loop for guessing
while guess != word:
    if guess == "-1":
        points -= 5
        if word == "penguin":
            print("Hint: This animal is a bird")
        elif word == "bread":
            print("Hint: You buy this at a bakery")
        elif word == "plant":
            print("Hint: You need to water it")
        elif word == "ship":
            print("Hint: This floats on water")
        elif word == "rain":
            print("Hint: Opposite of sun")
    print("Try again.")
    guesses += 1
    guess = input("Please enter your guess (-1 if you want a hint): ")

# final output to user
print("You got it!")
print("It took you", guesses, "tries.")
if points == 10:
    print("You earn", points, "points for solving the jumble with no hints!")
else:
    print("You earn", points, "points for solving the jumble with a hint.")

# PART 2 - Encrypt/Decrypt

# user input
msg = input("\nEnter a message: ")
shift = int(input("Enter a number to shift by (0-25): "))

# creating variables and alphabets
# msg_lower = msg.lower()
alpha = "abcdefghijklmnopqrstuvwxyz"
alphabet = list(alpha)
print("alphabet =", alphabet)
slice = alphabet[0: shift]
new_alpha = alphabet + slice
del new_alpha[0: shift]
print("new alpha =", new_alpha)
encrypted = ""
decrypted = ""

# encrypting message
for letter in msg.lower():
    if letter in alphabet:
        index = alpha.index(letter)
        new_letter = new_alpha[index]
        encrypted = encrypted + new_letter
    else:
        encrypted = encrypted + letter

# user output
print("Encrypting message....")
print("\tEncrypted message:", encrypted)

# decrypting message
for letter in encrypted:
    if letter in alphabet:
        index = new_alpha.index(letter)
        new_letter = alpha[index]
        decrypted = decrypted + new_letter
    else:
        decrypted = decrypted + letter

# user output
print("Decrypting message ....")
print("\tDecrypted message:", decrypted)
print("\tOriginal message:", msg)

