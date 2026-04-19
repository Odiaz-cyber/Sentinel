#!/usr/bin/python3 

# NOTA: Si el usuario es root para que pedir que ingrese un usuario

# En este modulo de manera inciar que van a revisar los modulos y permisos de archivos y 
# directorios que pueden presentar riesgos con  permisos inadecuados para el usuarios

# Una segunda opcion seria que ul usuario use como argumento un archivo con nombre de direcotorios o aarchivos para su
# revision
import subprocess
import json # Trabajando con json
import argparse
import signal
import sys
import time
from termcolor import colored
from compare import Compare
from report import Report
from send_to_email import SendEmail
from terminal_output import Output
from Json.white_list_config import WL # Dentro de la carptea json


def def_handler(sig,frame):
    print(colored("\n[!] Saliendo...." , "red"))
    sys.exit(1)

signal.signal(signal.SIGINT , def_handler)

def get_arguments():

    parse = argparse.ArgumentParser(description="Help Panel to Pentesting Test")
    parse.add_argument("-r" , "--report" , dest="report" ,  help="Optional parameter: 2 Types - html,pdf" )
    parse.add_argument("-e" , "--email" , dest="email" ,  help="Optional parameter: Email to send report (Ex test@test.com)" )
    parse.add_argument("-o" , "--output" , dest="output" ,  help="Optional parameter: Show Output in Termianl )" )
    options = parse.parse_args()

    return options.report , options.email , options.output

def permisos_sh():

    subprocess.run(["/bin/bash" ,"permisos.sh"])

def procces_file():
    

    with open("Json/permisos.json" , "r") as f:
        files_list = json.load(f) # Cargamos Json ahora es un diccionario
        
    

    with open("Json/white_list_perm.json" , "r") as f:
        white_list = json.load(f) # Cargamos Json ahora es un diccionario
    return files_list , white_list # Diccionarios
    


    
       

    

def main():

    # Realizar el scaneo como root (Lo puedo hacer opcional)
    
    name_user = subprocess.check_output("whoami" , shell=True) # Con esta funcion de subprocess podemos ejecutar un comando
    if name_user.decode().strip() != "root":                   # y guardar o mostrar el output
        print(colored("\n[+] Para realizar el escaneo es necesario convertirse en root\n" , "red"))
        time.sleep(2)
        subprocess.run(["sudo","su"])
    


     # Report Document Type 

    document , semail , output = get_arguments()

    # Add usuario a white list

    r = WL()
    wl = r.config()
    wl = r.setear(wl)
    r.parser(wl)

    # Get File Perm

    permisos_sh()
    files_list ,  white_list = procces_file()
    
   

    # Compare
    
    comparacion = Compare(files_list , white_list)
    result_list = comparacion.comparador()
    
  

    # Report

    # Ingresar seccion suid
    report = Report(document , result_list )
    report.report()


    # Terminal Otuput
    
    if output == 'terminal':
            terminal_output = Output(result_list)
            terminal_output.parse()
            print("\n------------------------------------------------ SUID ----------------------------------------------------\n")
            terminal_output.call_suid() # llamda a la funcion que llama  a la funcion que hace  el escaneo suid
            print("\n------------------------------------------------ SGID ----------------------------------------------------\n")
            terminal_output.call_sgid() # llamda a la funcion que llama a la funcion que hace escaneo sgid 
  
    
    
    # Email
    if semail:
        email = SendEmail()
        if document == "pdf":
            email.send_email("Report" , "Attachment to Report" , "h1mlesssssss@gmail.com" , [semail] , "pggg bxnd brzu aqcd " , attachment_path="report.pdf" )
        else:
            email.send_email("Report" , "Attachment to Report" , "h1mlesssssss@gmail.com" , [semail] , "pggg bxnd brzu aqcd " , attachment_path="report.html" )
  

if __name__ == "__main__":
    main()








