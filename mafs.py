import csv
from matplotlib import pyplot as plt
import numpy as np

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

points=[]

filepath = "data_files"
state_files=["cali_cars.csv","texas_cars.csv","chicago_cars.csv","washington_cars.csv","penn_cars.csv"]

for state_fname in state_files:
    state_file = open(filepath+"/"+state_fname)
    file_reader = csv.reader(state_file,quotechar="\"")
    for row in file_reader:
        try:
            cost=int(row[0].strip().replace(",","").replace("\"","").replace("$",""))
            origin=row[1].strip()
            dest=row[2].strip()
            points.append([distances[origin+dest],cost])
            print(origin, dest, distances[origin+dest],cost)
        except:
            pass
        
    state_file.close()

points.sort()
ship_distances = [x[0] for x in points]
costs = [x[1] for x in points]

m,b=np.polyfit(ship_distances,costs,1)
print("m =", m)
print("b =", b)

x_max = max(ship_distances)
x = [0, x_max]
y = [b, m*x_max+b]
plt.plot(ship_distances,costs,'yo',x,y,'--k')
plt.xlabel("Shipping Distance")
plt.ylabel("Shipping Cost")
plt.title("Cost as a Function of Distance")
plt.show()



