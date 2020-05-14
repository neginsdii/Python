def pig_latin(text):
  say = " "
  # Separate the text into words
  words = text.split()
  for index in range(len(words)):
    # Create the pig latin word and add it to the list
    words[index]=words[index][1:]+words[index][0]+"ay"
    # Turn the list back into a phrase
  return say.join(words)
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"