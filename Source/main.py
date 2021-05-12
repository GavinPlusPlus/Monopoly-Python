################################################################################
# main.py
# Main python script to run all battleship and network functions
# Python : Period 2
################################################################################

from NetAPI import Server

server = Server(32600)

server.startTCPServer()
server.startUDPServer()