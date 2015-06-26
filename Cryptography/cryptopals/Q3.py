import sys
from mymodules import *
import operator
import numpy as np
from collections import Counter

plain_text = sys.argv[1].decode('hex')

arr = dict()

for key in xrange(0,256):
    temp = xorstr(msg,chr(key))
    arr[key] = similarity(charfreq.values(),Counter(temp).values())
        
ans = max(arr.iteritems())

print xorstr(plain_text,chr(ans))