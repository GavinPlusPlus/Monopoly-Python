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
        self.netType = None
        self.name = None

    def runMainScreen(self):

        #Print starting screen
        print("Welcome to Python Monopoly!")
        print(f"\nVersion: {self.version}")
        print(f"Created by: {self.creators}\n\n")

        #Get Host or Client
        print("In order to play you must have one server and up to 3 other clients")
        print("Please enter the number of the option you would like")
        print("1. Host Game")
        print("2. Join Game")

        #Get Game Type
        valid = False
        while not valid:
            net = input("Option: ")
            try:
                net = int(net)
            except ValueError:
                print("Invalid input, please try again\n")
            
            if net == 1:
                print("Server Mode Selected\n")
                valid = True
                self.netType = 1
            elif net == 2:
                print("Client Mode Selected\n")
                valid = True
                self.netType = 2
            else:
                print("You did not pick a valid option, please try again\n")
        
    def getNetType(self):
        return self.netType

    

