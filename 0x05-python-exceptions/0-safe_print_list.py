#!/usr/bin/python3

def safe_print_list(my_list = [], x = 0):
	try:
	    i = 0
	    outpout = ""
	    for element in my_list:
		if i < x:
		   outpout += str(element)
		   i += 1
	    print(outpout)
	    return i
	except:
	       return i
