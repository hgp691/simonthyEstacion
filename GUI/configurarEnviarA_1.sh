#!/bin/bash

#desplegar el menu

OPTION=$(whiptail --title "LISTA DE CORREO PARA ENVIOS" --menu "Escoja una opcion" 15 60 4 \
"a" "Ver lista" 
"b" "Eliminar de la lista" \
"c" "Agregar a la lista" \
3>&1 1>&2 2>&3)

exitstatus=$?
if [ $exitstatus = 0 ]; then
    echo $OPTION
else
    echo "CANCEL"
fi
