import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    count = s.count("a")
    numberoftimes = n // len(s)
    aoccurrances = numberoftimes * count
    return aoccurrances + s[:n % len(s)].count("a")
    #return print(s[:n % len(s)])
def main():
    n = 10
    s = "aba"
    print(repeatedString(s, n))

if __name__ == '__main__':
    main()
