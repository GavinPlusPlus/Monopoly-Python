################################################################################
# Dice.py
# Code ported over from the dice project
# Python : Period 2
################################################################################

from random import randint
import time
import sys

class Dice:

    def __init__(self):

        self.diceStrings = [" ------- ;", "|       |;", "| *     |;", "|   *   |;", "|     * |;", "| *   * |;"]
        self.dice = [""] * 6
        for i in range(0, 6):
            #Add Top
            self.dice[i] += self.diceStrings[0]
            if (i == 0):
                self.dice[i] += self.diceStrings[1]
                self.dice[i] += self.diceStrings[3]
                self.dice[i] += self.diceStrings[1]
            elif (i == 1):
                self.dice[i] += self.diceStrings[1]
                self.dice[i] += self.diceStrings[5]
                self.dice[i] += self.diceStrings[1]
            elif (i == 2):
                self.dice[i] += self.diceStrings[2]
                self.dice[i] += self.diceStrings[3]
                self.dice[i] += self.diceStrings[4]
            elif (i == 3):
                self.dice[i] += self.diceStrings[5]
                self.dice[i] += self.diceStrings[1]
                self.dice[i] += self.diceStrings[5]
            elif (i == 4):
                self.dice[i] += self.diceStrings[5]
                self.dice[i] += self.diceStrings[3]
                self.dice[i] += self.diceStrings[5]
            elif (i == 5):
                self.dice[i] += self.diceStrings[5]
                self.dice[i] += self.diceStrings[5]
                self.dice[i] += self.diceStrings[5]
            self.dice[i] += self.diceStrings[0]

    
    def roll(self):

        rand1 = 0
        rand2 = 0

        for i in range (20):

            #Roll dice
            rand1 = randint(1, 6)
            rand2 = randint(1, 6)

            #Assemble Printable Dice
            for i in range (0, 5):

                stringToPrint = ""
                stringToPrint += self.dice[rand1 - 1].split(";")[i] + "   "
                stringToPrint += self.dice[rand2 - 1].split(";")[i] + "   "
                print(stringToPrint)
                time.sleep(0.02)

            for j in range (0, 5):
                sys.stdout.write("\033[F")

        for i in range (0, 6):
            print()

        return rand1 + rand2
