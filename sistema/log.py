#!/usr/bin/python

import serial
import time
import sys
import os
import csv
from subprocess import Popen, PIPE


def comprobarExistenciaLog(direccion):
        ruta='/mnt/usb/simonthy/logs/'+str(direccion)+'.csv'
        try:
                archivo=open(ruta,'r')
                archivo.close()
        except:
                print "Exepcion ",sys.exc_info()[1]
                print "Crear archivo"
                archivo=open(ruta,'wb')
                archivo.close()
#comprobarExistenciaLog(0)

def escribirLog(texto):
        try:
                comprobarExistenciaLog("log")
                fecha=time.strftime("%Y-%m-%d",time.localtime())
                hora=time.strftime("%H:%M:%S",time.localtime())
                fila=[fecha,hora,texto]
                archivo=open(r'/mnt/usb/simonthy/logs/log.csv','ab')
                escribir=csv.writer(archivo)
                escribir.writerow(fila)
                archivo.close()
        except:
                print "Excepcion -> ",sys.exc_info()[1]

#escribirLog("Texto de Log")



