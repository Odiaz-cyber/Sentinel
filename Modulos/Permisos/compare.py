#!/usr/bin/python3

# En este caso aqui vamos a ser las comparaciones entre un los archivos del sistema y la lista blanca


from termcolor import colored

class Compare:
    def __init__(self , files_list , white_list ):
        self.files_list = files_list 
        self.white_list = white_list
        self.result_list = [["Security" , "Files" , "Recomended"]]
      
        
    def comparador(self):
        
        for key , value in self.files_list.items():
            if key in self.white_list:
                if value == self.white_list[key]:
                    self.result_list.append(["Permits Recomended" , key])
                    
                else:
                    self.result_list.append(["Permits not recommended" , key , self.white_list[key]])
                   

        return self.result_list
    