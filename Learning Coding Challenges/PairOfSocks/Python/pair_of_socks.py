import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
  count = 0
  value = 0
  dumm = {}

  for sock in ar:
    if (sock in dumm):
      value = dumm.get(sock)
      dumm[sock] = sock + 1
    else:
      dumm[sock] = 1

  for sock in dumm:
    value = int(dumm.get(sock))
    pair = math.ceil(value / 2)
    count = count + pair
  
  return count


def main():
  n = 9
  ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
  print(sockMerchant(9, ar))



if __name__ == '__main__':
  main()