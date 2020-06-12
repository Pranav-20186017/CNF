import socket

HOST = '127.0.0.1' 
PORT = 65432        

currency = {
          'Dollar': 1,
          'INR': 67,
          'Pounds': 0.75,
          'Yen': 113.41
}


while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            data = conn.recv(4096)
            data = data.decode('utf-8')
            split = data.split(' ')
            # print(split)
            fr = split[1]
            val = float(split[2])
            to = split[4]
            conv = val / currency[fr]
            conv = conv * currency[to]
            if not conv:
                break
            conn.sendall(str(conv).encode('utf-8'))