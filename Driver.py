def read_file(filename) -> list:
    to_return = []  # list of lists to be returned
    try:
        f = open(filename)  # default reading/text
    except IOError:
        print("IOError has occurred, check filename?")
    try:
        s = f.readline()
        to_add = s.split(',')
        for i in range(0, len(to_add)):
            to_add[i] = to_add[i].strip()
    finally:
        return to_return


def main():
    print("Hello World")


if __name__ == "__main__":
    main()
