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

def replace_ending(sentence, old, new):
	# Check if the old string is at the end of the sentence 
	if sentence.endswith(old):
		i = sentence.rfind(old)
		new_sentence = sentence[:i]+new
		return new_sentence

	return sentence
	
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"



