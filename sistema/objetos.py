class TyH:
        def __init__(self,fecha,hora,temperatura,humedad):
                self.fecha=fecha
                self.hora=hora
                self.temperatura=temperatura
                self.humedad=humedad


class sonda:
	def __init__(self,temperatura,humedad,nombre,FechaUltimoDato,HoraUltimoDato):
		self.temperatura=temperatura
		self.humedad=humedad
		self.nombre=nombre
		self.FechaUltimoDato=FechaUltimoDato
		self.HoraUltimoDato=HoraUltimoDato
