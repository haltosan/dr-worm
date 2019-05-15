'''
task: get only the ipaddresses with 22 open in the text file
output to hostList
'''

a=open("sshOpen","r")
read=a.read()
a.close()

rmFilter="[STRING]"
rm1="[STRING]"
rm2="[STRING]"
successStr="[STRING]"

cleaned=read.replace(rmFilter,"")
cleaned1=cleaned.replace(rm1,"")
cleaned2=cleaned1.replace(rm2,"")
lines=cleaned2.split("\n")
out=[]
for i in lines:
  if(successStr in i):
    out.append(i)
print("out",out)
