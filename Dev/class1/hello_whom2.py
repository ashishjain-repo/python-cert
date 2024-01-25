#!/usr/bin/python

# Import the basic sys library.
import sys

cmd_list = sys.argv[1:]

if isinstance(cmd_list,list) and len(cmd_list) != 0:

    print("List of arguments is greater than zero.\n")

    counter = 0

    for element in cmd_list:
        print("["+ str(counter)+"]["+element +"]")
        counter = counter + 1

    print("\n")
    print("Hello "+ cmd_list[1]+"!\n")

    print("List fot eh arguments for ["+sys.argv[len(sys.argv)-1] +"] is zero!\n")

    print("Hello World")