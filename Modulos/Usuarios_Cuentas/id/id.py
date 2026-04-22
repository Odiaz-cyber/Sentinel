#!/usr/bin/python3

class U_ID:
    def __init__(self):
        pass

    def extract_info(self):
        with open("report/user_id.txt" , "r") as f:
            user_id = f.read()

            lista_users = user_id.split("\n")
            

            dict_user_id = {}
            for u in lista_users:
                temporal_list = u.split(" ")
                for i,v in enumerate(temporal_list):
                    if i == 0:
                        clave = v
                    else:
                        valor = v
                        dict_user_id[clave] = valor
            return(dict_user_id)

    def compare(self,user_id):
        user = user_id['0']
        if  user != "root":
            print("\n-------------------------------------------------------- ID ------------------------------------------------------------\n")
            print(f"ALERTA → {user_id["0"]} con ID 0")
        else:
            pass


