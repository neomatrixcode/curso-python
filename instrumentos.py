class Instrumento :
	def __init__ (self,precio):
		self.precio = precio

	def tocar (self):
		print "estamos tocando algo de musica"

	def romper (self):
		print "son", self.precio, " euros"

class Bateria(Instrumento):
	pass

class Guitarra (Instrumento):
	def __init__ (self,precio,tipocuerda):
		Instrumento.__init__(self,precio)
		
		