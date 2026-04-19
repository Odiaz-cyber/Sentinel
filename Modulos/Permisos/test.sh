#!/bin/bash

cat report/system_file_suid.txt | ls -l | awk '{print$3}' > own_file_suid.txt
