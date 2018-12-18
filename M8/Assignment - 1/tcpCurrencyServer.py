import socket

def main():
	host = '127.0.0.1'
	port = 5000
	s = socket.socket()
	s.bind((host,port))
	s.listen(1)
	c , addr = s.accept()
	print("Connection from: " + str(addr))
	while True:
		Currency = dict({("INR","Dollar"):1/67,("Dollar","INR"):67,
		("Pounds","Dollar"):1/0.75,("Dollar","Pounds"):0.75,("Yen","Dollar"):1/113.41,("Dollar","Yen"):113.41})
		data = c.recv(1024)
		data = data.decode()
		if not data:
			break
		print("from Connected User: " + str(data))
		temp = str(data).split(" ")
		key = (temp[1],temp[4])
		currency = float(temp[2]) * Currency[key]
		print("Sending: " + str(currency))
		c.send(str(currency).encode())
	c.close()
if __name__ == '__main__':
	main()