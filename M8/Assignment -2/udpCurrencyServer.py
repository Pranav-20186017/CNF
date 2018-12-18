import socket

def main():
	host = '127.0.0.1'
	port = 8080
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host,port))
	print("Server Started")
	while True:
		Currency = dict({("INR","Dollar"):1/67,("Dollar","INR"):67,
		("Pounds","Dollar"):1/0.75,("Dollar","Pounds"):0.75,("Yen","Dollar"):1/113.41,("Dollar","Yen"):113.41})
		data , addr = s.recvfrom(1024)
		data = data.decode()
		print("message from: " + str(addr))
		print("from connected user: " + str(data))
		temp = str(data).split(" ")
		key = (temp[1],temp[4])
		currency = float(temp[2]) * Currency[key]
		print("Sending: " + str(data))
		s.sendto(str(currency).encode(),addr)
	s.close()
if __name__ == '__main__':
	main()