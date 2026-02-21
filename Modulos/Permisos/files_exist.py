#!/usr/bin/python3 

import os 
from termcolor import colored

with open("files.txt" , "r") as f:
    files = f.read()


files_list = files.split("\n")

for ruta in files_list:
    if os.path.exists(ruta):
        print(colored(f"{ruta} -> exist" , "green"))
    else:
        print(colored(f"{ruta} -> no exist" , "red"))