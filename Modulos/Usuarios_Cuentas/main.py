#!/usr/bin/python3

import signal
import sys
import subprocess
import time
import argparse 
import re
from termcolor import colored
from shell_asignada.shell_asignada import ShellAsig
from id.id import U_ID

def get_argument():
    p = argparse.ArgumentParser(description="Help Panel to Pentesting Test")
    p.add_argument("-o" , "--output" , dest="output" ,  help="Optional parameter: Show Output in Termianl terminal )" )
    p.add_argument("-f" , "--filter" , dest="filter" ,  help="Optional parameter: Filter Output in terminal [python3 main.py -o terminal -f phrase]" )
    options = p.parse_args()
    
    return options.output,options.filter

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

    # Parameters

    o,f = get_argument()

    # Shell asignadas

    s = ShellAsig()
    human_user,system_user,etc_passwd,ishells,rshell = s.extract_info()

    if o == "terminal":
        print("\n----------------------------------------------- Shell Asignada ---------------------------------------------------\n")
        response = s.compare(human_user,system_user,etc_passwd,ishells,rshell)
        
        # Filros -> Agregar a otros modulos
        if f:
            for r in response:
                if re.findall(f,r,re.IGNORECASE): # Esta opcion permite que el match ocurra sin importar como esta escrito la palabra
                    print(r)

        else:
            for r in response:
                print(r)  

    # ID

    subprocess.run(["/bin/bash","id/id.sh"])
    
    u = U_ID()
    user_id = u.extract_info()
    u.compare(user_id)

    # Groups

    subprocess.run(["/bin/bash","grupos/extract_group.sh"])



if __name__ == "__main__":
    main()