import socket

def main():
	host = '127.0.0.1'
	port = 8081
	server = ('127.0.0.1', 8080)
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host,port))
	message = input("-> ")
	while message != 'q':
		s.sendto(str.encode(message),server)
		data, addr = s.recvfrom(1024)
		print("Recieved from server: " + data.decode())
		message = input("-> ")
	s.close()
if __name__ == '__main__':
	main()