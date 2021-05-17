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

        try:
            relPath = "\\Source\\json\\board.json"
            absPath = os.path.abspath("") + relPath
            with open(absPath, "r") as file:
                self.boardJSON = json.load(file)
            print("[Info]: Loaded board.json, applying settings...")
        except FileNotFoundError:
            print("[Error]: Failed to load board.json! Exiting...")
            sys.exit(-1)

    def printRawJson(self):
        print(self.boardJSON)

    def printCurrentBoard(self):
        #Print top
        stringToPrint = ""
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