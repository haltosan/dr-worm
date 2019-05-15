#python

a=open("sshOpen","r")
sshRaw=a.read()
a.close()

lines=sshRaw.split("\n")
lines.pop(0)
for i in range(3):
  lines.pop(1)
opens=[]
while True:
  if(not "Nmap" in lines[0]):
    break

  if("open" in lines[1]):
    opens.append(lines[0].split(" ")[len(lines[0].split(" "))-1])

  for i in range(4):
    lines.pop(0)
  try:
    for i in range(3):
      lines.pop(1)
  except:
    break

for i in opens:
  print(i)
