################################################################################
# Property.py
# Class that imports all data know about a particular property and stores it
# for later use
# Python : Period 2
################################################################################

import json
import sys
import os

class Property:

    #Functions
    def __init__(self, jsonDict):
        #Pre assign variables
        self.homePrice = None
        self.rentScale = None
        self.price = None
        self.jsonDict = jsonDict

        #Import Pre-Generated Data
        self.name = jsonDict["name"]
        self.color = jsonDict["color"]
        self.type = jsonDict["type"]

        #Post load variables
        self.owner = None
        self.symbol = None
        self.player = None
        self.isMonopoly = False
        self.rentLevel = 0
        self.currentPlayers = ["=", "=", "=", "="]
        
        #Set Data Flags For Specific Types Of Property
        if self.type == "ownable":
            self.homePrice = jsonDict["homePrice"]
            self.rentScale = jsonDict["rent"]
            self.price = jsonDict["price"]
        elif self.type == "railroad" or self.type == "utility":
            self.price = jsonDict["price"]
        elif self.type == "tax":
            self.price = jsonDict["price"]
        
        #No special flags for rng, special, or utility

    #Getters
    def getOwner(self):
        return self.owner

    def getHouseCost(self):
        return self.homePrice

    def getRent(self):
        return self.rentScale[str(self.rentLevel)]

    def getPlayer(self):
        return self.player

    def getPrice(self):
        return self.price

    def getCurrentPlayers(self):
        return self.currentPlayers
    
    def getJson(self):
        return self.jsonDict
    
    def getName(self):
        return self.name
    
    def getType(self):
        return self.type

    def getIsMonopoly(self):
        return self.isMonopoly

    #Setters
    def setOwner(self, owner, symbol, num):
        self.owner = owner
        self.symbol = symbol
        self.player = num

    def setMonopoly(self, state):
        self.rentScale[str(0)] = self.rentScale[str(0)] * 2
        self.isMonopoly = state

    def buyHouse(self):
        self.rentLevel+=1

    def addPlayer(self, player, symbol):
        self.currentPlayers[player] = symbol

    def removePlayer(self, player):
        self.currentPlayers[player] = "="

    def getBottomRow(self):
        string = ""
        if self.type == "special":
            string += "+=="
        else:
            string += "==="

        
        for i in range (0, 4):
            if self.currentPlayers[i] is not "=":
                string += "\u001b[0m"
                string += self.currentPlayers[i]
            else:
                string += self.color
                string +=self.currentPlayers[i]
        
        if self.type == "special":
            string += "==+"
        else:
            string += "==="
        
        return string

    def getTopRow(self):
        string = ""
        if self.type == "special":
            return "+========+"
        elif (self.type == "railroad" or self.type == "ownable" or self.type == "utility") and self.owner is not None:
            string += "="
            string += self.symbol
            string += "======"
            string += str(self.rentLevel)
            string += self.color
            string += "="
            return string
        else:
            return "=========="
            

    
    
