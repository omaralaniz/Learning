def linear_search(list, target):
  
  for i in range(0,len(list)):
    if list[i] == target:
      return i
  return None

x = linear_search([1,2,3,4], 7)

if x is not None:
  print("found in index: ", x)
else:
  print("item not found")