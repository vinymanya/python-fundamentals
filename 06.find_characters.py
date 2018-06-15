# Write a program that takes a list of strings and a string that contain a single character
# Print all strings with that character.

word_list = ["hello", "world", "name", "is", "Anna", "wow"]
# Set method returns a new instance of the specified object.
# Character to be searched in each individual str in the list
char = set("o")

# List of words contain the character above
new_list = []

# Loop through the list
for word in word_list:
	# Loop through the word
	for letter in word:
		if set(letter) == char:
			new_list.append(word)
		continue

# Print out the new list
print new_list






