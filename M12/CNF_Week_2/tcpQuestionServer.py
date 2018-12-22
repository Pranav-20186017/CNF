import socket
def main():
	f = open('data.csv',"r")
	reg = []
	line = f.readline()
	while line:
		reg.append(line.strip("\n"))
		line = f.readline()
	f.close()
	roster = dict({})
	k = list()
	val = list()
	for i in reg:
		temp = i.split(",")
		k.append(int(temp[0]))
		v = (temp[1],temp[2])
		val.append(v)
	host = '127.0.0.1'
	port = 5000
	s = socket.socket()
	s.bind((host,port))
	s.listen(1)
	c , addr = s.accept()
	print("Connection from: " + str(addr))
	while True:
		data = c.recv(1024)
		data = data.decode()
		if not data:
			break
		at = data.split(" ")
		roll = int(at[1])
		if roll not in k:
			st = "Roll Number Not Found"
			c.send(st.encode())
		ind = k.index(roll)
		q = "SECRET QUESTION "+ val[ind][0]
		c.send(q.encode())
		ans = c.recv(1024)
		ans = ans.decode()
		ans = ans.split(" ")
		if ans[1] == str(val[ind][1]):
			resp = "Attendacne Success"
			c.send(resp.encode())
		else:
			resp = "Attendance Faliure"
			c.send(resp.encode())
	c.close()
if __name__ == "__main__":
	main()
