import socket
import sys
import pickle
import select
from time import sleep

class Network():
    def __init__(self, password):
        self.__password = password
        self.__server = False
        try: # try to make UDP connection
            self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        except socket.error as err:
            print("socket creation failed with error %s" %(err))
            sys.exit()
        self.__recv_buf = bytes() # use bytes to convey the messages
        self.get_local_ip_addr()

    def get_local_ip_addr(self):
        # obtained from the original network code
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # use UDP to get the local IP
        # connect to nrg.cs.uc.ac.uk
        s.connect(("128.16.66.166", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip

    def server(self, port):
        self.__server = True
        
