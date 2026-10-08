# Part 2 (STRETCH) - filter the rows of a CSV file.
#
# This is a COMMAND-LINE program. You run it like:
#     python filter_csv.py people.csv city Oshawa
#
# The argument parser is finished for you. Complete the TODO.

import argparse
import csv
from email import header


def main():
    parser = argparse.ArgumentParser(
        description="Print the rows of a CSV where a column has a given value.")
    parser.add_argument("filename", help="the CSV file to read")
    parser.add_argument("column", help="the name of the column to match on")
    parser.add_argument("value", help="the value to match")
    args = parser.parse_args()


    with open(args.filename) as f:
        line = csv.reader(f)
        first_row = next(line)

        indexColumn=first_row.index(args.column)

        for row in line:
            if row[indexColumn] == args.value:
                print(",".join(row))

    # TODO: open args.filename and read it with csv.reader. The first row is the
    #   header. Find the position of args.column within the header, then print every
    #   data row (its values joined by commas) whose value in that column equals
    #   args.value.


if __name__ == "__main__":
    main()
