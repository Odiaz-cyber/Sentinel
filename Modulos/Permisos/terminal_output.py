#!/usr/bin/python3
from termcolor import colored
from suid.suid import SUID
from sgid.sgid import SGID

class Output:
    def __init__(self,result_list):
        self.result_list = result_list


    def parse(self):
        #firt_line = self.result_list[0]
        self.result_list.remove(self.result_list[0])
        print("\nSecurity ----------------------------  File  ----------------------------  Recomended  -------------------\n")
        for listas in self.result_list:
            cadena = "\t\t\t".join(listas)
            
            if "Permits Recomended" in cadena:
                print(colored(f"\n{cadena}" , "green"))
            else:    
                print(colored(f"\n{cadena}" , "red"))


    def call_suid(self):
        s = SUID()        
        s.process()
    
    def call_sgid(self):
        s = SGID()
        s.process
        # Probando otra forma de mostrar

        #security = []
        #file = []
        #recomended = []
        #    
        #self.result_list.remove(self.result_list[0])
        #for lista in self.result_list:
        #    for p,l in enumerate(lista):
        #        if  p == 0:
        #            recomended.append(l)
        #        elif p == 1:
        #            file.append(l)
        #        else:
        #            security.append(l)
        #parse_security = f"{'\n'.join(security)}"
        #parse_file = f"{'\n'.join(file)}"
        #parse_recomended = f"{'\n'.join(recomended)}"
#
        #print(f"{parse_file}-----{parse_recomended}------{parse_security}")
        ##print(parse_file)
        #print(parse_recomended)
        #print(parse_security)
