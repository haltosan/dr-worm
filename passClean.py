#python

a = open("log/found","r")
red = a.read()
a.close()

lines = red.split("\n")
info={}
for i in lines:
    if(not "hydra -C" in i):
        cells = i.split(" ")
        for j in range(len(cells)-1):
            if(cells[j].replace(" ","")=="host:"):
                host=cells[j+1]
            if(cells[j].replace(" ","")=="login:"):
                login=cells[j+1]
            if(cells[j].replace(" ","")=="password:"):
                password=cells[j+1]
        info[host]=[login,password]

for i in info:
    print i,info[i][0],info[i][1]
