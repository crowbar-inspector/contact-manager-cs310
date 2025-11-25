import sys

import pandas as pd


def main():
    file = sys.argv[1]
    csv_file = pd.read_csv(file)
    sadfewfsef = csv_file['first_name']
    isudfoisaufd = csv_file['phone']
    balls = []
    for row in sadfewfsef:
        balls.append(row)

    sorted_list = sorted(balls)
    # print(sorted_list)

    sorted_phones = sorted(isudfoisaufd)
    print(sorted_phones)


if __name__ == "__main__":
    main()
