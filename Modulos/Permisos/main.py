#!/usr/bin/python3 

# En este modulo de manera inciar que van a revisar los modulos y permisos de archivos y 
# directorios que pueden presentar riesgos con  permisos inadecuados para el usuarios

# Una segunda opcion seria que ul usuario use como argumento un archivo con nombre de direcotorios o aarchivos para su
# revision
import subprocess
import json # Trabajando con json
import argparse
from compare import Compare
from report import Report
from send_to_email import SendEmail
def get_arguments():

    parse = argparse.ArgumentParser(description="Help Panel to Pentesting Test")
    parse.add_argument("-r" , "--report" , dest="report" , required=True  , help="2 Types - html,pdf" )
    parse.add_argument("-e" , "--email" , dest="email" ,  help="Optional parameter: Emil to send report (Ex test@test.com)" )
    options = parse.parse_args()

    return options.report , options.email

def permisos_sh():

    subprocess.run(["/bin/bash" ,"permisos.sh"])

def procces_file():
    

    with open("permisos.json" , "r") as f:
        files_list = json.load(f) # Cargamos Json ahora es un diccionario
        
    

    with open("white_list_perm.json" , "r") as f:
        white_list = json.load(f) # Cargamos Json ahora es un diccionario
    return files_list , white_list # Diccionarios
    


       

    

def main():

     # Report Document Type 

    document , semail = get_arguments()

    # Get File Perm

    permisos_sh()
    files_list ,  white_list = procces_file()
    
   

    # Compare
    
    comparacion = Compare(files_list , white_list)
    result_list = comparacion.comparador()
    print(result_list)
    

    # Report

    report = Report(document , result_list )
    report.report()

    # Email
    if semail:
        email = SendEmail()
        if document == "pdf":
            email.send_email("Report" , "Attachment to Report" , "h1mlesssssss@gmail.com" , [semail] , "pggg bxnd brzu aqcd " , attachment_path="report.pdf" )
        else:
            email.send_email("Report" , "Attachment to Report" , "h1mlesssssss@gmail.com" , [semail] , "pggg bxnd brzu aqcd " , attachment_path="report.html" )
    

if __name__ == "__main__":
    main()








