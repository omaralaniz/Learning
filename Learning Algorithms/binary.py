def binary_search(list, target):
  first = 0
  last = len(list) - 1

  while first <= last:
    midpoint = (first + last) // 2

    if list[midpoint] == target:
      return midpoint
    elif list[midpoint] < target:
      first = midpoint + 1
    else:
      last = midpoint - 1
  
  return None

def recursive_binary_search(list, target):
  if len(list)  == 0:
    return False
  else:
    midpoint = (len(list)) // 2
    if list[midpoint] == target:
      return True;
    else:
      if list[midpoint] < target:
        return recursive_binary_search(list[midpoint +1: ], target)
      else:
        return recursive_binary_search(list[:midpoint], target)
  
  return False

def verify(index):
  if index is not None:
    print("the item is in this index: ", index)
  else:
    print("item was not found")

result = binary_search([1, 2, 3, 4, 5, 6, 10], 67)

verify(result)

x = recursive_binary_search([1, 2, 3, 4, 5, 6, 10], 3)
print(x)