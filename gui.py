from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedTk

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Mr Worldwide but its Cars")
        master.configure(bg='#363636')
        master.geometry('900x500')
        
        #title 
        self.label = Label(master, text="Cars, better than trains")
        self.label.config(font=("Courier", 20))
        self.label.pack(padx=10, pady=10)

        #infoframe 
        self.finfo = Frame(master) 
        self.finfo.pack(side=LEFT, padx=10, pady=10)

        #left frame with car selection information 
        self.leftframe = Frame(self.finfo)
        self.leftframe.pack(side=LEFT, padx=10, pady=10)
 
        #right frame  with car selection information 
        self.fright = Frame(self.finfo)
        self.fright.pack(side=RIGHT, padx=10, pady=10)
        
        #menu to select location 
        self.mb = Menubutton(self.leftframe, text="My Location")
        self.mb.menu = Menu(self.mb)
        self.mb["menu"]=self.mb.menu

        a = IntVar()
        self.mb.menu.add_checkbutton(label = "location", variable =a)
        self.mb.pack(side=TOP, padx=10, pady=10)


        #menu to car 
        self.mb = Menubutton(self.leftframe, text="Car I want to Buy ")
        self.mb.menu = Menu(self.mb)
        self.mb["menu"]=self.mb.menu

        a = IntVar()
        self.mb.menu.add_checkbutton(label = "car", variable =a)
        self.mb.pack(side=TOP, padx=10, pady=10)

        #information about car 
        self.carinfo = Message(self.fright, text="lets say, hypothetically, you have a car. hypothetically, then, this is where the information of the car would go. like its price. its store location. um. model? brand? name. idk", width=200)
        self.carinfo.pack()


        #map 
        self.map = Canvas(master, bg="white", height=300, width=500)
        self.map.pack(side=RIGHT, padx=10, pady=10)
        self.USmap = PhotoImage(file="map.png")
        self.map.create_image((0,0),image=self.USmap,anchor='nw')

        #close button 
        self.close_button = Button(self.leftframe, text="Close", command=master.quit)
        self.close_button.pack(side=TOP, padx=10, pady=10)

    def greet(self):
        print("Greetings!")

def start():
    root = ThemedTk(theme="equilux")
    my_gui = GUI(root)
    root.mainloop()


