################################################################################
# main.py
# Main python script to run all battleship and network functions
# Python : Period 2
################################################################################

from NetAPI import Server, Client
from Menu import Menu
from Player import Player

#Variables
socket = None

#Objects
menu = Menu()
localPlayer = Player()


#Main Code
menu.runMainScreen()
localPlayer.setName()


