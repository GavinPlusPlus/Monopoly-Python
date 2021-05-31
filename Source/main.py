################################################################################
# main.py
# Main python script to run all battleship and network functions
# Python : Period 2
################################################################################

from Menu import Menu
from Player import Player
from Game import Game
import random
import time
import os

#Objects
menu = Menu()
players = []
freeSymbols = ["@", "$", "%", "&", "#", "*"]
currentTurn = 0

#Main Code
menu.printTitle()
menu.runMainScreen()

#Get Game Type
gType = menu.getGameType()

if gType == 1:
    #Generate Players
    for i in range(0, menu.getNumPlayers()):
        print(f"\nPlayer {i + 1}:")
        tempPlayer = Player()
        tempPlayer.setName()
        freeSymbols = tempPlayer.setSymbol(freeSymbols)
        players.append(tempPlayer)

    os.system("cls||clear")
    menu.printTitle()

    print("Preparing Game...")
    time.sleep(1)
    print("Loading Board...")
    time.sleep(.38)
    print("Randomizing Player Order...")
    time.sleep(.68)
    random.shuffle(players)

    print("Player Order:")
    for i in range(0, len(players)):
        print(f"Player {i + 1}: {players[i].getName()} ({players[i].getSymbol()})")
    print()

    