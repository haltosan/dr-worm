#!/usr/bin/expect -f
set HOSTNAME [lindex $argv 0]
set P1 [lindex $argv 1]
set pass [lindex $argv 2]
spawn ssh $HOSTNAME
expect "no)? "
send "yes\r"
expect "assword:"
send "$P1\r"
expect "#"
expect "#"
send "echo -e '$pass\n$pass' | passwd root\r"
interact
