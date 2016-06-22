#!/bin/bash

aa=$1
bb=$2
cc=$3
dd=$4
ee=$5
ff=$6

msj="Cuenta de correo para enviar: $aa \nClave del correo: $bb \nDireccion IP o nombre del servidor: $cc \nPuerto del servicio SMTP: $dd \nAutenticacion TLS: $ee"

echo $msj

if(whiptail --title "Configuracion actual" --yesno "$msj" --yes-button "Configurar" --no-button "Cancelar" 15 60)then
	echo "EDIT"
else
	echo "CANCEL"
	exit
fi


dirCo=$(whiptail --title "Enviar desde:" --ok-button "Aceptar" --cancel-button "Cancelar" --inputbox "El correo electronico desde donde se va a enviar los correos" 10 60 $aa 3>&1 1>&2 2>&3)

exitstatus=$?

#echo $exitstatus
if [ $exitstatus = 0 ]; then
        echo $dirCo
else
        echo "CANCEL"
	exit
fi

clave=$(whiptail --title "Clave:" --ok-button "Aceptar" --cancel-button "Cancelar" --inputbox "Clave de el correo desde el cual se va a enviar" 10 60 $bb 3>&1 1>&2 2>&3)

exitstatus=$?

#echo $exitstatus
if [ $exitstatus = 0 ]; then
        echo $clave
else
        echo "CANCEL"
        exit
fi

dirSrv=$(whiptail --title "Servidor:" --ok-button "Aceptar" --cancel-button "Cancelar" --inputbox "Direccion IP del servidor SMTP" 10 60 $cc 3>&1 1>&2 2>&3)

exitstatus=$?

#echo $exitstatus
if [ $exitstatus = 0 ]; then
        echo $dirSrv
else
        echo "CANCEL"
        exit
fi

portSrv=$(whiptail --title "Servidor:" --ok-button "Aceptar" --cancel-button "Cancelar" --inputbox "Puerto del servidor SMTP" 10 60 $dd 3>&1 1>&2 2>&3)

exitstatus=$?

#echo $exitstatus
if [ $exitstatus = 0 ]; then
        echo $portSrv
else
        echo "CANCEL"
        exit
fi

if(whiptail --title "Start_TLS:" --yes-button "Autenticar" --no-button "No Autenticar" --yesno "El servidor se tiene que autenticar" 10 60 $ee 3>&1 1>&2 2>&3) then
	echo "YES"
else
	echo "NO"
fi

if(whiptail --title "Activar envio de correos:" --yes-button "Activar" --no-button "No Activar" --yesno "Desea activar el envio de correos electronicos" 10 60 $ff 3>&1 1>&2 2>&3) then
        echo "YES"
else
        echo "NO"
fi

