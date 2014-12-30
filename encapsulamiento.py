class Ejemplo:
	def publico(self):
		print "publico"

	def __privado(self):
		print "privado"



ej= Ejemplo()
ej.publico()
ej._Ejemplo__privado()