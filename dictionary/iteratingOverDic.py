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
