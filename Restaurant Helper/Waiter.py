# Sophia Lu, sjlu@usc.edu
# ITP 115, Spring 2021
# Final Project - Waiter class

# Part 3 - Creating a Waiter
# importing
from Menu import Menu
from Diner import Diner

class Waiter:
    def __init__(self, menuObject):
        self.menu = menuObject
        self.diners = [] # a list of Diner objects

    def addDiner(self, newDiner): # newDiner is a Diner object
        self.diners.append(newDiner)

    def getNumDiners(self):
        numDiners = len(self.diners)
        return numDiners

    def printDinerStatus(self):
        print()
        # loop through all the statuses in class variable of Diner class
        for index in range(0, len(Diner.STATUSES)):
            status = Diner.STATUSES[index]
            print("Diners who are", status + ":")
            for customer in self.diners:
                # customer is a Diner object
                # if the customer has the same status, print it
                if customer.getStatus() == index:
                    print("\tDiner", customer.getName(), "is currently", status + ".")

    def takeOrders(self):
        for customer in self.diners:
            # customer is a Diner object
            if customer.getStatus() == 1: # index one corresponds to ordering
                # loop through each category
                for category in Menu.CATEGORIES:
                    # print out the menu for that category
                    # create Menu object first
                    menuForDiner = Menu("menu.csv")
                    # print menu
                    menuForDiner.printMenuItem(category)
                    print(customer.getName() + ", please select a " + category + " menu item number.")

                    # getting user input
                    itemIndex = input("> ")
                    # error checking
                    while itemIndex.isdigit() is False or int(itemIndex) not in range(menuForDiner.getNumMenuItems(category)): # will return an int
                        itemIndex = input("> ")
                    itemIndex = int(itemIndex)

                    # add the Menu item to order
                    # first get the menu item using getMenuItem() method from Menu
                    itemOrdered = menuForDiner.getMenuItem(category, itemIndex)
                    customer.addToOrder(itemOrdered)

                # print what the diner ordered calling printOrder() method from Diner
                print()
                customer.printOrder()

    def printMealCost(self):
        for customer in self.diners:
            # make sure customer is in paying status
            if customer.getStatus() == 3: # index 3 corresponds to paying
                cost = customer.getMealCost()
                costFormat = "{:.2f}".format(cost)
                print("\n" + customer.getName() + ", your meal cost $" + costFormat)

    def removeDiners(self):
        # loop through the diners backwards
        for customerIndex in range(len(self.diners)-1, -1, -1):
            # find which diner it is and get the status
            customer = self.diners[customerIndex]
            # customer is a Diner object
            if customer.getStatus() == 4: # index 4 corresponds to leaving
                print("\n" + customer.getName() + ", thank you for dining with us! Come again soon!")
                # remove the Diner object from list of diners
                self.diners.remove(customer)

    def advanceDiners(self):
        # call printDinerStatus method
        Waiter.printDinerStatus(self)
        # call other methods
        Waiter.takeOrders(self)
        Waiter.printMealCost(self)
        Waiter.removeDiners(self)

        # update each Diner status
        for customer in self.diners:
            # call updateStatus() method for Diner objects
            customer.updateStatus()