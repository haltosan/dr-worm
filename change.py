#python
import os

a=open("lib/creds","r")
lines = a.read().split("\n")
a.close()

for i in lines:
    if(i!=''):
        l = i.split(" ")
        os.system("./login "+l[0]+" "+l[3])
