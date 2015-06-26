plain_text = raw_input("Enter the plain text : ")
key = raw_input("Enter the key : ")

n = len(plain_text)
l = len(key)

cipher = []

for i in range(0,n):
	cipher.append(hex(int(key[i%l],base=16)^int(plain_text[i],base=16)))
	
ans=[]

for i in cipher:
	ans.append(i[2])

print "Cipher Text : " + "".join(ans)