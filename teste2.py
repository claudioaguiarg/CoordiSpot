from customtkinter import CTk, CTkFrame, CTkLabel, CTkEntry

class CustomWindow(CTk):
    def __init__(self):
        super().__init__()
        self.root = CTk()
        self.title("Tabela Personalizada")
        self.geometry("400x300")
        self.main()


    def main(self):
        # Cabeçalho da tabela
        header_frame = CTkFrame(self)
        header_frame.pack(fill='x')

        header_labels = ['Nome', 'Idade', 'Email']
        for i, label_text in enumerate(header_labels):
            label = CTkLabel(header_frame, text=label_text, font=("Arial", 12, "bold"))
            label.grid(row=0, column=i, padx=10, pady=5)

        # Dados da tabela
        data_frame = CTkFrame(self)
        data_frame.pack(fill='both', expand=True)

        data = [
            ['João', '30', 'joao@example.com'],
            ['Maria', '25', 'maria@example.com'],
            ['Pedro', '35', 'pedro@example.com']
        ]

        for i, row in enumerate(data):
            for j, cell in enumerate(row):
                entry = CTkEntry(data_frame)
                entry.insert('end', cell)
                entry.grid(row=i, column=j, padx=10, pady=5)

App = CustomWindow()
App()
