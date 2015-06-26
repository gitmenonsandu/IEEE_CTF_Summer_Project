from sys import argv
from mymodules import *
script,str1,str2 = argv
str1 = str1.decode('hex')
str2 = str2.decode('hex')
ans = xorstr(str1,str2)
print ans.encode('hex')