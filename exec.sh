#!/bin/bash

#    ssh root@[IP] 'bash -s' < [SCRIPT_NAME]

#Loop:

#connect to the vulnerable device

#generate a passwd

 #pass=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)

#change password in loop

 #echo -e "$pass\n$pass" | passwd [USER]

#log the password localy

 #echo "$pass,[IP],[NAME]" >> log.[TIME]

#End loop:
