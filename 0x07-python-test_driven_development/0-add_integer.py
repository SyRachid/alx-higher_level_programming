#!/usr/bin/python3
#the module to add two integer
def add_integer(a, b=98):
	"""int a: parameter which type is integer of float
	int b: parameter
	return the sum a + b"""     
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b)!=float:
        raise TypeError("b must be an integer")
    return int(a) +  int(b)

if __name__ == "__main__":
""" import doctest""""
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
