new_list = [1, 2, 3, 10]
result = new_list[1] + new_list[2]

if 1 in new_list: 
  print("yeah it is in here bruh")
else:
  print("not in here bruh")

new_list.extend([1,2])
print(new_list)
print(result)