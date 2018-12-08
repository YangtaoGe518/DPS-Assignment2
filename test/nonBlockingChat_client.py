import sys
import socket 
from time import sleep 
from nonblocking_readline import * # here need use UNIX  

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
sock.setblocking(False)

close_connect = False

while close_connect == False:
    try:
        key_text = nonblocking_readline()  # need define another function 
    except (EOFError, KeyboardInterrupt):
        close_connect = True

    if key_text != "":   # if sent empty data to the clinet --- close the connection
        encode_text = key_text.encode('utf-8')

        try: 
            bytessent = sock.send(encode_text)
            print ("sent ", bytessent, "bytes") 
        except BrokenPipeError as err:
            close_connect = True   

    try:
        received_bytes = sock.recv(1024)
        if len(received_bytes) == 0:   # receive nothing
            close_connect = True
        else:         
            net_text = received_bytes.encode('utf-8')
            print(">>", net_text)
    except BlockingIOError:
        pass

print("End of input, closing connection")
sock.close()
