from customtkinter import *
from tkinter import CENTER, BOTTOM, LEFT, RIGHT, TOP
from pyautogui import position

class App:
    def __init__(self):
        self.root = CTk()
        self.root.geometry('300x200')
        self.root.title('Mouse Plot')
        self.root.attributes("-topmost", False)
        self.main()
        self.root.mainloop()


    def main(self):

        def mouse_plot():
            x, y = position()

        self.frame_axis = CTkFrame(self.root)
        self.frame_axis.pack()
        self.label_x = CTkLabel(self.frame_axis, text='Position X')
        self.label_x.grid(row=1, column = 1, padx = 20)
        self.label_y = CTkLabel(self.frame_axis, text='Position y')
        self.label_y.grid(row=1, column = 2, padx = 20)
        self.switch_top = CTkSwitch(self.root, text='Always on Top', command=self.always_on_top)
        self.switch_top.pack(side = BOTTOM)


    def always_on_top(self):
        option = self.switch_top.get()
        if option == 1:
            self.root.attributes("-topmost", True)
        else:
            self.root.attributes("-topmost", False)


App()