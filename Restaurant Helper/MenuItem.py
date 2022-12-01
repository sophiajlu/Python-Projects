# Sophia Lu, sjlu@usc.edu
# ITP 115, Spring 2021
# Final Project - Menu Item Class

# Part 1 - Creating the Restaurant's Menu
class MenuItem:
    # defining instance attributes
    def __init__(self, dishName, dishCategory, dishPrice, description):
        self.name = dishName
        self.category = dishCategory
        self.price = dishPrice
        self.desc = description

    # defining get methods for all instance attributes
    def getName(self):
        return self.name
    def getCategory(self):
        return self.category
    def getPrice(self):
        return self.price
    def getDesc(self):
        return self.desc

    # def __str__
    def __str__(self):
        # formatting statement (price)
        priceFloat = float(self.price)
        priceFormat = "{:.2f}".format(priceFloat)
        info = self.name + " (" + self.category + "): $" + priceFormat + "\n\t" + self.desc
        # add something about formatting price as $xx.00
        return info