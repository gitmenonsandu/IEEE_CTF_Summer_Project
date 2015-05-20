print "Enter two strings of equal length "
a=raw_input()
b=raw_input()
xor=[]
for i in range(0,len(a)):
	c=chr(ord(a[i])^ord(b[i]))
	xor.append(c)
print xor
print "".join(xor)
