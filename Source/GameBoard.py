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

    def printJson(self):
        print(self.boardJSON)

game = GameBoard()
game.printJson()