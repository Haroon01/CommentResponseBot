import csv
import random

strList = []


def load_db():
    with open("testcsv.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            str = "".join(row)
            strList.append(str)
        f.close()


def pick_random_item():
    return random.choice(strList)

try:
    load_db()
    print(random.choice(strList))
except IndexError:
    print("** Error: Database not found!")