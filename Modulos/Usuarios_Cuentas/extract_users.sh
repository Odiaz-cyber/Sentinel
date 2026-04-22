#!/bin/bash

# Si quieres extraer de manera automatica las cuentas humanas descomenta esto pero me gurda con saltos de linea
# Hay que quitarlos
# ls /home > report/human_users.txt 

getent passwd | cut -d: -f1 > report/system_users.txt

awk -F: '{print $1,$7}' /etc/passwd > report/etc_passwd.txt
