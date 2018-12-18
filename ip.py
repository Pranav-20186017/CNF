import textwrap
ip = input("enter ip: ")
vals = ip.split(".")
pad = int(input())
print(vals)
one = ""
for i in range(pad):
	one = one + "1"
if pad != 32:
	dif = 32 - pad
	for i in range(dif):
		one = one + "0"
xo = textwrap.wrap(one,8)
# print(xo)
# print(vals)
AN = []
for i in range(4):
	AN.append(int(xo[i],2))
vals = list(map(int,vals))
NWID = []
for i in range(4):
	NWID.append(AN[i] & vals[i])
print(NWID)
FH = []
for i in range(4):
	FH.append(NWID[i])
FH[3] = FH[3] + 1
print(FH)
BCA = input().split(".")
BCA = list(map(int, BCA))
tp = []
for i in BCA:
	tp.append(~i)
BA = []
for i in range(4):
	BA.append(tp[i] | vals[i])
print(BA)