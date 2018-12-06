import socket 

def Main():
    host = '127.0.0.1'
    port = 5001 # this should be different from Sever
    serverport = 5000

    server = (host, serverport)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    message = input(" -> ")
    while message != 'q':
        s.sendto (message.encode('utf-8'), server)
        data, address = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Receive from server: " + data)
        message = input (" -> ")
    s.close()

if __name__ == "__main__":
    Main()

