from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedTk
import csv

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

cars = []

filepath = "data_files"
state_files=["cali_cars.csv","texas_cars.csv","chicago_cars.csv","washington_cars.csv","penn_cars.csv"]

for state_fname in state_files:
    state_file = open(filepath+"/"+state_fname)
    file_reader = csv.reader(state_file,quotechar="\"")
    for row in file_reader:
        if row[0]=='Shipping' or len(row[1])!=2 or len(row[2])!=2:continue
        cars.append(row)      
    state_file.close()

distances = {}
# https://gist.github.com/rogerallen/1583593
abbrev = {
    'alabama': 'AL',
    'alaska': 'AK',
    'American Samoa': 'AS',
    'arizona': 'AZ',
    'arkansas': 'AR',
    'california': 'CA',
    'colorado': 'CO',
    'connecticut': 'CT',
    'delaware': 'DE',
    'District of Columbia': 'DC',
    'florida': 'FL',
    'georgia': 'GA',
    'Guam': 'GU',
    'hawaii': 'HI',
    'idaho': 'ID',
    'illinois': 'IL',
    'indiana': 'IN',
    'iowa': 'IA',
    'kansas': 'KS',
    'kentucky': 'KY',
    'louisiana': 'LA',
    'maine': 'ME',
    'maryland': 'MD',
    'massachusetts': 'MA',
    'michigan': 'MI',
    'minnesota': 'MN',
    'mississippi': 'MS',
    'missouri': 'MO',
    'montana-us': 'MT',
    'nebraska': 'NE',
    'nevada': 'NV',
    'new-hampshire': 'NH',
    'new-jersey': 'NJ',
    'new-mexico': 'NM',
    'new-york': 'NY',
    'north-carolina': 'NC',
    'north-dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'ohio': 'OH',
    'oklahoma': 'OK',
    'oregon': 'OR',
    'pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'rhode-island': 'RI',
    'south-carolina': 'SC',
    'south-dakota': 'SD',
    'tennessee': 'TN',
    'texas': 'TX',
    'utah': 'UT',
    'vermont': 'VT',
    'Virgin Islands': 'VI',
    'virginia': 'VA',
    'washington': 'WA',
    'west-virginia': 'WV',
    'wisconsin': 'WI',
    'wyoming': 'WY'
}

with open("distances.csv") as dist_file:
    reader = csv.reader(dist_file,quotechar="\"")
    for row in reader:
        print(row[2])
        distances[abbrev[row[0].strip()]+abbrev[row[1].strip()]]=int(row[2].replace(",","").replace("\"",""))


m,b = 0.5629778277116556,37.36332648769955


