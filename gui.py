from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedTk

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Mr Worldwide but its Cars")
        
        #title 
        self.label = Label(master, text="Cars, better than trains")
        self.label.pack(padx=10, pady=10)
        
        #menu to select location 
        self.mb = Menubutton(master, text="My Location")
        self.mb.menu = Menu(self.mb)
        self.mb["menu"]=self.mb.menu

        a = IntVar()
        self.mb.menu.add_checkbutton(label = "location", variable =a)
        self.mb.pack(side=LEFT, padx=10, pady=10)


        #menu to car 
        self.mb = Menubutton(master, text="Car I want to Buy ")
        self.mb.menu = Menu(self.mb)
        self.mb["menu"]=self.mb.menu

        a = IntVar()
        self.mb.menu.add_checkbutton(label = "car", variable =a)
        self.mb.pack(side=LEFT, padx=10, pady=10)


        #map 
        self.map = Canvas(master, bg="white", height=300, width=500)
        self.map.pack(side=RIGHT, padx=10, pady=10)
        self.USmap = PhotoImage(file="map.png")
        self.map.create_image((0,0),image=self.USmap,anchor='nw')

        #close button 
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack(side=LEFT, padx=10, pady=10)

    def greet(self):
        print("Greetings!")

def start():
    root = ThemedTk(theme="equilux")
    my_gui = GUI(root)
    root.mainloop()


