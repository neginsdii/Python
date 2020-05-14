multiples = [x*7 for x in range(1*11)]
print(multiples)
print("*"*30)
languages = ["Python", "Perl", "Java", "Go", "C++"]

lengths=[len(language) for language in languages]

i=0
for length in lengths:
  print("{:<6} : {:>3}".format(languages[i], length))
  i+=1
print("*"*30)
z=[x for x in range(0,101) if x%3 ==0]
print(z)