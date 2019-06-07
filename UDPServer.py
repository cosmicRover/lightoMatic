import socket


def Main():
    host = '192.168.1.6'
    port = 1234

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print("Server started")
    while True:
        data, addr = s.recvfrom(1024)
        print("message from: " + str(addr))
        print("message from connected user: " + str(data))

        data = str(data).upper()
        print("sending: " + str(data))
        s.sendto(bytes(data, 'utf-8'), addr)
    s.close()


if __name__ == "__main__":
    Main()
