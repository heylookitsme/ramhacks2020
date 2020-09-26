from bs4 import BeautifulSoup
html = open("Tinley_Park_Chicago.html","r")
html = html.read()
soup = BeautifulSoup(html, 'html.parser')

transfers = [x.text for x in soup.findAll("span", {"class": "transfer"})]
year_make = [x.text for x in soup.findAll("span", {"class": "year-make"})]
model_trim = [x.text for x in soup.findAll("span", {"class": "model-trim"})]
price = [x.text for x in soup.findAll("span", {"class": "price"})]
miles = [x.text for x in soup.findAll("span", {"class": "miles"})]
store = [x.text for x in soup.findAll("span", {"class": "store"})]

for x in transfers:
    if "•" in x: 
        print(x.split(" • ")[0].split(" ")[0])
    else:
        print(x)
print("\n")
for x in transfers:
    if "•" in x: 
        print(x.split(" • ")[1].split(" ")[0])
    else:
        print("N/A")
print("\n")
for x in transfers:
    if "•" in x: 
        print(x.split(" • ")[1].split(" ")[2])
    else:
        print("N/A")
print("\n")
for x in year_make:
    print(x)
print("\n")
for x in model_trim:
    print(x)
print("\n")
for x in price:
    print(x[:-1])
print("\n")
for x in miles:
    print(x.split(" ")[0])
print("\n")
for x in store:
    print(" ".join(x.split(" ")[1:]))
