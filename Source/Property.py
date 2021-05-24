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
        self.topTile = "=========="

        #Import Pre-Generated Data
        self.name = jsonDict["name"]
        self.color = jsonDict["color"]
        self.type = jsonDict["type"]

        #Post load variables
        self.owner = None
        self.symbol = None
        self.isMonopoly = False
        self.rentLevel = 0
        self.currentPlayers = []
        
        #Set Data Flags For Specific Types Of Property
        if self.type == "ownable":
            self.homePrice = jsonDict["homePrice"]
            self.rentScale = jsonDict["rent"]
            self.price = jsonDict["price"]
        elif self.type == "railroad":
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
    def setOwner(self, owner, symbol):
        self.owner = owner
        self.symbol = symbol

    def setMonopoly(self, state):
        self.rentScale[str(0)] = self.rentScale[str(0)] * 2
        self.isMonopoly = state

    def buyHouse(self):
        self.rentLevel+=1

    def setCurrentPlayers(self, players):
        self.currentPlayers = players

    
    
