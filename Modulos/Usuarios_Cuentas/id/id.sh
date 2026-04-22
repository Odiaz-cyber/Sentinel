#!/bin/bash

cat report/system_users.txt | xargs id | awk '{print$1}' | awk -F"=" '{print$2}' | tr -d ')' | tr '(' ' ' > report/user_id.txt

