import wx

class CustomFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Janela Personalizada", size=(400, 300))
        
        self.panel = wx.Panel(self)
        
        self.main_label = wx.StaticText(self.panel, label="Conteúdo principal", pos=(100, 100))
        
        reduce_button = wx.Button(self.panel, label="Reduzir", pos=(100, 220), size=(100, 30))
        reduce_button.Bind(wx.EVT_BUTTON, self.reduce_window)
        
        restore_button = wx.Button(self.panel, label="Restaurar", pos=(220, 220), size=(100, 30))
        restore_button.Bind(wx.EVT_BUTTON, self.restore_window)
        
    def reduce_window(self, event):
        self.SetSize((200, 150))
        self.main_label.SetLabel("Conteúdo reduzido")

    def restore_window(self, event):
        self.SetSize((400, 300))
        self.main_label.SetLabel("Conteúdo principal")

app = wx.App()
frame = CustomFrame()
frame.Show()
app.MainLoop()
