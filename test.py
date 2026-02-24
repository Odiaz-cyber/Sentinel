dicc = {"casa":{"propietario":"odiaz"}}
dicc2 = {"casa":{"propietario":"odiaza" , "permiso":"r-r-r"}}

lista = []

for key , value in dicc.items():
    if key in dicc2:
        if value == dicc2[key]:
            print("Si los diccionarios son iguales")
        else:
           for key , value in dicc2[key].items():
               lista.append(value)

print(" ".join(lista))
