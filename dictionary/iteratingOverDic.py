file_counts={"jpg" : 10 , "txt": 14, "csv":2, "py":23, "html":7}

for extension in file_counts:
  print(extension)

for ext, amount in file_counts.items():
  print("There are {} files with the .{} extension.".format(amount,ext))

print("*"*20)

for value in file_counts.values():
  print(value)

print("*"*20)

for key in file_counts.keys():
  print(key)

print("*"*20)

def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  list1.reverse()
  for item in list2:
    list1.append(item)
  return list1
  
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))
