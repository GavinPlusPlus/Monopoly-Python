################################################################################
# Player.py
# Class that contains all information pertaining to one player of the game
# including their properties, money, symbol, and position
# Python : Period 2
################################################################################

import json
import zlib

class Player:

    #Functions
    def __init__(self): 

        #Define Variables
        self.name = ""
        self.symbol = ""
        self.money = 1500
        self.properties = []
        self.boardPosition = 0

    #Getters
    def getName(self):
        return self.name

    def getSymbol(self):
        return self.symbol

    def getMoney(self):
        return self.money

    def getProperties(self):
        return self.properties

    def getBoardPosition(self):
        return self.boardPosition

    #Setters
    def setName(self):
        #Prompts user for a name to enter
        name = ""
        valid = False

        while not valid:
            name = input("Please enter your name (Under 16 Characters): ")
            if len(name) < 16:
                valid = True
            else: 
                print("Entered name is invalid! Please try again!")
        
        self.name = name
    
    def setSymbol(self, symbol):
        self.symbol = symbol

    def changeMoney(self, amount):
        self.money = self.money + amount

    def addProperty(self, num):
        self.properties.append(num)

    def removeProperty(self, num):
        if num in self.properties:
            self.properties.remote(num)
    
    def advanceBoardPosition(self, offset):
        #Check if player passes go
        if self.boardPosition + offset > 39:
            self.boardPosition + offset
            self.boardPosition = self.boardPosition - 39 
            print("Congrats! You passed Go, $200 Dollars has been added to your balance")
        else:
            self.boardPosition + offset

    def exportJson(self):
        #Build JSON Object
        jsonObj = None
        jsonObj["player"]["name"] = self.name
        jsonObj["player"]["symbol"] = self.symbol
        jsonObj["player"]["money"] = self.money
        jsonObj["player"]["properties"] = self.properties
        jsonObj["player"]["pos"] = self.boardPosition

        #Dump to string and compress
        compressed = zlib.compress(json.dumps(jsonObj).encode())

        #Return Compressed Data
        return compressed

    def importJson(self, jsonObj):
        #Uncompress JSON Data
        rawData = json.loads(zlib.decompress(jsonObj).decode())
        
        #Load JSON into local variables
        self.name = rawData["player"]["name"]
        self.symbol = rawData["player"]["symbol"]
        self.money = rawData["player"]["money"]
        self.properties = rawData["player"]["properties"]
        self.boardPosition = rawData["player"]["pos"]
    