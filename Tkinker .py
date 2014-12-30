from Tkinter import *

class App:
	def __init__(self,master):
		frame= Frame (master)
		frame.pack()
		self.hi_there = Button(frame, text="hola",command=self.decir_hola)
		self.hi_there.pack(side=LEFT)

	def decir_hola(self):
		print("hola mundo")



root= Tk()
app= App(root)
root.mainloop()