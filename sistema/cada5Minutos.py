#!/usr/bin/python
import json1
import correo
import log
import objetos


def textoSonda(sonda,setT,setH):
	texto="<tr>"
	texto+="<td>"+sonda.nombre+"</td>"
	if sonda.temperatura > setT :
		texto+="<td><strong style='color:red'>"+str(sonda.temperatura)+" C</strong></td>"
	else:
		texto+="<td><strong style='color:green'>"+str(sonda.temperatura)+" C</strong></td>"
	if sonda.humedad > setH:
		texto+="<td><strong style='color:red'>"+str(sonda.humedad)+" RH</strong></td>"
	else:
		texto+="<td><strong style='color:green'>"+str(sonda.humedad)+" RH</strong></td>"
	texto+="<td>"+sonda.FechaUltimoDato+" "+sonda.HoraUltimoDato+"</td>"
	texto+="</tr>"
	return texto
def enviarAlarma(arreglo,setT,setH):
	print "ENVIAR ALARMA"	
	asunto="ALARMA por cambio de estado !!!"
	texto='<html><h1>ALARMA!!</h1>'
	texto+="<table>"
	texto+="<tr>"
	texto+="<th>NOMBRE SONDA:</th>"
	texto+="<th>TEMPERATURA (SET:"+str(setT)+" C)</th>"
	texto+="<th>HUMEDAD (SET:"+str(setH)+" RH)</th>"
	texto+="<th>FECHA ULTIMO DATO:</th>"
	texto+="</tr>"
	for sonda in arreglo:
		texto+=textoSonda(sonda,setT,setH)
	texto+="</table>"
	texto+="</html>"
	clientes=json1.obtenerCientesCorreo()
        for cliente in clientes:
                correo.correo(asunto,texto,cliente["EMAIL"])

def revisarValores():
	log.escribirLog("revisarValores")
	arreglo=[]
	setT=json1.obtenerSetTemp()
	setH=json1.obtenerSetHum()
	#local
	Tlocal=json1.revisarUltimos5Temp("local.csv")
	Hlocal=json1.revisarUltimos5Hum("local.csv")
	if Tlocal > setT or Hlocal > setH :
		a=json1.ultimo("local.csv")
		obj=objetos.sonda(Tlocal,Hlocal,"ESTACION",a.fecha,a.hora)
		arreglo.append(obj)
	else:
		print "Es menor"
	#remotas
	a=json1.obtenerRemotas()
	for remota in a:
		if remota["ACTIVA"] == "YES":
			archivo=str(remota["DIRECCION"])+".csv"
			t=json1.revisarUltimos5Temp(archivo)
			h=json1.revisarUltimos5Hum(archivo)
			if t > setT or h > setH :
				b=json1.ultimo(archivo)
				obj=objetos.sonda(t,h,remota["NOMBRE"],b.fecha,b.hora)
				arreglo.append(obj)
			else:
				print "Remota es menor"
		else:
			print remota["NOMBRE"]+" desactivada"	
	if len(arreglo) > 0:
		enviarAlarma(arreglo,setT,setH)
revisarValores()
