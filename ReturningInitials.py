def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result

print(initials("Universal Serial Bus"))
print(initials("local area network")) 
print(initials("Operating system")) 
print(initials("firstname lastname"))