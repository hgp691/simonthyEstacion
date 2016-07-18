import correo
import json1
import log

log.escribirLog("Reinicio del sistema")

clientes=json1.obtenerCientesCorreo()
print len(clientes)
for cliente in clientes:
	print cliente["EMAIL"]
	correo.inicio(cliente["EMAIL"])
