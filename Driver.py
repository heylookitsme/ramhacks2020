def read_file(filename) -> list:
    to_return = []  # list of lists to be returned
    f = open(filename)  # default reading/text
    lines = f.readlines()

    for line in lines:
        to_add = line.split(",")
        for i in range(0, len(to_add)):
            to_add[i] = to_add[i].strip()
            to_return.append(to_add)
    return to_return


def main():
    big_list = read_file('cali_cars.csv')
    print(big_list)


if __name__ == "__main__":
    main()
