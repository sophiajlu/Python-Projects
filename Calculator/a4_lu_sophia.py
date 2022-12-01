# Sophia Lu, sjlu@usc.edu
# ITP 115, Spring 2021
# Assignment 4
# Description:
# This program asks the user to enter integers then finds the average, smallest, and largest values

# creating variables
repeat = "y"

# outer loop
while repeat.lower() == "y":
    # user input
    print("Input an integer greater than or equal to 0 (-1 to quit)")
    num = int(input("> "))
    # more variables
    sum = num
    count = 1
    large = num
    small = num
    # inner loop
    while num != -1:
        num = int(input("> "))
        if num != -1:
            # branching
            if num > large:
                large = num
            elif num < small:
                small = num
           # reassigning variables
            sum = sum + num
            count = count + 1
    # calculating average
    average = sum / count
    #output to user
    print("The largest number is", large)
    print("The smallest number is", small)
    print("The average number is", average)
   # reassinging variable
    repeat = input("\nWould you like to enter another set of numbers (y/n)? ")
    print()

# ending message
print("Goodbye!")


