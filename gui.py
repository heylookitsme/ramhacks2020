from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedTk

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Mr Worldwide but its Cars")
        
        #title 
        self.label = Label(master, text="Cars, better than trains")
        self.label.pack()

        #menu to select location 
        self.mb = Menubutton(master, text="My Location")
        self.mb.menu = Menu(self.mb)
        self.mb["menu"]=self.mb.menu

        a = IntVar()
        self.mb.menu.add_checkbutton(label = "hng", variable =a)
        self.mb.pack(side=LEFT)
        
        #map 
        self.map = Canvas(master, bg="white", height=300, width=1000)
        self.map.pack(side=RIGHT)

        #close button 
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack(side=LEFT)

    def greet(self):
        print("Greetings!")

def start():
    root = ThemedTk(theme="equilux")
    my_gui = GUI(root)
    root.mainloop()


