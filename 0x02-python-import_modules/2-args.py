#!/usr/bin/python3
import sys

length = len(sys.argv)

if len(sys.argv) == 1:
    print("{} arguments.".format(length - 1))
else:
    print("{} argument:".format(length - 1))

    for i in range(1, length):
        print("{}: {}".format(i, sys.argv[i]))
