# Part 1 - a small "find" tool (like a simplified `grep`).
#
# This is a COMMAND-LINE program: you run it from the terminal and pass it
# arguments, e.g.   python find.py apple sample.txt
#
# The argument parser is started for you. Finish the TODOs below.

import argparse
from fileinput import filename, close


def main():
    parser = argparse.ArgumentParser(
        description="Print the lines of a file that contain a given pattern.")
    parser.add_argument("pattern", help="the text to look for")
    parser.add_argument("filename", help="the file to search")
    # TODO: add an optional flag -i / --ignore-case  (use action="store_true")
    parser.add_argument("-i", "--ignore-case", action="store_true")


    args = parser.parse_args()

    with open(args.filename) as s:
        for i, text in enumerate(s, start=1):
                text = text.rstrip("\n")
                if args.pattern in text and not args.ignore_case:
                    print(str(i) + ": "+ text)
                elif args.pattern.lower() in text.lower() and args.ignore_case:
                    print(str(i) + ": "+ text)



    # TODO: open args.filename and read its lines. For each line, numbered starting
    #   at 1, print "<number>: <line>" when the line contains args.pattern.
    #   If the --ignore-case flag was given, match without caring about upper/lower
    #   case (hint: compare the lowercased versions of both).

    close()

if __name__ == "__main__":
    main()
