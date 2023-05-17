from customtkinter import *
from tkinter import BOTTOM
from pyautogui import position
from pynput import keyboard
from pynput.keyboard import KeyCode
from PIL import Image


class App:
    def __init__(self):
        self.root = CTk(fg_color=('#171810'))
        self.root._set_appearance_mode("dark")
        self.root.geometry('300x350')
        self.root.title('CoordiSpot')
        self.root.iconbitmap('ico.ico')
        self.root.attributes("-topmost", False)
        self.root.wm_resizable(False, False)
        # self.root.wm_overrideredirect(True)
        self.main()
        self.root.mainloop()

    def main(self):
        self.x = ''
        self.y = ''

        def mouse_plot():
            self.x, self.y = position()
            self.label_x.configure(text=f'X : {self.x}')
            self.label_y.configure(text=f'Y : {self.y}')
            self.label_x.after(10, mouse_plot)

        import pyperclip
        import pyautogui

        def on_key_press(key):
            option = self.option_menu.get()
            if(option == 'Copy mode'):
                try:
                    if key.char in '123456789':
                        entry_num = int(key.char)

                        entryx_attr = f'entryx{entry_num}'
                        entryy_attr = f'entryy{entry_num}'

                        entryx = getattr(self, entryx_attr)
                        entryy = getattr(self, entryy_attr)

                        entryx.configure(state='normal')
                        entryy.configure(state='normal')

                        entryx.delete(0, 'end')
                        entryy.delete(0, 'end')
                        entryx.insert('end', self.x)
                        entryy.insert('end', self.y)

                        entryx.configure(state='readonly')
                        entryy.configure(state='readonly')

                        entries = getattr(self, 'entries', {})
                        entries[entry_num] = (entryx, entryy)
                        setattr(self, 'entries', entries)

                        return

                except:
                    pass
            else:
                if isinstance(key, KeyCode):
                    typed = str(key.vk)
                    print(typed)
                    if typed in ['97','98','99','100','101','102','103','104','105']:
                        entry_num = str(int(typed) - 96)

                        entryx_attr = f'entryx{entry_num}'
                        entryy_attr = f'entryy{entry_num}'

                        entryx = getattr(self, entryx_attr)
                        entryy = getattr(self, entryy_attr)

                        varx = entryx.get()
                        vary = entryy.get()

                        # Copiar o texto para a área de transferência
                        pyperclip.copy(f'({varx}, {vary})')

                        # Colar o conteúdo da área de transferência
                        pyautogui.hotkey('ctrl', 'v')

        self.logo = Image.open("logo.png")
        self.logo_image = CTkImage(self.logo, size=(200, 37))
        self.logo_label = CTkLabel(master=self.root, image=self.logo_image, text='')
        self.logo_label.pack(pady = 5)

        self.frame_master = CTkFrame(self.root, fg_color=self.root._fg_color)
        self.frame_master.pack(pady=3)

        self.frame_axis = CTkFrame(self.frame_master)
        self.frame_axis.pack(pady=5)

        self.label_x = CTkLabel(self.frame_axis, text='')
        self.label_x.grid(row=1, column=1, padx=20)

        self.label_y = CTkLabel(self.frame_axis, text='')
        self.label_y.grid(row=1, column=2, padx=20)

        self.scroll_frame = CTkScrollableFrame(self.root,
                                               width=170,
                                               height=20,
                                               scrollbar_button_color='#03fa6e',
                                               scrollbar_button_hover_color='#04a248')
        self.scroll_frame.pack()

        self.frame_switch = CTkFrame(self.root, fg_color=self.root._fg_color)
        self.frame_switch.pack(side=BOTTOM, pady = 5)

        self.switch_top = CTkSwitch(self.frame_switch,
                                    text='Always on Top',
                                    command=self.always_on_top,
                                    button_color='#03fa6e',
                                    button_hover_color='#04a248',
                                    progress_color='#04a248',
                                    font=("Arial", 12, "bold"))
        self.switch_top.grid(row=1, column = 1, padx = 5)

        self.option_menu = CTkOptionMenu(self.frame_switch,
                                         values=["Copy mode", "Paste mode"],
                                         text_color=self.root._fg_color,
                                         fg_color='#03fa6e',
                                         button_color='#03fa6e',
                                         button_hover_color='#04a248',
                                         dropdown_fg_color='#03fa6e',
                                         dropdown_hover_color='#04a248',
                                         dropdown_text_color=self.root._fg_color,
                                         dropdown_font=("Arial", 12, "bold"),
                                         font=("Arial", 12, "bold"))

        self.option_menu.grid(row=1, column = 2, padx = 5)


        # Titles of columns --
        header_labels = ['Num', 'Pos x', 'Pos y']
        for i, label_text in enumerate(header_labels):
            label = CTkLabel(self.scroll_frame, text=label_text, font=("Arial", 12, "bold"))
            label.grid(row=0, column=i, padx=2, pady=2)



        # Copy 1 --
        self.lbl1 = CTkLabel(self.scroll_frame, text=f'{1}').grid(row=1, column=0)
        # X1
        self.entryx1 = CTkEntry(self.scroll_frame, width=65, height=30)
        self.entryx1.grid(row=1, column=1, padx=2, pady=2)
        self.entryx1.configure(state='readonly')
        # Y1
        self.entryy1 = CTkEntry(self.scroll_frame, width=65, height=30)
        self.entryy1.grid(row=1, column=2, padx=2, pady=2)
        self.entryy1.configure(state='readonly')

        # Copy 2 --
        self.lbl2 = CTkLabel(self.scroll_frame, text=f'{2}').grid(row=2, column=0)
        # X2
        self.entryx2 = CTkEntry(self.scroll_frame, width=65, height=30)
        self.entryx2.configure(state='readonly')
        self.entryx2.grid(row=2, column=1, padx=2, pady=2)
        # Y2
        self.entryy2 = CTkEntry(self.scroll_frame, width=65, height=30)
        self.entryy2.configure(state='readonly')
        self.entryy2.grid(row=2, column=2, padx=2, pady=2)

        # Copy 3
        self.lbl3 = CTkLabel(self.scroll_frame, text=f'{3}').grid(row=3, column=0)
        # X3
        self.entryx3 = CTkEntry(self.scroll_frame, width=65, height=30)
        self.entryx3.configure(state='readonly')
        self.entryx3.grid(row=3, column=1, padx=2, pady=2)
        # Y3
        self.entryy3 = CTkEntry(self.scroll_frame, width=65, height=30)
        self.entryy3.configure(state='readonly')
        self.entryy3.grid(row=3, column=2, padx=2, pady=2)

        # Copy 4
        self.lbl4 = CTkLabel(self.scroll_frame, text=f'{4}').grid(row=4, column=0)
        # X4
        self.entryx4 = CTkEntry(self.scroll_frame, width=65, height=30)
        self.entryx4.configure(state='readonly')
        self.entryx4.grid(row=4, column=1, padx=2, pady=2)
        # Y4
        self.entryy4 = CTkEntry(self.scroll_frame, width=65, height=30)
        self.entryy4.configure(state='readonly')
        self.entryy4.grid(row=4, column=2, padx=2, pady=2)

        # Copy 5
        self.lbl5 = CTkLabel(self.scroll_frame, text=f'{5}').grid(row=5, column=0)
        # X5
        self.entryx5 = CTkEntry(self.scroll_frame, width=65, height=30)
        self.entryx5.configure(state='readonly')
        self.entryx5.grid(row=5, column=1, padx=2, pady=2)
        # Y5
        self.entryy5 = CTkEntry(self.scroll_frame, width=65, height=30)
        self.entryy5.configure(state='readonly')
        self.entryy5.grid(row=5, column=2, padx=2, pady=2)

        # Copy 6
        self.lbl6 = CTkLabel(self.scroll_frame, text=f'{6}').grid(row=6, column=0)
        # X6
        self.entryx6 = CTkEntry(self.scroll_frame, width=65, height=30)
        self.entryx6.configure(state='readonly')
        self.entryx6.grid(row=6, column=1, padx=2, pady=2)
        # Y6
        self.entryy6 = CTkEntry(self.scroll_frame, width=65, height=30)
        self.entryy6.configure(state='readonly')
        self.entryy6.grid(row=6, column=2, padx=2, pady=2)

        # Copy 7
        self.lbl7 = CTkLabel(self.scroll_frame, text=f'{7}').grid(row=7, column=0)
        # X7
        self.entryx7 = CTkEntry(self.scroll_frame, width=65, height=30)
        self.entryx7.configure(state='readonly')
        self.entryx7.grid(row=7, column=1, padx=2, pady=2)
        # Y7
        self.entryy7 = CTkEntry(self.scroll_frame, width=65, height=30)
        self.entryy7.configure(state='readonly')
        self.entryy7.grid(row=7, column=2, padx=2, pady=2)

        # Copy 8
        self.lbl8 = CTkLabel(self.scroll_frame, text=f'{8}').grid(row=8, column=0)
        # X8
        self.entryx8 = CTkEntry(self.scroll_frame, width=65, height=30)
        self.entryx8.configure(state='readonly')
        self.entryx8.grid(row=8, column=1, padx=2, pady=2)
        # Y8
        self.entryy8 = CTkEntry(self.scroll_frame, width=65, height=30)
        self.entryy8.configure(state='readonly')
        self.entryy8.grid(row=8, column=2, padx=2, pady=2)

        # Copy 9
        self.lbl9 = CTkLabel(self.scroll_frame, text=f'{9}').grid(row=9, column=0)
        # X9
        self.entryx9 = CTkEntry(self.scroll_frame, width=65, height=30)
        self.entryx9.configure(state='readonly')
        self.entryx9.grid(row=9, column=1, padx=2, pady=2)
        # Y9
        self.entryy9 = CTkEntry(self.scroll_frame, width=65, height=30)
        self.entryy9.configure(state='readonly')
        self.entryy9.grid(row=9, column=2, padx=2, pady=2)

        # Hearing keyboard
        listener = keyboard.Listener(
            on_press=on_key_press,
        )

        # Initial hearing
        listener.start()
        mouse_plot()

    def always_on_top(self):
        option = self.switch_top.get()
        if option == 1:
            self.root.attributes("-topmost", True)
        else:
            self.root.attributes("-topmost", False)


App()

