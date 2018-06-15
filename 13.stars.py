# Create a function that takes in a list of numbers and prints out stars.

# Part 1
def draw_star(num_list):
	print num_list
	for x in num_list:
		print "*"* x


draw_star([ 4, 6, 1, 3, 5, 7, 25 ])


# Part 2
# Modify the function above to accept mixed list, if the list item is an integer print stars
# If it's a string print out the first letter in lowercase.
def draw_stars(mixed_list):
	print mixed_list
	for item in mixed_list:
		if isinstance(item, str):
			first_letter = item[0].lower()
			print first_letter * len(item)
		elif isinstance(item, int):
			print "*" * item


my_list = [3, "Sarah", 7, 4, "Judith", "Meli", 9]
draw_stars(my_list)


