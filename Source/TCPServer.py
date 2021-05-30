################################################################################
# TCPServer.py
# File to manage and preform all game functions
# Python : Period 2
################################################################################

import socket
import sys
from threading import Thread
import time

class TCPServer():

    #Functions
    def __init__(self):

        #Define Variables
        self.socket = None
        self.hostname = socket.gethostname()
        self.ip = socket.gethostbyname(self.hostname)
        self.port = 32600 

        self.clients = 0

        #Init TCP Server
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
            self.socket.bind((self.ip, self.port))
            print(f"[INFO]: Started TCP Server on {self.ip}:{self.port}")
        except socket.error as e:
            print(f"[ERROR]: Failed to start TCP Server, exiting... EXCEPTION: {str(e)}")
            sys.exit(-1)

    @staticmethod
    def clientNetworkLoop(c, addr):
        while True:
            #Get incoming data from clients
            data = c.recv(2048)
        
    def searchForClients(self):

        #Start Listening for clients
        while self.clients < 3:
            self.socket.listen(5)

            c, addr = self.socket.accept()
            start_new_thread(clientNetworkLoop, (c, addr))
            self.clients += 1

