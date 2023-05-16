import tkinter as tk


class PopupWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Popup")
        self.geometry("200x100")
        self.attributes("-topmost", True)  # Fica sempre no topo
        self.overrideredirect(True)  # Remove a barra de título

        self.content_label = tk.Label(self, text="Conteúdo reduzido")
        self.content_label.pack(pady=20)

        self.restore_button = tk.Button(self, text="Voltar", command=self.restore_window)
        self.restore_button.pack()

    def restore_window(self):
        self.master.state('normal')  # Restaura a janela principal


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Janela Personalizada")
        self.geometry("400x300")

        self.content_label = tk.Label(self, text="Conteúdo principal")
        self.content_label.pack(pady=50)

        self.reduce_button = tk.Button(self, text="Reduzir", command=self.reduce_window)
        self.reduce_button.pack()

        self.popup = None

    def reduce_window(self):
        if self.popup is None:
            self.state('iconic')  # Minimiza a janela principal
            self.popup = PopupWindow(self)
            self.popup.geometry("+10+10")  # Define a posição do pop-up no canto superior esquerdo
            self.popup.protocol("WM_DELETE_WINDOW", self.close_popup)

    def close_popup(self):
        self.popup.destroy()
        self.popup = None
        self.state('normal')  # Restaura a janela principal


window = MainWindow()
window.mainloop()
