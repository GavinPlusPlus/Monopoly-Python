################################################################################
# NetAPI.py
# File for scanning and connecting to games
# Python : Period 2
################################################################################

import socket
import sys
import time
import os
from threading import Thread


class Server:
    
    #Variables
    netSock = None
    ip = None
    hostname = None
    port = 32600
    udpConnected = False

    #Functions
    def __init__(self, port):

        self.port = port
        self.hostname = socket.gethostname()
        self.ip = socket.gethostbyname(self.hostname)

        #Socket and Thread Related Variables
        Thread.__init__(self)
        self.threadCount = 0
        self.activeConnections = []

    def startTCPServer(self):

        #Init Socket
        try:
            self.netSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.netSock.bind((self.ip, self.port))
            print(f"[INFO]: Success! Created TCP socket on {self.ip}:{self.port}")
        except socket.error:
            print(f"[ERROR]: Failed to TCP bind socket to {self.ip}:{self.port}")
            sys.exit(-1)

    def runTCPSearch(self):

        #Run Loop
        

    def startUDPServer(self):

        #Init temp socket
        tempSock = None
        try:
            tempSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
            tempSock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            tempSock.settimeout(.5)
            tempSock.bind(("", self.port))
            print(f"[INFO]: Success! Created UDP socket on {self.ip}:{self.port}")
        except socket.error:
             print(f"[ERROR]: Failed to create broadcast socket")
             sys.exit(-2)

        print(f"[INFO]: Broadcasting and waiting for client")
        
        #Broadcast loop
        broadcastPacket = f"NetAPI|HOST_SEARCH|{self.ip}:{self.port}|{self.hostname}"

        timeoutCounter = 120
        print()
        while not self.udpConnected and timeoutCounter >= 0:
            #Send Broadcast
            tempSock.sendto(bytes(broadcastPacket, "utf-8"), ("<broadcast>", self.port))

            #Look for response
            try:
                data, address = tempSock.recvfrom(1024)
                data = data.decode("utf-8")

                if data.startswith("NetAPI|HOST_REQ|"):
                    print(f"[INFO]: Found client on {address}")
                    self.udpConnected = True
                    return address

            except socket.timeout:
                sys.stdout.write("\033[F")
                print(f"[INFO]: Broadcast Time Remaining: {timeoutCounter / 2}")
                sys.stdout.flush()
                timeoutCounter -= 1

class Client:

    #Variables
    netSock = None
    localIP = None
    localHostname = None

    remoteIP = None
    remoteHostname = None

    port = 32600
    udpConnected = False

    #Functions
    def __init__(self, port):

        self.port = port
        self.localHostname = socket.gethostname()
        self.localIP = socket.gethostbyname(self.localHostname)


    def connectTCPSock(self, ip):

        #Init Socket Connection
        print(ip)

    def runClientLoop(self, data):



    def startUDPSearch(self):

        #Start UDP Search
        tempSock = None
        try:
            tempSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
            tempSock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            print(f"[INFO]: Success! Created UDP socket on {self.localIP}:{self.port}")
            tempSock.bind(("", self.port))
            tempSock.settimeout(.2)
        except socket.error:
            print(f"[ERROR]: Failed to create broadcast socket")
            sys.exit(-2)

        timeoutCounter = 120
        print()
        while not self.udpConnected and timeoutCounter >= 0:
            #Look for response
            try:
                data, address = tempSock.recvfrom(1024)
                data = data.decode("utf-8")

                if data.startswith("NetAPI|HOST_SEARCH|"):
                    print(f"[INFO]: Found server on {address}")
                    self.udpConnected = True

                    #Respond Server to Prep for TCP
                    responsePacket = f"NetAPI|HOST_REQ|{self.localHostname}"
                    tempSock.sendto(bytes(responsePacket, "utf-8"), (address[0], self.port))

                    return address

            except socket.timeout:
                sys.stdout.write("\033[F")
                print(f"[INFO]: Search Time Remaining: {timeoutCounter / 2}")
                sys.stdout.flush()
                timeoutCounter -= 1