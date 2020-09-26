import re
import gui.py

def read_file(filename) -> list:
    to_return = []  # list of lists to be returned
    f = open(filename)  # default reading/text
    lines = f.readlines()

    for line in lines:
        regex = r',(?=([^\"]*\"[^\"]*\")*[^\"]*$)'
        to_add = re.split(regex, line)
        while None in to_add:
            to_add.remove(None)
        for i in range(0, len(to_add)):
            to_add[i] = to_add[i].replace('"', '').strip()
        to_return.append(to_add)
    return to_return


def fix_regex_mess(car_list) -> list:
    for car in car_list[1::]:
        del car[1:10:2]


def strings_to_ints(car_list) -> list:
    for car in car_list[1:]:
        if car[0].lower() == 'free': #parse shipping price into ints
            car[0] = 0
        elif car[0][0] == "$":
            car[0] = int(car[0][1:].replace(',', ''))
        else:
            car[0] = "Not Available"

        car[5] = int(car[5][1::].replace(',', ''))

    return car_list


def main():
    big_list = read_file('cali_cars.csv')
    print(big_list)
    fix_regex_mess(big_list)
    print(big_list)
    strings_to_ints(big_list)
    print(big_list)
    root = Tk()
    my_gui = MyFirstGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
