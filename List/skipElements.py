def skip_elements(elements):
	# Initialize variables
	new_list = []
	# Iterate through the list
	for i in range(len(elements)):
		# Does this element belong in the resulting list?
		if i%2==0:
			# Add this element to the resulting list
			new_list.append(elements[i])
		# Increment i
		i+=1

	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []


