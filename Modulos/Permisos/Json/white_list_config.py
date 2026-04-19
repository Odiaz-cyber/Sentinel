#!/usr/bin/python3 

import json
from termcolor import colored
import signal



class WL:

    def __init__(self):
        
        self.usuario = input(colored("\n[+] Ingrese el nombre del usuario NO-ROOT con el que va a realiazar el escaneo: " , "green"))

    def config(self):
        with open("Json/white_list_perm.json", "r") as f:
            white_list = json.load(f)
            return white_list

    def setear(self,wl):
        #wl2 = {}
        for k,v in wl.items():
            if v["propietario"]  != "root":
                v["propietario"] = self.usuario

                wl[k] = v 
        return wl

    def parser(self,wl):
        
        with open("Json/white_list_perm.json", "w") as f:
            json.dump(wl,f,indent=4,sort_keys=True)   



  