#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    somme = 0
    for i in range(1, len(sys.argv), 1):
        somme +=  int(sys.argv[i])
    print("{}".format(somme))
