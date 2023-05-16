from customtkinter import *
from tkinter import CENTER, BOTTOM, LEFT, RIGHT, TOP
from pyautogui import position, click
from pynput import keyboard

class App:
    def __init__(self):
        self.root = CTk()
        self.root.geometry('300x350')
        self.root.title('Mouse Plot')
        self.root.attributes("-topmost", False)
        self.root.wm_resizable(False, False)
        # self.root.wm_overrideredirect(True)
        self.main()
        self.root.mainloop()


    def main(self):
        self.x = ''
        self.y = ''

        self.data = [
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', '']
        ]
        def mouse_plot():
            self.x, self.y = position()
            self.label_x.configure(text = self.x)
            self.label_y.configure(text = self.y)
            self.label_x.after(10, mouse_plot)

        def update_scroll_frame(index):
            try:
                self.scroll_frame._desired_width()
            except:
                pass
            if index == 0:
                for i, row in enumerate(self.data):
                    frame = CTkFrame(self.scroll_frame)
                    frame.grid(row=i + 1, column=0)
                    CTkLabel(frame,text=f'{i+1}').grid(row=0, column=0, padx = 10)

                    for j, cell in enumerate(row):
                        entry = CTkEntry(frame, width=65, height=30)
                        entry.insert('end', cell)
                        entry.configure(state='readonly')
                        entry.grid(row=0, column=j+1, padx=2, pady=2)
                # widgets = self.scroll_frame.winfo_children()
                # widgets[0].destroy()
            else:
                CTkLabel(self.scroll_frame, text=f'{index+1}').grid(row=0, column=0, padx=10)

                for j, cell in enumerate(self.data[index]):
                    entry = CTkEntry(self.scroll_frame_label, width=65, height=30)
                    entry.insert('end', cell)
                    entry.configure(state='readonly')
                    entry.grid(row=0, column=j+1, padx=2, pady=2)

                widgets = self.scroll_frame.winfo_children()
                widgets[index + 1].destroy()


        self.frame_master = CTkFrame(self.root, fg_color=self.root._fg_color)
        self.frame_master.pack(pady=20)

        self.frame_axis_titles = CTkFrame(self.frame_master)
        self.frame_axis_titles.pack()

        self.frame_axis = CTkFrame(self.frame_master)
        self.frame_axis.pack(pady = 10)

        self.label_name_x = CTkLabel(self.frame_axis_titles, text='Pos X')
        self.label_name_x.grid(row=1, column=1, padx=20)

        self.label_name_y = CTkLabel(self.frame_axis_titles, text='Pos y')
        self.label_name_y.grid(row=1, column=2, padx=20)

        self.label_x = CTkLabel(self.frame_axis, text='')
        self.label_x.grid(row=1, column = 1, padx = 20)

        self.label_y = CTkLabel(self.frame_axis, text='')
        self.label_y.grid(row=1, column = 2, padx = 20)

        self.scroll_frame = CTkScrollableFrame(self.root, width=170, height=20)
        self.scroll_frame.pack()
        update_scroll_frame()

        self.scroll_frame_label = CTkFrame(self.scroll_frame, width=100, height=100)
        self.scroll_frame_label.grid(row=0, column=0)
        header_labels = ['Num      ', 'Pos X       ', 'Pos Y    ']
        for i, label_text in enumerate(header_labels):
            label = CTkLabel(self.scroll_frame_label, text=label_text, font=("Arial", 12, "bold"))
            label.grid(row=0, column=i, pady = 10)






        self.switch_top = CTkSwitch(self.root, text='Always on Top', command=self.always_on_top)
        self.switch_top.pack(side = BOTTOM)



        def on_key_press(key):
            if key.char in '123456789':
                self.data[int(key.char) - 1] = [self.x, self.y]
                update_scroll_frame()



        # Cria um ouvinte de teclado
        listener = keyboard.Listener(
            on_press=on_key_press,
        )

        # Inicia o ouvinte
        listener.start()
        mouse_plot()

    def always_on_top(self):
        option = self.switch_top.get()
        if option == 1:
            self.root.attributes("-topmost", True)
        else:
            self.root.attributes("-topmost", False)


App()