#!/usr/bin/expect -f
set HOSTNAME [lindex $argv 0]
set P1 [lindex $argv 1]
spawn ssh $HOSTNAME
expect "no)? "
send "yes\r"
expect "assword:"
send "$P1\r"
expect "#"
send "pass=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)\r"
expect "#"
send "echo -e '$pass\n$pass' | passwd root\r"
interact
