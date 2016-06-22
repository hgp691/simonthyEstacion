#!/bin/bash


RADIOLIST=""
j=1
for i in "$@"
do
	RADIOLIST=$RADIOLIST"$j) $i"
	j=$((j+1))
done

ELIMINAR=$(whiptail --title "ELIMINAR CORREO" --inputbox $RADIOLIST 20 78  3>&1 1>&2 2>&3)

exitstatus=$?

if [ $exitstatus = 0 ]; then
	echo "A ELIMINAR: " $ELIMINAR
else
	echo "CANCELO"
fi
