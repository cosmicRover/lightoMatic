import socket 

def Main():
    host = "127.0.0.1"
    port = 5001

    server = ('69.116.111.26', 5001)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.bind((host, port))

    message = input("-> ")
    
    while message != 'q':
        s.sendto(bytes(message, 'utf8'), server)
        data, addr = s.recvfrom(1024)
        print("Recieved from server: " + str(data))
        message = input("-> ")
    s.close()

if __name__ == "__main__":
    Main()