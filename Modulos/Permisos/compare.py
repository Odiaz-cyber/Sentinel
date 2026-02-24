#!/usr/bin/python3

# En este caso aqui vamos a ser las comparaciones entre un los archivos del sistema y la lista blanca


from termcolor import colored

class Compare:
    def __init__(self , files_list , white_list ):
        self.files_list = files_list 
        self.white_list = white_list
        self.result_list = [["Security" , "Files" , "Recomended"]]
        self.list_perm =[]
        
    def comparador(self):
        
        for key , value in self.files_list.items():
            if key in self.white_list:
                if value == self.white_list[key]:
                    self.result_list.append(["Permits Recomended" , key])
                    
                else:
                    for key2 , value in self.white_list[key].items():
                        
                        self.list_perm.append(value)

                        if len(self.list_perm) == 3:
                            self.result_list.append(["Permits not recommended" , key ,"\t".join(self.list_perm)])
                            self.list_perm = []
                   

        return self.result_list
    