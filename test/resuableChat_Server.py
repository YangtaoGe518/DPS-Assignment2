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

def accept_new_connection(sock):
    # wait here until on incoming connection arrives. when it does we accept it
    client_sock, address = sock.accept() # accept method returns a tuple
    print ("got on incomming connection from", address)
    return client_sock  # if it is bind successfully --- return the sock 
    
# ___________________________MAIN FUNCTION________________________________

listener_sock = get_sock()
server(listener_sock, 1234)
while True:
    print("listening for incoming connection ..")
    sock = accept_new_connection(listener_sock)
    while True:
        try:
            encoded_text = sock.recv(1024)
        except KeyboardInterrupt as err:
            print ("user termination")
            sock.close()
            break # exit the loop --- end the infinite loop here

        if len(encoded_text) == 0: # if nothing send to the server, we think the connection is closed
            print("connection closed by remote end")    
            break # exit the loop

        text = encoded_text.decode('utf-8')  # get the text and decode it 
        print(text) 