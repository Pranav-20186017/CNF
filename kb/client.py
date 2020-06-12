import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

inp = None
while True:
    inp = input("Enter input: ").encode('utf-8')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(inp)
        data = s.recv(4096)
    print('Received', repr(data.decode('utf-8')))