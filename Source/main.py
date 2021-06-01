################################################################################
# main.py
# Main python script to run all battleship and network functions
# Python : Period 2
################################################################################

from Menu import Menu
from Player import Player
from Game import Game
from Dice import Dice
import random
import time
import os
import sys

#Objects
menu = Menu()
dice = Dice()
game = Game()

players = []
freeSymbols = ["@", "$", "%", "&", "#", "*"]
totalTurns = 0
winner = False

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
    time.sleep(3)

    #Set all players at Go
    props = game.getPropertyList()
    for i in range (0, len(players)):
        props[0].addPlayer(i, players[i].getSymbol())
    game.updatePropertyList(props)
    game.updatePlayers(players)

elif gType == 2:
    print("Not working yet, check back later...")
    sys.exit(0)


#Main game code
while not winner:
    #Go through a turn for every player
    bankruptPlayers = []
    for i in range (0, len(players)):
        #Clear Screen and Print Board
        os.system("cls||clear")
        print(f"It is {players[i].getName()}'s Turn!")
        game.printCurrentBoard(0)
        print(f"\n\n\nYou currently have ${players[i].getMoney()}!")

        action = 0
        #Check if player is jailed first
        if players[i].isJailed() == False:
            action = game.askAction(i)
        else:
            print("You are currently in jail!")
            jailState = players[i].getJailRemaining()
            if jailState > 0: 
                print(f"You can either wait {jailState} more turns or pay $75 dollars now")
                print("1. Give up turn")
                print("2. Pay $75")

                valid = False
                while not valid:
                    option = input("Option: ")
                    try:
                        option = int(option)
                    except ValueError:
                        print("Invalid input, please try again\n")

                    if option == 1:
                        print("You wait another day...")
                        valid = True
                    elif option == 2:
                        print("You are now free, just 75 dollars poorer")
                        players[i].changeMoney(-75)
                        players[i].setJailed(False)
                        valid = True
                    else:
                        print("Invalid Option, Please try again")
                
            time.sleep(3)

        #Dev Flags
        devFlag = False
        result = 0

        #Dev Code
        if action == 123:
            roll = input("DEV MODE: Enter roll (1-39): ")
            result = int(roll)
            action = 1
            devFlag = True

        #Other options
        if action == 2:
            print("You have chosen to build on one of your properties")
            print("Please pick a property to build on (type 0 to exit)")
            validProps = 0
            for j, props in enumerate(board):
                if props.getPlayer() == i:
                    print(f"{j + 1}. {props.getName()} for ${props.getHouseCost()}")
                    validProps += 1
                    
            board = game.getPropertyList()
            if validProps > 0:
                valid = False
                option = 0
                while not valid:
                    option = input("Option: ")
                    try:
                        option = int(option)
                    except ValueError:
                        print("Invalid input, please try again\n")
                    
                    if option > validProps:
                        print("Invalid Option")
                    elif option > 0 and option <= validProps:
                        getBoardNum = players[i].getProperty(option)
                        board[getBoardNum].buyHouse()
                        print(f"You have chosen to build on {board[getBoardNum].getName()} for ${board[getBoardNum].getHouseCost()}")
                        players[i].changeMoney(-board[getBoardNum].getHouseCost())
                        valid = True
                    elif option == 0:
                        valid = True
                
            else:
                print("You have no properties you can build on!")
            action = 1
            game.updatePropertyList(board)

        #Main Roll Code
        if action == 1:

            #Run Dice and Change Pos
            oldPos = players[i].getBoardPosition()
            if not devFlag:
                result = dice.roll()
                devFlag = False
            print(f"You Rolled a {result}!")
            time.sleep(2)
            players[i].advanceBoardPosition(result)

            #Update Board
            board = game.getPropertyList()
            board[oldPos].removePlayer(i)
            board[players[i].getBoardPosition()].addPlayer(i, players[i].getSymbol())
            game.updatePropertyList(props)
            game.updatePlayers(players)

            #Print New Board
            os.system("cls||clear")
            print(f"It is {players[i].getName()}'s Turn!")
            game.printCurrentBoard(1)

            #Print what you landed on
            newPos = players[i].getBoardPosition()
            print(f"You landed on {board[newPos].getName()}")

            #Check if you can buy and afford property/railroad/utility
            if (board[newPos].getType() == "ownable" or board[newPos].getType() == "railroad" or board[newPos].getType() == "utility") and board[newPos].getOwner() == None:
                print(f"This property is currently for sale, would you like to buy it for ${board[newPos].getPrice()}")
                print(f"You currently have ${players[i].getMoney()}")
                #Ask for action
                valid = False
                while not valid:
                    option = input("Purchase (Y/N): ")
                    option = option.upper()
                    #Run math
                    if option == "Y":
                        valid = True
                        players[i].changeMoney(-board[newPos].getPrice())
                        players[i].addProperty(newPos)
                        print(f"SOLD! You now have ${players[i].getMoney()}")
                    elif option == "N":
                        valid = True
                        print("PASS! You chose not to buy the property")
                    else:
                        print("Invalid Option! Please try again! (Y/N)")
                board[newPos].setOwner(players[i].getName(), players[i].getSymbol(), i)
                game.updatePropertyList(board)
                
            #Check if someone else owns a property
            elif (board[newPos].getType() == "ownable" and board[newPos].getOwner() != None):
                owner = board[newPos].getOwner()
                rent = board[newPos].getRent()
                print(f"You have landed on {board[newPos].getName()} which is owned by {owner}")
                print(f"You must pay ${rent}!")

                #Subtract and print new balances
                players[i].changeMoney(-rent)
                players[board[newPos].getPlayer()].changeMoney(rent)
                print(f"Your Balance: ${players[i].getMoney()} | {owner}'s Balance: $ {players[board[newPos].getPlayer()].getMoney()}")
                game.updatePropertyList(board)
                time.sleep(2)

            #Check if someone else owns railroad
            elif (board[newPos].getType() == "railroad" and board[newPos].getOwner() != None):
                owner = board[newPos].getOwner()
                rent = 25
                print(f"You have landed on {board[newPos].getName()} which is owned by {owner}")

                #Find rent
                total = 0
                for property in board:
                    if property.getType() == "railroad" and property.getOwner() == owner:
                        total += 1

                if total == 1:
                    rent = 25
                elif total == 2:
                    rent = 50
                elif total == 3:
                    rent = 100
                elif total == 4:
                    rent = 200

                print(f"You must pay ${rent}!")
                 #Subtract and print new balances
                players[i].changeMoney(-rent)
                players[board[newPos].getPlayer()].changeMoney(rent)
                print(f"Your Balance: ${players[i].getMoney()} | {owner}'s Balance: $ {players[board[newPos].getPlayer()].getMoney()}")
                game.updatePropertyList(board)
                time.sleep(2)

            #Check if someone else owns a utility
            elif (board[newPos].getType() == "utility" and board[newPos].getOwner() != None):
                owner = board[newPos].getOwner()
                print(f"You have landed on {board[newPos].getName()} which is owned by {owner}")
                
                #Find if both or single are owned
                total = 0
                for property in board:
                    if property.getType() == "utility" and property.getOwner() == owner:
                        total += 1
                
                print(f"Because this is a utility and {owner} owns {total} you must pay ", end="")
                if total == 1:
                    print("4 times what you roll")
                elif total == 2:
                    print("10 times what you roll")

                rent = dice.roll()

                if total == 1:
                    rent *= 4
                elif total == 2:
                    rent *= 10

                #Subtract and print new balances
                players[i].changeMoney(-rent)
                players[board[newPos].getPlayer()].changeMoney(rent)
                print(f"Your Balance: ${players[i].getMoney()} | {owner}'s Balance: $ {players[board[newPos].getPlayer()].getMoney()}")
                game.updatePropertyList(board)
                time.sleep(2)

            #Check if player has landed on chance or community chest
            elif (board[newPos].getType() == "rng"):
                #good/bad toggle
                money = 0
                goodBad = random.randint(0, 1)
                if goodBad == 0:
                    money = 5 * random.randint(0, 15)
                    print(f"It is your lucky day! You got ${money}!")
                elif goodBad == 1:
                    money = -5 * random.randint(0, 10)
                    print(f"You gtt a popped tire, Pay ${money}")
                
                players[i].changeMoney(money)
                game.updatePropertyList(board)
            
            #Check if player has landed on a special space
            elif (board[newPos].getType() == "special"):
                tile = board[newPos]
                if (tile.getName() == "Pass go, Collect $200"):
                    print()
                elif (tile.getName() == "Jail"):
                    print()
                elif (tile.getName() == "Free Parking"):
                    print()
                elif (tile.getName() == "Go To Jail"):
                    print("You must go directly to jail!")
                    players[i].setJailed(True)
                    board[30].removePlayer(i)
                    board[10].addPlayer(i, players[i].getSymbol())
                game.updatePropertyList(board)

            #Check if anyone has gone bankrupt
            for player in players:
                if player.getMoney() <= 0:
                    print("UH OH")
                    print(f"{player.getName()} has run out of money!")
                    print("So long! It was nice knowing you")
                    print("Properties liquidated")

                    for props in board:
                        if props.getOwner() == player:
                            props.setOwner(None, None, None)

                    bankruptPlayers.append(i)

            print("Going to next player in 3 seconds")
            time.sleep(3)

    #Remove Bankrupt players
    for bankrupt in bankruptPlayers:
        del players[bankrupt]
        
    bankruptPlayers.clear()
    totalTurns +=1

