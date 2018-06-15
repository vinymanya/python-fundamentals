
# Odd/Even
def odd_even():
	for i in range(1, 2001):
		if i % 2 == 0:
			print "Numer is {}. This is an even number.".format(i)
		else:
			print "Numer is {}. This is an odd number.".format(i)
# odd_even()

# Multiply
# Multiply each element in the list by the specified interger.
def multiply(array, num):
	for x in range(len(array)):
		array[x] *= num
	return array

result = multiply([2,4,10, 16], 6)
print result


# Hacker Challenge
def layered_multiple(arr):
	print arr
	# Initialize an empty list
	new_list = []
	for x in arr:
		# Create an empty list for every value in the arr
		val_list = []
		for i in range(0, x):
			# Append 1 into val_list
			val_list.append(1)
		new_list.append(val_list)
	return new_list


# strore the returned value
# y = layered_multiple(multiply([2, 4, 5], 3))
# print y

# Hacker Challenge
def layered_multiple(arr):
	print arr
	new_list = []
	for x in arr:
		val_list = []
		for i in range(0, x):
			val_list.append(1)
		new_list.append(val_list)
	return new_list

y = layered_multiple(multiply([ 2, 4, 6 ], 3))
print y

