#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        output = ""
        for element in my_list:
            if count < x:
                output += str(element)
                count += 1
        print("{}".format(output))
        return count
    except:
        return count
