################################################################################
# NetAPI.py
# File for scanning and connecting to battleship games
################################################################################

import socket
import sys
import time

class Server:
    
    #Variables
    netSock = None
    port = 32600
    ip = None
    connected = False

    #Functions
    def __init__(self, port):

        self.port = port
        self.ip = socket.gethostname()

    def startTCPServer(self):

        #Init Socket
        try:
            self.netSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.netSock.bind(self.ip, self.port)
            print(f"[INFO]: Success! Created socket on {self.ip}:{self.port}")
        except socket.error:
            print(f"[ERROR]: Failed to bind socket to {self.ip}:{self.port}")
            sys.exit(-1)
            

    def startUDPSearch(self):

        #Init temp socket
        tempSock = None
        try:
            tempSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
            tempSock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            tempSock.settimeout(1)
            print("[INFO]: Created broadcast socket")
        except socket.error:
             print(f"[ERROR]: Failed to create broadcast socket")
             sys.exit(-2)

        print(f"[INFO]: Broadcasting and waiting for client", end="")
        
        #Broadcast loop
        broadcastPacket = f"NetAPI|HOST_SEARCH|{self.ip}:{self.port}"
        while not self.connected:
            #Send Broadcast
            tempSock.sendto(bytes(broadcastPacket, "utf-8"), ("<broadcast>", self.port))
            print(".", end="")
            time.sleep(.5)

            #Look for response
            data, address = tempSock.recvfrom(1024)
            data = data.encode("utf-8")

            if data.startswith("NetAPI|HOST_REQ|"):
                print(f"[INFO]: Found client on {address}")
                self.connected = True



