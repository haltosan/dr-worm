#python

import os

a = open("ipOpen","r")
red = a.read()
a.close()

lines = red.split("\n")
for i in lines:
  os.system("bash exec.sh "+i)
