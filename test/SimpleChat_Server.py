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

def server(sock, port):
    # we need to bind the socket to a specific port
    while True:
        try:
            sock.bind(('', port)) #bind the host(socket) with the port
            break # here break the loop if the socket is binded to the port
        except OSError as err:
            # sometimes the port is used by other program -- wait untill it free
            print(err)
            print("Waiting ,will retry in 10 sec")
            sleep (10) # wait for 10s then connect again 
    # tell the socket to listen for incoming connection
    sock.listen(1)
    print("listening for incoming connection")

    # wait until the connection arrived
    client_sock, address = sock.accept() # accept method returns a tuple
    print ("got on incomming connection free", address)
    return client_sock  # if it is bind successfully --- return the sock 
    
# ___________________________MAIN FUNCTION________________________________

listener_sock = get_sock()
sock = server(listener_sock, 1234)

while True:
    encoded_text = sock.recv(1024)
    text = encoded_text.decode()  # get the text and decode it 
    print(text)