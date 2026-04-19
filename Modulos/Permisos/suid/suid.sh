#!/bin/bash

find / -perm -4000 2>/dev/null > report/system_file_suid.txt

cat report/system_file_suid.txt | xargs ls -l | awk '{print$3}' > report/own_file_suid.txt