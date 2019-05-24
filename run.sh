bash ipScan.sh
python portCleanup.py > ipOpen

cat ipOpen
#hydra -l root -P /usr/share/wordlist/rockyou.txt [ip] ssh -t 4
