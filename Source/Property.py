################################################################################
# Property.py
# Class that imports all data know about a particular property and stores it
# for later use
# Python : Period 2
################################################################################

import json
import sys
import os

class Property:

    #Functions
    def __init__(self, jsonDict):
        #Import Pre-Generated Data
        self.name = jsonDict["name"]
        self.color = jsonDict["color"]
        self.type = jsonDict["type"]
        
        #Set Data Flags For Specific Types Of Property
        if self.type == "ownable":
            self.homePrice = jsonDict["homePrice"]
            self.rentScale = jsonDict["rent"]
            self.price = jsonDict["price"]
        elif self.type == "railroad":
            self.price = jsonDict["price"]
        elif self.type == "tax":
            self.price = jsonDict["price"]
        
        #No special flags for rng, special, or utility
