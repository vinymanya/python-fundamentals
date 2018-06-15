# Write a program that compares two lists and print a message depending on whether the lists are identical or not.

# Test cases
list_one = [1,2,5,6,3]
list_two = [1,2,5,6,2]

list_three = [1,2,5,6,5]
list_four = [1,2,5,6,5,3]

list_five = [1,2,5,6,5,16]
list_six = [1,2,5,6,5]

list_seven = ['celery','carrots','bread','milk']
list_eight = ['celery','carrots','bread','cream']

# Comaparing two lists
if list_five == list_six:
	print "The lists are the same!"
else:
	print "The lists are not the same!"