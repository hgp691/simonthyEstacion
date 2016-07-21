#!/usr/bin/python

import serial
import time
import sys
import log


def obtenerRemota(obj):
        puerto=obj["PUERTO"]
        velocidad=obj["VELOCIDAD"]
        try:
                ser = serial.Serial(puerto, velocidad, timeout=2)
                ser.close()
                ser.open()
                ser.write(obj["DIRECCION"])
                time.sleep(3)
                ser.flush()
                print "Imprimiendo dato"
                read_val=ser.read(size=64)
                print read_val
                ser.flush()
                print "* "+str(len(read_val))
                ser.close()
        except serial.SerialException:
                print "Exeption"
                aaa="Excepcion remota.obtenerRemota "+obj["NOMBRE"]+" -> "
                res0=aaa,sys.exc_info()[0]
                print res0
                res=aaa,sys.exc_info()[1]
                print res
                log.escribirLog(res0)
                log.escribirLog(res)
