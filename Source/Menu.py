################################################################################
# Menu.py
# Class that contains all information pertaining to starting and running
# the game
# Python : Period 2
################################################################################

import json
import sys
import time

class Menu:

    #Init
    def __init__(self):
        
        #Constant Variables 
        self.version = "1.0.0"
        self.creators = "Gavin, Ryan, Anthany, Edward"
        
        #Dynamic Variables
        self.gameType = None
        self.saveData = None
        self.numPlayers = None

    def printTitle(self):

        print("  _____    ______       ______      ____     ____      ______      ___  _____       ______      ____       ___      ___")
        print(" /      \\_/      \     /  __  \\     |  |\\    |  |     /  __  \     |  \\/  _  \     /  __  \\     |  |       \\  \\    /  /")
        print(" |  |\\       /|  |    |  /  \  |    |  | \\   |  |    |  /  \  |    |     | |  \   |  /  \  |    |  |        \  \  /  /")
        print(" |  | \\     / |  |    |  |  |  |    |  |\\ \\  |  |    |  |  |  |    |  |  |_|  /   |  |  |  |    |  |         \  \/  /")
        print(" |  |  \\   /  |  |    |  |  |  |    |  | \\ \\ |  |    |  |  |  |    |  |\_____/    |  |  |  |    |  |          \    /")
        print(" |  |   \\_/   |  |    |  \\__/  |    |  |  \ \|  |    |  \__/  |    |  |           |  \__/  |    |  |______     |  |")
        print("/____\\       /____\\    \\______/     |__|   \_|__|     \\______/     |__|            \\______/     |_________|    |__|")

        print("\n\n\n\n\n\n\n\n\n\n")

    def runMainScreen(self):

        #Print starting screen
        print("Welcome to Python Monopoly!")
        print(f"\nVersion: {self.version}")
        print(f"Created by: {self.creators}\n\n")

        #Get Game Type
        print("Please enter the number of the option you would like")
        print("1. Start Game")
        print("2. Load Game")
        
        valid = False
        while not valid:
            net = input("Option: ")
            try:
                net = int(net)
            except ValueError:
                print("Invalid input, please try again\n")
            
            if net == 1:
                print("New Game Selected\n")
                valid = True
                self.gameType = 1
            elif net == 2:
                print("Attemping to search for save file")
                valid = True
                self.gameType = 2
            else:
                print("You did not pick a valid option, please try again\n")

        #Get Num of players
        print("Please enter how many players are going to be playing")
        
        getPlayers = False
        if self.gameType == 1:
            getPlayers = True
        while getPlayers:
            self.numPlayers = input("Players:")
            try:
                self.numPlayers = int(self.numPlayers)
                if self.numPlayers <= 4 and self.numPlayers >= 2:
                    getPlayers = False
                else:
                    print("Please enter a number of players between 2-4")
            except ValueError:
                print("Invalid number of players, please try again")
        
    def getGameType(self):
        return self.gameType

    def getSaveFileData(self):
        return self.saveData

    def getNumPlayers(self):
        return self.numPlayers
