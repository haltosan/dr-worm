echo "finding curent subnet/ip range"
lIp=$(ifconfig | sed -En 's/127.0.0.1//;s/.*inet (addr:)?(([0-9]*\.){3}[0-9]*).*/\2/p')
echo "local ip is: " $lIp
nmap -sn $lIp"/24" -oN liveIps
echo "*********************************************************************************"
cat liveIps
#nmap -iL liveIps -p22 -oN sshOpen
