import csv


def read_property(key, file):
    with open(file) as f:
        list = f.readlines()
    for line in list:
        entry = line.strip().split(" = ")
        if entry[0] == key:
            return entry[1]


# value = read_property("browser","../first/browser.config")
# print(value)

def get_rows(csv_file):
    rows = []
    with open(csv_file, 'r') as f:
        line = csv.reader(f)
        next(line)
        for row in line:    # list of colum values
#map(str.strip, my_list):
#Iterates through each element in my_list.
#Applies the str.strip() method to each element, removing leading and trailing whitespaces.
#Returns an iterator containing the stripped strings. list(...):
#Converts the iterator returned by map() into a new list

            row = list(map(str.strip, row))
            print(row)
            rows.append(row)
    return rows             #list of rows where each row is a list of column values


#print(get_rows("../data/invalid.csv"))
