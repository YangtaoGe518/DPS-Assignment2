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
        except OSError as err:
            print("OSERROR: " ,err)


# ___________________________MAIN FUNCTION________________________________

sock = get_sock()
sock = client(sock, "127.0.0.1", 1234) #communication with the local device

while True:
    try:       
        text = input("->")
    except EOFError as err:
        print("End of input, closing connection")
        sock.close()
        break

    encode_text = text.encode('utf-8')
    sock.send(encode_text)

    try:
        bytessent = sock.send(encode_text)
        print("sent", bytessent, "bytes")
    except BrokenPipeError as err:
        print("Connection closed by remote end")
        break
        