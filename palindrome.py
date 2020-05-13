def is_palindrome(input_string):
	# We'll create two strings, to compare them
	input_string=input_string.lower()
	new_string = input_string.split()
	reserve_string = ""
	for word in new_string:
	  reserve_string+=word
	new_string = ""
	# Traverse through each letter of the input string
	index=len(reserve_string)-1
	while index>=0:
	  new_string+=reserve_string[index]
	  index-=1
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
	# Compare the strings
	if new_string == reserve_string:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
print(is_palindrome("Bab"))