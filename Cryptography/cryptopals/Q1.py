from sys import argv
import base64

script , hexstr = argv

ans = base64.b64encode(hexstr.decode('hex'))

print "base64 String :"+ ans