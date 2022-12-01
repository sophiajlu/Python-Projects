# Sophia Lu, sjlu@usc.edu
# ITP 115, Spring 2021
# Final Project - Menu class

# import
from MenuItem import MenuItem

# Part 1 - Creating the Restaurant's Menu
class Menu:
    # class variable
    CATEGORIES = ["Drink", "Appetizer", "Entree", "Dessert"]

    # defining instance attributes
    def __init__(self, fileName):
        # dictionary with key = category and value = empty list
        self.items = {"Drink": [], "Appetizer": [], "Entree": [], "Dessert": []}

        # opening the CSV file for read
        fileObject = open(fileName, "r")
        # loop through file
        for line in fileObject:
            # strip each line and split into list
            line = line.strip()
            lineList = line.split(",")
            # create MenuItem object from line
            # lineList[2] must be turned into a float for the MenuItem object
            item = MenuItem(lineList[0], lineList[1], float(lineList[2]), lineList[3])
            # item becomes a MenuItem object
            # add item to list with key = category (lineList[1] is category)
            self.items[lineList[1]].append(item)
        # close the file
        fileObject.close()

    def getMenuItem(self, category, positionIndex):
        if category in Menu.CATEGORIES and positionIndex in range(0, len(self.items[category])):
            chosenCat = self.items[category]
            chosenItem = chosenCat[positionIndex]
            return chosenItem

    def printMenuItem(self, category):
        if category in Menu.CATEGORIES:
            categoryList = self.items[category]
            print("\n-----" + category.upper()  + "S-----")
            for item in categoryList:
                # item is a MenuItem object, so will call __str__ from MenuItem to print item
                print(str(categoryList.index(item)) + ")", item)
        # if category is not an option, nothing will be printed

    def getNumMenuItems(self, category):
        if category in Menu.CATEGORIES:
            numItems = len(self.items[category])
        # if category is not an option, set numItems to 0
        else:
            numItems = 0
        return numItems