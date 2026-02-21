#!/bin/bash

# Crear con Bash archivos Json 

function permisos(){
    echo "{" # Abrir Json
    first=true
    while read -r file; do
        # -ld para que no muestre el contenido de los directorios 
        permiso=$((ls -ld "$file" | awk '{print $1}') 2> /dev/null &)  # permisos
        propietario=$((ls -ld "$file" | awk '{print $3}') 2> /dev/null &)  # propietario (columna 3)
        grupo=$((ls -ld "$file" | awk '{print $4}') 2>/dev/null &)  # grupo (columna 4)
        if [ "$first" = true ]; then 
            first=false
        else 
            echo "," 
        fi
        # Imprimir clave/valor en formato JSON
        echo -n " \"${file}\": { \"permiso\": \"${permiso}\", \"propietario\": \"${propietario}\", \"grupo\": \"${grupo}\" }"
        done < files.txt  # Hacer esto es lo mismo que usar cat file.txt | while ....
        echo

    echo "}" # Cerrar Json
}

permisos > permisos.json