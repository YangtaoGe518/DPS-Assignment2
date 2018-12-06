import sys
import socket 
from time import sleep 

def get_sock():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # here use TCP
    except socket.error as err:
        print("socket creation failed with error %s" %(err))
        sys.exit()
    return sock

def client(sock, ip, port): 
    while True: # here is the infinte loop
        try:
            sock.connect((ip, port))
            print("connected to", ip, "on port", port)
            return sock
        except ConnectionRefusedError as err:
            # here server is not ready
            sock.close()
            sock = get_sock()
            print ("Waiting for server")
            sleep (1)

sock = get_sock()
sock = client(sock, "127.0.0.1", 1234) #communication with the local device

while True:
    text = input("->")
    encode_text = text.encode()
    sock.send(encode_text)