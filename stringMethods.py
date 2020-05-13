names=["john","harry","megan","sara","kira"]
for name in names:
  if name.endswith("ra"):
    print (name, end=" ")

print("\n")
message=" This a message with white spaces "
print(message.strip())
print(message.rstrip())
print(message.lstrip())

sentence=" "
sentence=sentence.join(['hello,', "this", "is", "for", "practice"])
print(sentence)

print(message.find("for"))
print(sentence.index("f"))
print(sentence.find("for"))
print(sentence.capitalize())
print(sentence.title())

print("*"*20)
name="Manny"
lucky_number=len(name)*3
print("Hello {}, Your lucky number is: {}".format(name,lucky_number))

print("Your lucky number is {number}, {name}".format(number=lucky_number, name=name))
print("*"*20)
prices=[8,12,22,4,2,45]
tax=1.09
for price in prices:
  print("Base price: ${:0.2f}, With Tax: ${:0.2f}".format(price,price*tax))

  print("_"*20)
 def to_celsius(x):
    deg=(x-32)*5/9
    print("{:>3} F | {:>6.2f} c".format(x,deg))

  degs=[0,10,20,30,40,50,60,70,80,90,100]
for deg in degs:
  to_celsius(deg)

  print("_"*20)
def nametag(first_name, last_name):
	return(first_name+" {}.".format(last_name[0]))

print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 