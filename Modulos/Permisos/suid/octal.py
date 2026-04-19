#!/usr/bin/python3

is_first = True
is_second = True
is_therd = True

vueltas = 0

permiso = "rwxrw-r-x"

lectura = 4
escritura = 2
ejecucion = 1


propietario = 0
grupos = 0
otros = 0 

for i in permiso:
# Propietario
    if is_first and vueltas < 3:
        if i == "r":
            propietario+=lectura
            vueltas +=1
        elif i == "w":
            propietario+=escritura
            vueltas +=1
        elif i == "x":
            propietario+=ejecucion
            vueltas +=1
        else:
            propietario+=0
            vueltas +=1
    else:
        is_first = False
        
        


# Grupos 
        if is_second and vueltas >= 3 and vueltas < 6:
            if i == "r":
                grupos+=lectura
                vueltas +=1
            elif i == "w":
                grupos+=escritura
                vueltas +=1
            elif i == "x":
                grupos+=ejecucion
                vueltas +=1
            else:
                grupos+=0
                vueltas+=1
        else:
            is_second = False
            
# Otros
            if is_therd and vueltas >= 6:
                if i == "r":
                    otros+=lectura
                    vueltas +=1
                elif i == "w":
                    otros+=escritura
                    vueltas +=1
                elif i == "x":
                    otros+=ejecucion
                    vueltas +=1
                else:
                   otros+=0
                   vueltas +=1
           

notacion_octal = f"{propietario}{grupos}{otros}"
print(notacion_octal)

