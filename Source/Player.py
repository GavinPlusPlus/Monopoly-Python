################################################################################
# Player.py
# Class that contains all information pertaining to one player of the game
# including their properties, money, symbol, and position
# Python : Period 2
################################################################################

import json
import zlib
import time

class Player:

    #Functions
    def __init__(self): 

        #Define Variables
        self.name = ""
        self.symbol = ""
        self.money = 1500
        self.properties = []
        self.boardPosition = 0
        self.jailed = False
        self.jailRemaining = 3

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

    def isJailed(self):
        return self.jailed

    def getJailRemaining(self):
        self.jailRemaining -= 1
        if self.jailRemaining == 0:
            self.jailed = False
            print("You waited your time, You are now out of jail!")
            self.jailRemaining = 3
            return 0
        else:
            return self.jailRemaining

    #Setters
    def setJailed(self, state):
        self.jailed = state
        self.boardPosition = 10
        self.jailRemaining = 3

    def setName(self):
        #Prompts user for a name to enter
        name = ""
        valid = False

        while not valid:
            name = input("Please enter your name (Under 16 Characters): ")
            if len(name) < 16:
                valid = True
                print("Your Name is: " + name + "\n")
            else: 
                print("Entered name is invalid! Please try again!")
        
        self.name = name
    
    def setSymbol(self, symbols):
        #Prompts user for a symbol
        symbol = ""
        valid = False

        while not valid:
            symbol = input(f"Please choose a symbol from the following options ({symbols}): ")
            if symbol in symbols:
                symbols.remove(symbol)
                valid = True
            else:
                print("Character invalid or already used! Please try again")
        
        self.symbol = symbol
        return symbols

    def changeMoney(self, amount):
        self.money = self.money + amount

    def addProperty(self, num):
        self.properties.append(num)

    def getProperty(self, num):
        return self.properties[num - 1]

    def removeProperty(self, num):
        if num in self.properties:
            self.properties.remote(num)
    
    def advanceBoardPosition(self, offset):
        #Check if player passes go
        if self.boardPosition + offset > 40:
            self.boardPosition += offset
            self.boardPosition = self.boardPosition - 40 
            print("Congrats! You passed Go, $200 Dollars has been added to your balance")
            time.sleep(2)
            self.money += 200
        else:
            self.boardPosition += offset

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
    