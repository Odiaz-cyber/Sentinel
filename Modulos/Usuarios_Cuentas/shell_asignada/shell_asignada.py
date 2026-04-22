#!/usr/bin/python3
from termcolor import colored

class ShellAsig:
    def __init__(self):
        pass

    def extract_info(self):
        with open("report/human_users.txt" , "r") as f:
            human_user = f.read()

        with open("report/system_users.txt" , "r") as f:
            system_user = f.read()

        with open("report/etc_passwd.txt" , "r") as f:
            etc_passwd = f.read()
        
        with open("config/interactive_shells.txt" , "r") as f:
            ishells = f.read()
        
        with open("config/restricted_shells.txt" , "r") as f:
            rshell = f.read()
        
        human_user = human_user.split(" ")
        system_user = system_user.split("\n")
        etc_passwd = etc_passwd.split("\n")
        ishells = ishells.split("\n")
        rshell = rshell.split("\n")

        dict_etc_passwd = {}
        for s in etc_passwd:
            temporal_list = s.split(" ")
            for i,v in enumerate(temporal_list):
                if i == 0:
                    clave = v
                else:
                    valor = v
                    dict_etc_passwd[clave] = valor
                    
        return human_user,system_user,dict_etc_passwd,ishells,rshell

    def compare(self,human_user,system_user,etc_passwd,ishells,rshell):
        response = []
        for u in system_user:
            try:
                s = etc_passwd[u]
        
                if u not in human_user and s in ishells:
                    comm = colored(f"[usermod -s {s} {u}]","white")
                    r = colored(f"\n[ALERTA] Usuario: {u} → Shell insegura: {s}\nPara cambiar de shell → {comm}\n","red")
                    response.append(r)
                elif u not in human_user and s in rshell:
                    r = colored(f"\n[OK] Usuario: {u} → Shell segura: {s}\n","green")
                    response.append(r)
            except:
                pass
        return response