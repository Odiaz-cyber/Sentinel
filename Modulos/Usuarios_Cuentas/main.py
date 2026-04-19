#!/usr/bin/python3

import signal
import sys
import subprocess
import time
from termcolor import colored



def def_handler(sig,frame):
    print(colored("\n[!] Saliendo...." , "red"))
    sys.exit(1)

signal.signal(signal.SIGINT , def_handler)

def main(): # Flujo del programa
    user = subprocess.check_output("whoami",shell=True)
    
    if user.strip().decode() != "root":
        print(colored("\n[+] Para realizar el escaneo es necesario convertirse en root\n" , "red"))
        time.sleep(2)
        subprocess.run(["sudo","su"])
    
    # Extraer usuarios del sistema

    subprocess.run(["/bin/bash","extract_users.sh"])


if __name__ == "__main__":
    main()