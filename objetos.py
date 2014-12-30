class Coche:

	def __init__(self,gasolina):
		self.gasolina = gasolina
		print "tenemos",gasolina, "litros" 

	def arrancar(self):
		if self.gasolina>0:
			print "arranca"
		else:
			print "No podemos arrancar"

	def conducir(self):
		if self.gasolina >0:
			self.gasolina -= 1
			print "Queda", self.gasolina, " litros"
		else:
			print "No nos movemos"


mi_coche = Coche(3)

print (mi_coche.gasolina)

mi_coche.arrancar()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.arrancar()


print "gthfg".upper()
print "junmkkijj".count("junmk")