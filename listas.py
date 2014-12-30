
def main():
	a = [1,4,7]

	l = [3.5,-1,"hola",[1.0,[3,17]],1]

	m = [[[1,[2,[]]],1,1,8],[2,2,2,6],[4,4,4,9]]

	print ("lista a es : "+str(a)+" con "+str(len(a))+ " elementos \nultimo elemento de la lista es: "+str(a[-1])+"\n") 

	print ("lista l es : "+str(l)+" con "+str(len(l))+ " elementos \nultimo elemento de la lista es: "+str(l[-1])+"\n") 

	
	for i in range(len(m)):
		for j in range(len(m[0])):
			print (m[i][j], end ="")

		print ("\n")




	a.append (17)

	print ("lista a es : "+str(a)+" con "+str(len(a))+ " elementos \nultimo elemento de la lista es: "+str(a[-1])+"\n") 

	l[0:2]=["elemeto agregado"]

	print ("lista l es : "+str(l)+" con "+str(len(l))+ " elementos \nultimo elemento de la lista es: "+str(l[-1])+"\n") 

	prueba = l[::-2]
	print ("lista prueba es : "+str(prueba)+" con "+str(len(prueba))+ " elementos \nultimo elemento de la lista es: "+str(prueba[-1])+"\n") 


	nuevalista= l+a
	print ("lista nuevalista es : "+str(nuevalista)+" con "+str(len(nuevalista))+ " elementos \nultimo elemento de la lista es: "+str(nuevalista[-1])+"\n") 
	
	nuevamul = a*4
	print ("lista nuevamul es : "+str(nuevamul)+" con "+str(len(nuevamul))+ " elementos \nultimo elemento de la lista es: "+str(nuevamul[-1])+"\n")



	for i in range (len(l)-1,-1,-1):
		print (l[i], end =" ")



	rb = 1 in a	
	print (rb)

	rc = "z" in "palabra"
	print (rc)


	frase = "\nesta es           una prueba"

	print (str(list(frase)))

	rr= frase.split()
	print (str(rr)+" contine "+str(len(frase.split()))+ " palabras" )

	print ("".join(["u","b","v","a"]))


	ordenado = sorted(l,key=str,reverse=True)
	print (ordenado) 

	l.sort(key=str)
	print (l)

if __name__ == "__main__":

	main()