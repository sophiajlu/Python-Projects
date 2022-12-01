# Sophia Lu, sjlu@usc.edu
# ITP-115, Spring 2021
# Assignment 3
# Description:
# This program creates a Harry Potter vending machine.
# It determines change and gives a discount.

# Conversions:
# 1 knut = 1 knut
# 1 sickle = 29 knuts
# 1 galleon = 493 knuts

# display to user
print("Please select an item from the vending machine: ")
print("     a) Butterbeer: 58 knuts")
print("     b) Quill: 10 knuts")
print("     c) The Daily Prophet: 7 knuts")
print("     d) Book of Spells: 400 knuts")


# user input
item = input("> ")
price = 0
while item.lower() != "a" and item.lower() != "b" and item.lower() != "c" and item.lower() != "d":
    print("You have entered an invalid option. Please try again.")
    item = input("> ")

# variables
if item.lower() == "a":
     item = "Butterbeer"
     price = 58
elif item.lower() == "b":
    item = "Quill"
    price = 10
elif item.lower() == "c":
    item = "The Daily Prophet"
    price = 7
elif item.lower() == "d":
    item = "Book of Spells"
    price = 400
# else:
#     print("You have entered an invalid option. You will be given a Butterbeer for 58 knuts.")
#     item = "Butterbeer"
#     price = 58


# getting user input for coupon
coupon = input("Will you share this on Instagram (y/n)?: ")

while coupon.lower() != "y" and coupon.lower() != "n":
    print("You have entered an invalid option. Please try again.")
    coupon = input("Will you share this on Instagram (y/n)?: ")
if coupon.lower() == "y":
    print("Thanks! You get 5 knuts off your purchase.")
    coupon = 5
elif coupon.lower() == "n":
    coupon = 0
# else:
#     print("You have entered an invalid option. No coupon will be used.")
#     coupon = 5

# user input for amount of money they want to enter (extra credit)
print("\nYou must now pay", price - coupon, "knuts for your " + item + ". How many of each coin would you like to enter? Enter 0 if none.")
galleons = int(input("Galleons (equals 493 knuts): "))
galValue = galleons * 493
sickles = int(input("Sickles (equals 29 knuts): "))
sicValue = sickles * 29
knuts = int(input("Knuts (equals 1 knut): "))
cost = galValue + sicValue + knuts
while cost < (price - coupon):
    print("You did not enter enough money. Please try again.")
    galleons = int(input("Galleons (equals 493 knuts): "))
    galValue = galleons * 493
    sickles = int(input("Sickles (equals 29 knuts): "))
    sicValue = sickles * 29
    knuts = int(input("Knuts (equals 1 knut): "))
    cost = galValue + sicValue + knuts


# Equations to calculate change
change = cost - price + coupon
galChange = change // 493
sicChange = (change % 493) // 29
knutsChange = (change % 493) % 29

# ouput to user for change
print("\nYou bought a " + item + " for", price, "knuts (with a coupon of " + str(coupon) + " knuts) and paid with")
print(galleons, "Galleons,", sickles, "sickles, and", knuts, "knuts.")
print("Here is your change (" + str(change) + " knuts): ")
print("Galleons:", galChange)
print("Sickles:", sicChange)
print("Knuts:", knutsChange)
