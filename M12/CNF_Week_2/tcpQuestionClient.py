import socket

def main():
	host = '127.0.0.1'
	port = 5000
	s = socket.socket()
	s.connect((host,port))
	message = input("-> ")
	while message != 'q':
		s.send(str.encode(message))
		data = s.recv(1024)
		check = data.decode()
		if check == 'Attendacne Success':
			print("Response from server: " + data.decode())
			break
		print("Response from server: " + data.decode())
		message = input("-> ")
	s.close()
if __name__ == '__main__':
	main()