animals=['Lion', 'Zebra','Dolphin', 'Monkey', 'Tiger'
]
chars=0
for animal in animals:
  chars+=len(animal)

print("Total characters:{}, Average length:{}".format(chars,chars/len(animals)))



winners=['Ashley','Dylan','Manny']

for index, person in enumerate(winners):
  print("{} - {}".format(index+1,person))



  def skip_elements(elements):

  new_list=[]
  for index,element in enumerate(elements):
    if index%2==0:
      new_list.append(element)
  return new_list




print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

#*********************
def full_emails(people):
  result=[]
  for email, name in people:
    result.append("{} <{}>".format(name, email))
  return result

print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))
