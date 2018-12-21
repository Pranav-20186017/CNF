import socket
import threading
clients = list()
def srvthd(c):
    while True:
        data = c.recv(1024)
        data = data.decode()
        if not data:
            break;
        for client in clients:
            if client != c:
                client.send(str(data).encode())


def main():
    num_connect = int(input("Please provide number of users: "))
    host = '127.0.0.1'
    port = 5000
    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    for i in range(0, num_connect):
        c, addr = s.accept()
        print("Connection established with " + str(addr))
        clients.append(c)
        thread = threading.Thread(target = srvthd, args = (clients[i],))
        thread.start()
    s.close()

if __name__ == '__main__':
    main()