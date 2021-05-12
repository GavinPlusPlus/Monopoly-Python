################################################################################
# main.py
# Main python script to run all battleship and network functions
# Python : Period 2
################################################################################

from NetAPI import Server



testType = input("Would you like to be the server or client? (S - Server, C - Client)")

if testType == "S":

    server = Server(32600)
    server.startTCPServer()
    server.startUDPServer()
elif testType == "C":

    client = Client(32600)
    client.startUDPSearch()