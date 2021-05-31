################################################################################
# Game.py
# File to import, create, and build the monopoly board
# Python : Period 2
################################################################################

import time
import json
import sys
import os
from Property import Property

class Game:

    #Variables
    boardJSON = None
    propertyList = []

    #Functions
    def __init__(self):

        #Define Variables
        self.propertyList = []

        relPath = "\\json\\board.json"
        absPath = os.path.abspath("") + relPath
        try:
            with open(absPath, "r") as file:
                self.boardJSON = json.load(file)
            print("[Info]: Loaded board.json, applying settings...")
        except FileNotFoundError:
            print("[Error]: Failed to load board.json! Exiting...")
            print(absPath)
            sys.exit(-1)

        #Load all properties into propertyList
        for i in range (0, 11):
            self.propertyList.append(Property(self.boardJSON["board"]["bottom"][str(i)]))
        for i in range (0, 9):
            self.propertyList.append(Property(self.boardJSON["board"]["left"][str(i)]))
        for i in range (0, 11):
            self.propertyList.append(Property(self.boardJSON["board"]["top"][str(i)]))
        for i in range (0, 9):
            self.propertyList.append(Property(self.boardJSON["board"]["right"][str(i)]))

    def printCurrentBoard(self):

        stringToPrint = ""
        centerSpacing = "                                                                                          "

        #Print Top
        for i in range (0, 5):
            stringToPrint = ""
            for j in range (0, 11):
                stringToPrint += str(self.boardJSON["board"]["top"][str(j)]["color"])
                tileStr = self.boardJSON["board"]["top"][str(j)]["tile"]
                stringToPrint += tileStr.split(";")[i] + "\u001b[0m"
            print(stringToPrint)
            time.sleep(.02)

        #Print Sides
        for i in range (0, 9):
            for j in range (0, 5):
                stringToPrint = ""
                #Left Side
                stringToPrint += str(self.boardJSON["board"]["left"][str(8 - i)]["color"])
                tileStr = self.boardJSON["board"]["left"][str(8 - i)]["tile"]
                stringToPrint += tileStr.split(";")[j] + "\u001b[0m"
                stringToPrint += centerSpacing

                #Right Side
                stringToPrint += str(self.boardJSON["board"]["right"][str(i)]["color"])
                tileStr = self.boardJSON["board"]["right"][str(i)]["tile"]
                stringToPrint += tileStr.split(";")[j] + "\u001b[0m"
                print(stringToPrint)
                time.sleep(.02)

        #Print bottom
        for i in range (0, 5):
            stringToPrint = ""
            for j in range (0, 11):
                stringToPrint += str(self.boardJSON["board"]["bottom"][str(10 - j)]["color"])
                tileStr = self.boardJSON["board"]["bottom"][str(10 - j)]["tile"]
                stringToPrint += tileStr.split(";")[i] + "\u001b[0m"
            print(stringToPrint)
            time.sleep(.02)

game = Game()
print()


