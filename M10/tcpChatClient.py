import socket
import threading

def receivedata(s):
    while True:
        data = s.recv(1024)
        data = data.decode()
        print(data)

def main():
    host = '127.0.0.1'
    port = 5000
    print("Enter your name to connect to the group chat")
    username = input("Name: ")


    s = socket.socket()
    s.connect((host, port))

    s.send((str(username) + " has just joined the chat").encode())

    threading.Thread(target = receivedata, args = (s, )).start()

    while True:
        message = input()
        s.send((username +": " + message).encode())
    s.close()

if __name__ == '__main__':
        main()  