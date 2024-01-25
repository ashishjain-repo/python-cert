#!/usr/bin/python

import sys
#Import the basic sys library

def parse_input(input_list):

    cmd_list = input_list[1:]

    result = ""

    if isinstance(input_list,list) and len(input_list) != 0:

        for element in cmd_list:
            if len(result) == 0:
                result = element
            else:
                result = result + " " + element
        
        return result
    
whom = parse_input(sys.argv)

if len(whom) > 0:
    print("Hello " + whom + "!\n")
else:
    print("Hello World")
