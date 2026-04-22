#!/bin/bash

cat report/system_users.txt | xargs id | awk '{print$1,$3}' > report/groups.txt