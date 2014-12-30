import codecs

def main():

	f = open("texto.txt","r+")
    
  

	for linea in f:
		print (linea)
		

	for i in range(5):
		f.write("texto agregado\n")

	print (f.name)
	print (f.mode)
	print (f.closed)

	f.close()

	print (f.closed)


if __name__ == "__main__": 

	main()