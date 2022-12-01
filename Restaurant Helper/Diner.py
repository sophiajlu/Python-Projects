# Sophia Lu, sjlu@usc.edu
# ITP 115, Spring 2021
# Final Project - Diner class

# Part 2 - Creating Diners

# import
from MenuItem import MenuItem

class Diner:
    # class variable
    STATUSES = ["seated", "ordering", "eating", "paying", "leaving"]

    # instance attributes
    def __init__(self, dinerName):
        self.name = dinerName
        self.order = [] # list of MenuItem objects ordered by diner
        self.status = 0
    # get methods
    def getName(self):
        return self.name
    def getOrder(self):
        return self.order
    def getStatus(self):
        return self.status

    def updateStatus(self):
        # add one to the diner's status
        self.status += 1

    def addToOrder(self, newItem): # newItem is a MenuItem object
        self.order.append(newItem)

    def printOrder(self):
        print(self.name, "ordered:")
        # for each item in the list of items they ordered, print it out
        for item in self.order: # item is MenuItem object
            print("-", item)

    def getMealCost(self):
        totalCost = 0
        for item in self.order: # item is a MenuItem
            itemCost = float(item.getPrice()) # call getPrice() function from MenuItem
            # add individual cost to the total cost
            totalCost = totalCost + itemCost
        return totalCost

    def __str__(self):
        info = "Diner " + self.name + " is currently " + Diner.STATUSES[self.status]
        return info
