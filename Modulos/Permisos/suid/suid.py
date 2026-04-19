#!/usr/bin/python3

import subprocess
import sys
import time
from termcolor import colored

class SUID:


    
    def __init__(self):

        subprocess.run(["/bin/bash","suid/suid.sh"])

        with open ("report/system_file_suid.txt" , "r") as f:
            self.strings_binarys = f.read() 
            self.lista_binarys = self.strings_binarys.split("\n")
            
        with open ("suid/black_list_files_suid.txt" , "r") as f:
            self.strings_binarys_white = f.read()
            self.lista_binarys_white = self.strings_binarys_white.split("\n")

        with open ("report/own_file_suid.txt" , "r") as f:
            self.own_string = f.read()
            self.list_own = self.own_string.split("\n")

    def  process(self):
        for s,o in zip(self.lista_binarys,self.list_own):
            
            if s not in  self.lista_binarys_white and o == "root":
                so = colored(f"[{s}]","white")
                sms = colored(f"tiene permiso SUID y su propietario es ROOT\n<i> Se recomienda revisar dicho binario , puede comprometer el sistema","red")
                sms2 = colored(f"[chmod -s {s}]","green")
                sms3 = colored("<i> Para eliminar el permiso puedes ejecutar el siguinte comando","red")
                rd = colored(f"\n<!> BINARY: {so} {sms}\n{sms3} -> {sms2}\n" , "red" )
                # Se puede hacer algo interante segun el binario reportar que problemas puede traer al sistema
                print(rd)
                time.sleep(1)
                #return rd

# Agregar a reporte html,pdf

