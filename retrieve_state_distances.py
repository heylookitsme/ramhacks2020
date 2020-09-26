import urllib.request
states="""Alabama
Alaska
Arizona
Arkansas
California
Colorado
Connecticut
Delaware
Florida
Georgia
Hawaii
Idaho
Illinois
Indiana
Iowa
Kansas
Kentucky
Louisiana
Maine
Maryland
Massachusetts
Michigan
Minnesota
Mississippi
Missouri
Montana US
Nebraska
Nevada
New Hampshire
New Jersey
New Mexico
New York
North Carolina
North Dakota
Ohio
Oklahoma
Oregon
Pennsylvania
Rhode Island
South Carolina
South Dakota
Tennessee
Texas
Utah
Vermont
Virginia
Olympia US
West Virginia
Wisconsin
Wyoming"""
# distancefromto.net does not recognize the state of washington, sowe use olympia instead
states = states.lower().replace(" ","-").split("\n")
output_csv = open("distances.csv", "w")
for state_from in states:
    for state_to in states:
        html = str(urllib.request.urlopen('https://www.distancefromto.net/distance-from-'+state_from+'-to-'+state_to).read())
        e=html.rfind(" kilometers")
        s=e-1
        while html[s] != " ":s-=1
        distance = html[s+1:e]
        if "olympia-us" in [state_from,state_to]:print("olympia-us")
        if state_from == "olympia-us": state_from = "washington"
        if state_to == "olympia-us": state_to = "washington"
        print(state_from, "to", state_to, "->", distance)
        output_csv.write(state_from + "," + state_to + ",\"" + distance + "\"\n")
output_csv.close()
