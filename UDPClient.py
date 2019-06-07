import socket 

def Main():
    host = ""
    port = 5001

    server = ('127.0.0.1', 1234)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.bind((host, port))

    message = input("-> ")
    
    while message != 'q':
        s.sendto(bytes(message, 'utf-8'), server)
        data, addr = s.recvfrom(1024)
        print("Recieved from server: " + str(data))
        message = input("-> ")
    s.close()

if __name__ == "__main__":
    Main()