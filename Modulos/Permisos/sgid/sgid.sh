#!/bin/bash

find / -perm -2000 2>/dev/null > report/system_file_sgid.txt

cat report/system_file_sgid.txt | xargs ls -ld  | awk '{print$4}' > report/own_file_sgid.txt
