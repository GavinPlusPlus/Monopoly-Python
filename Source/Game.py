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

    #Functions
    def __init__(self):

        #Define Variables
        self.propertyList = []
        self.players = []

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

    def updatePlayers(self, players):
        self.players = players

    def askAction(self, currentPlayer):
        print("What would you like to do?")
        print("1. Roll")
        print("2. Build")
        print("3. List Properties")

        valid = False
        while not valid:
            option = input("Option: ")
            try:
                option = int(option)
            except ValueError:
                print("Invalid input, please try again\n")

            if option != 1 or option != 2 or option != 3 or option != 123:
                return option
            else:
                print("Invalid Option, please try again")

    def getPropertyList(self):
        return self.propertyList

    def updatePropertyList(self, list):
        self.propertyList = list

    def printCurrentBoard(self, mode):

        stringToPrint = ""
        centerSpacing = "                                                                                          "

        #Print Top
        for i in range (0, 5):
            stringToPrint = ""
            for j in range (0, 11):
                stringToPrint += str(self.boardJSON["board"]["top"][str(j)]["color"])

                #Special Case for Top and Bottom
                if i == 4:
                    stringToPrint += self.propertyList[20 + j].getBottomRow() + "\u001b[0m"
                elif i == 0:
                    stringToPrint += self.propertyList[20 + j].getTopRow() + "\u001b[0m"
                else:
                    tileStr = self.boardJSON["board"]["top"][str(j)]["tile"]
                    stringToPrint += tileStr.split(";")[i] + "\u001b[0m"
                    
            print(stringToPrint)
            if mode == 0:
                time.sleep(.02)

        #Print Sides
        for i in range (0, 9):
            for j in range (0, 5):
                stringToPrint = ""
                #Left Side
                stringToPrint += str(self.boardJSON["board"]["left"][str(8 - i)]["color"])

                if j == 4:
                    stringToPrint += self.propertyList[19 - i].getBottomRow() + "\u001b[0m"
                elif j == 0:
                    stringToPrint += self.propertyList[19 - i].getTopRow() + "\u001b[0m"
                else:
                    tileStr = self.boardJSON["board"]["left"][str(8 - i)]["tile"]
                    stringToPrint += tileStr.split(";")[j] + "\u001b[0m"

                stringToPrint += centerSpacing

                #Right Side
                stringToPrint += str(self.boardJSON["board"]["right"][str(i)]["color"])

                if j == 4:
                    stringToPrint += self.propertyList[31 + i].getBottomRow() + "\u001b[0m"
                elif j == 0:
                    stringToPrint += self.propertyList[31 + i].getTopRow() + "\u001b[0m"
                else:
                    tileStr = self.boardJSON["board"]["right"][str(i)]["tile"]
                    stringToPrint += tileStr.split(";")[j] + "\u001b[0m"

                print(stringToPrint)
                if mode == 0:
                    time.sleep(.02)

        #Print bottom
        for i in range (0, 5):
            stringToPrint = ""
            for j in range (0, 11):
                stringToPrint += str(self.boardJSON["board"]["bottom"][str(10 - j)]["color"])

                #Special Case for Top and Bottom
                if i == 4:
                    stringToPrint += self.propertyList[10 - j].getBottomRow() + "\u001b[0m"
                elif i == 0:
                    stringToPrint += self.propertyList[10 - j].getTopRow() + "\u001b[0m"
                else:
                    tileStr = self.boardJSON["board"]["bottom"][str(10 - j)]["tile"]
                    stringToPrint += tileStr.split(";")[i] + "\u001b[0m"

            print(stringToPrint)
            if mode == 0:
                time.sleep(.02)

