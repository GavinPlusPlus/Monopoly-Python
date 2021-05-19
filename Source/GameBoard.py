################################################################################
# GameBoard.py
# File to import, create, and build the monopoly board
# Python : Period 2
################################################################################

import time
import json
import sys
import os

class GameBoard:

    #Variables
    boardJSON = None

    #Functions
    def __init__(self):

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

    def printRawJson(self):
        print(self.boardJSON)

    def printCurrentBoard(self):

        stringToPrint = ""
        centerSpacing = "                                                                        "

        #Print Sides
        for i in range (0, 9):
            for j in range (0, 5):
                stringToPrint = ""
                #Left Side
                stringToPrint += str(self.boardJSON["board"]["left"][str(8 - i)]["color"])
                tileStr = self.boardJSON["board"]["left"][str(8 - i)]["tile"]
                stringToPrint += tileStr.split(";")[j] 
                stringToPrint += centerSpacing

                #Right Side
                stringToPrint += str(self.boardJSON["board"]["right"][str(i)]["color"])
                tileStr = self.boardJSON["board"]["right"][str(i)]["tile"]
                stringToPrint += tileStr.split(";")[j] 
                print(stringToPrint)

        #Print bottom
        for i in range (0, 5):
            stringToPrint = ""
            for j in range (0, 11):
                stringToPrint += str(self.boardJSON["board"]["bottom"][str(10 - j)]["color"])
                tileStr = self.boardJSON["board"]["bottom"][str(10 - j)]["tile"]
                stringToPrint += tileStr.split(";")[i]
            print(stringToPrint)

game = GameBoard()
game.printRawJson()
print()
game.printCurrentBoard()