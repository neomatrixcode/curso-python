class Terrestre:
	def __init__(self, velocidadcaminar):
 		super(Acuatico, self).__init__()
 		self.velocidadcaminar = velocidadcaminar
	def caminar(self):
		print "estoy caminando"

	def desplazar(self):
		print "el animal anda"


class Acuatico(object):
 	
 	def __init__(self, velocidaddenado):
 		super(Acuatico, self).__init__()
 		self.velocidaddenado = velocidaddenado

 	def desplazar(self):
 		print "el animal nada"

 	def nadar(self):
 		print "estoy nadando"

 		 


class Cocodrilo (Acuatico,Terrestre):
	pass



Cocodrilo1 = Cocodrilo(1)
Cocodrilo1.desplazar()