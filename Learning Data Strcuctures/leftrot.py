def rotLeft(a, d):
    for i in range(d):
        
        a.append(a.pop(0))

    return a

print( rotLeft([1,2,3,4], 3))
for i in range(3):
  print(i)