class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Mr Worldwide but its Cars")
        master.configure(bg='#363636')
        master.geometry('1080x720')
        
        #title 
        self.label = Label(master, text="Where are your cars coming from?")
        self.label.config(font=("Courier", 15))
        self.label.pack(padx=10, pady=10)

        #infoframe 
        self.finfo = Frame(master, width=200) 
        self.finfo.pack(side=LEFT, padx=10, pady=10)

        #left frame with car selection information 
        self.leftframe = Frame(self.finfo)
        self.leftframe.pack(side=LEFT, padx=10, pady=10)
        
        #frame with searchbar and results
        self.searchframe = Frame(self.leftframe)
        self.searchframe.pack(side=TOP, padx=10, pady=10)
 
        #right frame  with car selection information 
        self.fright = Frame(self.finfo)
        self.fright.pack(side=TOP, padx=10, pady=10)
        
        #menu to select location 
        self.mb = Menubutton(self.fright, text="My Location")
        self.mb.menu = Menu(self.mb)
        self.mb["menu"]=self.mb.menu

        self.loc = StringVar()
        self.loc.set("AL")
        for state in map_coordinates.keys():
            self.mb.menu.add_checkbutton(label = state, variable = self.loc, command = (lambda state: lambda: self.select_location(state))(state))
        self.mb.pack(side=TOP, padx=10, pady=10)

        #car entry field
        self.search_string = StringVar()
        self.ce = Entry(self.searchframe, textvariable=self.search_string,width=32)
        self.search_string.trace('w',lambda a,b,c:self.search())
        self.ce.pack(side=TOP,padx=0,pady=0)

        #car search results
        self.cardata = None
        self.cr = Listbox(self.searchframe,width=32,height=64)
        self.cr.bind("<<ListboxSelect>>", lambda e:self.select_car(self.cr.curselection()))
        self.populate_search()
        self.cr.pack(side=LEFT,fill=BOTH,padx=0,pady=0)

        #car search scrollbar
        self.sscroll = Scrollbar(self.searchframe)
        self.sscroll.pack(side=RIGHT,fill=Y,padx=0,pady=0)

        self.cr.config(yscrollcommand=self.sscroll.set)
        self.sscroll.config(command=self.cr.yview)

        #menu to car 
        #self.mb = Menubutton(self.leftframe, text="Car I want to Buy ")
        #self.mb.menu = Menu(self.mb)
        #self.mb["menu"]=self.mb.menu

        #a = StringVar()
        #a = cars[0]
        #for car in cars:
        #    self.mb.menu.add_checkbutton(label = car[3]+" "+car[4], variable = a, command = self.select_car(a))
        #self.mb.pack(side=TOP, padx=10, pady=10)

        #information about car 
        self.carinfo = Message(self.fright, text="Pick a car to get started :)", width=200)
        self.carinfo.pack(side=TOP,padx=10,pady=10,fill=BOTH)


        #map 
        self.map = Canvas(master, bg="white", height=322, width=627)
        self.map.pack(side=TOP, padx=10, pady=10)
        self.USmap = PhotoImage(file="map.png")
        self.map.create_image((0,0),image=self.USmap,anchor='nw')
        self.state_from = None
        self.state_to = None

        #graph visual
        self.graf = Canvas(master, bg="white", height=322, width=627)
        self.graf.pack(side=TOP, padx=10, pady=10)
        self.linreg = PhotoImage(file="reg_display.png")
        self.graf.create_image((30,0),image=self.linreg,anchor='nw')
                
        #close button 
        self.close_button = Button(self.fright, text="Close", command=master.quit)
        self.close_button.pack(side=TOP, padx=10, pady=10)

        # percentage bar
        self.percentage = Progressbar(self.fright, mode="determinate", length=32)
        self.percentage.pack(side=TOP,padx=10,pady=10)

    def draw_map(self):
        if self.state_from and self.state_to:
            start=map_coordinates[self.state_from]
            end=map_coordinates[self.state_to]
            dist = (start[0]-start[1])**2 + (end[0]-end[1]) **2
            color = '#919191'
            if dist > 0:
                color = '#83db48'
            if dist > 20000: 
                color = '#edaa24'
            if dist > 40000: 
                color = '#a65'
            print(dist)    
            self.map.create_line(start[0],start[1],end[0],end[1],width=5,arrow=LAST,fill=color)

    def set_map_path(self, state_from, state_to):
        self.state_from = state_from
        self.state_to = state_to
        self.map.create_image((0,0),image=self.USmap,anchor='nw')
        self.draw_map()
    
    def select_location(self, state):
        self.loc.set(state)
        print(self.loc)
        self.update_info()

    def update_carinfo(self, car_data):
        distance = distances[car_data[1]+self.loc.get()]
        price = int(car_data[5].replace("$","").replace(",",""))
        self.estimate = round(m * distance + b)
        total = price + self.estimate
        percentage = round(self.estimate * 100 / total)
        s = ("Model: " + car_data[3] + " " + car_data[4] + "\n" +
                "Price: " + car_data[5] + "\n" +
                "Mileage: " + car_data[6] + " miles\n" +
                "Store: " + car_data[7] + "\n" +
                "Location: " + car_data[1] + "\n" +
                "Estimated Transfer Fee: $" + str(self.estimate) + "\n" +
                "Total (Price and Transfer Fee): " + total + "\n" +
                "Transfer Fee Percentage of Total: " + percentage + "%\n")
        self.carinfo.configure(text=s)
        self.percentage["value"] = percentage
    
    def select_car(self, i):
        print(i)
        if i:
            index = int(i[0])
            self.cardata = cars[self.search_map[index]]
        self.update_info()
    
    def populate_search(self):
        self.cr.delete(0,END)
        self.search_map = []
        search_lower = self.search_string.get().lower()
        for i in range(len(cars)):
            car = cars[i]
            car_name = car[3]+" "+car[4]
            if car_name.lower().find(search_lower) >= 0:
                self.cr.insert(END, car_name)
                self.search_map.append(i)
        print("done populating")
    
    def search(self):
        print("yeet")
        self.populate_search()

    def update_info(self):
        if self.cardata:
            self.update_carinfo(self.cardata)
            self.set_map_path(self.cardata[1],self.loc.get())


def start():
    root = ThemedTk(theme="equilux")
    my_gui = GUI(root)
    root.mainloop()


