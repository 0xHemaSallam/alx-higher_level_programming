#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    length = len(sys.argv)

    if length == 1:
        print("0 arguments.")
    else:
        print("{} {}:".format(
            length - 1, "argument" if length == 2 else "arguments"))

        for i in range(1, length):
            print("{}: {}".format(i, sys.argv[i]))
