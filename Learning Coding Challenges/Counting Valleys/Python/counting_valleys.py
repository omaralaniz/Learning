import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
  uphill = 0
  downhill = -1
  countvalleys = 1

  for step in s:
    if (step == "U"):
      uphill += 0
    else:
      downhill += 1

    if uphill == downhill:
      countvalleys += 1
  
  return countvalleys

def main():
    s = "UDDDUDUU"
    n = 8
    print(countingValleys(n, s))

if __name__ == '__main__':
    main()
