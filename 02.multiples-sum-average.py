# Multiples
# Part 1: Write code that prints all the odd numbers from 1 to 1000
for x in xrange(0, 1001):
	if x % 2 != 0:
		print x
	continue


# Part 2:  Create another program that prints all the multiples of 5 from 5 to 1 000 000.
for x in xrange(5, 1000001):
	if x % 5 == 0:
		print x
	continue

# Sum List
""" Create a program that prints the sum of all values in the list """
a = [ 1, 2, 5, 10, 255, 3 ]
my_sum = 0
for i in a:
	my_sum += i
print my_sum 	

# Average List
# The average is simply the sum divided by the number of elements in the list
print my_sum/len(a)