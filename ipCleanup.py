#python

'''
task: get only the ips into 'ips' file
'''
a=open("liveIps","r")
liveRaw=a.read()
a.close()

lines=liveRaw.split("\n")

for i in range(4):  #remove extra header and gateway
  lines.pop(0)

lines.pop(len(lines)-1)

lst=[]
for i in range(len(lines)):  #split into ips only
  temp = lines[i].split(" ")
  if("192." in temp[len(temp)-1]):
    lst.append(((temp[len(temp)-1]).replace("(","")).replace(")",""))

a=open("ips","w")
a.write("")
a.close()
a=open("ips","a+")
for i in range(len(lst)):
  a.write(lst[i]+"\n")
a.close()
