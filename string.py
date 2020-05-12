def first_and_last(message):
  if message=="":
    return True
  if message[0]== message[len(message)-1]:
    return True
  else:
    return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

color= "Orange"
print(color[1:4])
print(color[:4])
print(color[4:])
