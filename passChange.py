#python

import os

a=open("lib/creds","r")
lines = a.read().split("\n")
a.close()

for i in lines:
    print("ssh connect")
