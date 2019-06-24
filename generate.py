#python
import os
import random
import string
#'''
a=open("lib/creds","r")
lines = a.read().split("\n")
a.close()
#'''
def gen():
    l = string.ascii_letters
    return ''.join(random.choice(l) for i in range(10))

Lines=[]
for i in lines:
    i=i+" "+gen()
    Lines.append(i)

print(lines)

'''
a=open("lib/creds","w")
a.write(lines)
'''
