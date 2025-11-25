import sys
import csv
import pandas as pd

from util.contact import Contact
from util.structures import mergesort
from util.structures import ContactBST


def main():

    file = sys.argv[1]
    csv_file = pd.read_csv(file)
    sadfewfsef = csv_file['first_name']
    isudfoisaufd = csv_file['phone']
    balls = []
    for row in sadfewfsef:
        balls.append(row)

    sorted_list = sorted(balls)
    #print(sorted_list)

    sorted_phones = sorted(isudfoisaufd)
    print(sorted_phones)




if __name__ == "__main__":
    main()