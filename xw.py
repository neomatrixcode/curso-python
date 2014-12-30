import wx

class MyFrame(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,-1,title)
        bt=wx.Button(self,-1,"hola")
        self.Bind(wx.EVT_BUTTON, self.decir_hola, bt)

    def decir_hola(self,*arg):
		print ("hola mundo")


class MyApp (wx.App):
    def OnInit(self):
        frame = MyFrame(None,"Mi primer ventana con wx")
        frame.Show(True)
        return True

MyApp().MainLoop()
