#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as cal
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(sys.argv[1])
        op = (sys.argv[2])
        b = int(sys.argv[3])
        if op == "+":
            print("{} {} {} = {}".format(a, op, b, cal.add(a, b)))
        if op == "-":
            print("{} {} {} = {}".format(a, op, b, cal.sub(a, b)))
        if op == "*":
            print("{} {} {} = {}".format(a, op, b, cal.mul(a, b)))
        if op == "/":
            print("{} {} {} = {}".format(a, op, b, cal.div(a, b)))
        elif op not in {"+", "-", "*", "/"}:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
