from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedTk

map_coordinates = {
    'WA' : (65,50),
    'OR' : (65,97),
    'CA' : (72,184),
    'NV' : (99,148),
    'ID' : (122,101),
    'MT' : (165,55),
    'WY' : (184,109),
    'UT' : (148,155),
    'AZ' : (148,207),
    'NM' : (198,208),
    'CO' : (203,158),
    'ND' : (245,52),
    'SD' : (249,89),
    'NE' : (254,127),
    'KS' : (264,160),
    'OK' : (279,197),
    'TX' : (260,241),
    'LA' : (323,249),
    'MS' : (345,225),
    'AR' : (319,205),
    'MO' : (319,163),
    'IA' : (311,119),
    'MN' : (303,69),
    'WI' : (345,89),
    'IL' : (351,143),
    'MI' : (395,105),
    'IN' : (376,145),
    'KY' : (389,174),
    'TN' : (379,195),
    'AL' : (374,225),
    'FL' : (420,273),
    'GA' : (402,227),
    'SC' : (428,215),
    'NC' : (439,195),
    'VA' : (450,170),
    'WV' : (429,161),
    'OH' : (410,142),
    'MD' : (464,153),
    'DE' : (477,159),
    'NJ' : (485,143),
    'PA' : (456,133),
    'NY' : (485,115),
    'CT' : (502,125),
    'RI' : (511,125),
    'MA' : (506,115),
    'VT' : (500,95),
    'NH' : (511,104),
    'ME' : (530,81),
    'AK' : (0,0),
    "HI" : (0,150)
}

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Mr Worldwide but its Cars")
        master.configure(bg='#363636')
        master.geometry('1080x720')
        
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
        self.map = Canvas(master, bg="white", height=322, width=627)
        self.map.pack(side=RIGHT, padx=10, pady=10)
        self.USmap = PhotoImage(file="map.png")
        self.map.create_image((0,0),image=self.USmap,anchor='nw')
        self.state_from = None
        self.state_to = None
                
        #close button 
        self.close_button = Button(self.leftframe, text="Close", command=master.quit)
        self.close_button.pack(side=TOP, padx=10, pady=10)

    def greet(self):
        print("Greetings!")

    def draw_map(self):
        if self.state_from and self.state_to:
            start=map_coordinates[self.state_from]
            end=map_coordinates[self.state_to]
            self.map.create_line(start[0],start[1],end[0],end[1],width=5,arrow=LAST)

    def set_map_path(self,state_from, state_to):
        self.state_from = state_from
        self.state_to = state_to
        self.draw_map()
        

def start():
    root = ThemedTk(theme="equilux")
    my_gui = GUI(root)
    my_gui.set_map_path("MD","WA")
    my_gui.set_map_path("AK","FL")
    root.mainloop()


