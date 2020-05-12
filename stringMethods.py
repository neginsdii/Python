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