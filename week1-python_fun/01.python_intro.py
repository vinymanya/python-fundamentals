# Data types

# Primitive data types (They can only hold a single value)
# Passed by values : they can be copied across

# Interger
myInt = 9
# Float
myFloat = 5.7
# String
myStr = "Hello"
new_str = myStr + " World" # Adding two strings together
another_str = myStr, "Viny"

# print new_str
# print another_str

# Boolean
myBool = True



# Composite types (They can hold on to multiple values)
# List: is just like an array
my_list = [ 1, 2, 3, 4, 5 ]

# Print the last value on the list
# print my_list[len(my_list)-1]
# print my_list[-2]

# reset a value at particular index
my_list[0] = 50 
# print my_list

# You can also slice or extract portion of a list into a new list
new_list = my_list[:3]
# print new_list



# Dictionary: is just like an object (they are stored by string)
myDict = {
	"name": "Terra",
	"stack": "MEAN"
}

# You can change a dictionary's value on the fly
myDict["stack"] = "Python"
# Add a new key
myDict["location"] = "Seattle"
myDict["hobbies"] = ["soccer", "hiking", "cycling", "coding"]

# print myDict["hobbies"][-1]
# print myDict

# We can have a list of dictionaries
students = [
	{
		'location': 'Seattle', 
		'hobbies': ['soccer', 'hiking', 'cycling', 'coding'],
		'name': 'Terra', 
		'stack': 'Python'
	},
	{
		'location': 'Dallas', 
		'hobbies': ['basketball', 'swimming', 'dancing', 'coding'],
		'name': 'George', 
		'stack': 'MEAN'
	}
]

# print students[1]["hobbies"][0]


# Tuple: is just like an array that you can't change (immutable data type)
myTuple = ("Dallas", "hobbies", "Terra", "MEAN")
# print myTuple[1]

# You cannot change the value inside a tuple
# TypeError: 'tuple' object does not support item assignment
# myTuple[0] = "New York"
# print myTuple

# But you can change the entire tuple itself
myTuple = ("Cyprus", "hobbies", "Python")
# print myTuple

# A tuple can be used to swap values inside a list
myList = ["Viny", 35, "Cyprus", 99 ]
(myList[0], myList[-1]) = (myList[-1], myList[0])
print myList


# Loop
# Loop through a list
for i in range(0, len(myList)):
	print myList[i]

# Loop through numbers
for x in xrange(1, 10, 2):
	print x

# Loop through a tuple
for i in range(0, len(myTuple)):
	print myTuple[i]

# Loop through a string
word = "Viny"
for letter in range(0, len(word)):
	print word[letter]

# Loop through a dictionary
for key in myDict:
	print key, myDict[key]



# Conditionals
# To negate a conditional
# if not True:
# 	pass 
# if != True:
# 	pass

name = "Viny"
position = "student"

if name == "viny" and position == "student":
	print "He is studying"
else:
	print "He is having fun!"

if not name or position:
	print "He is not studying" 

# Function
def printDict():
	for key in myDict:
		print myDict[key]


printDict()

# Another way to access keys of a dictionary
person = {
	"name": "John",
	"age": 35,
	"occupation": "Developer"
}

for key in person.iterkeys():
	print key

# You can also access the values
for val in person.itervalues():
	print val

# To print all keys and values at once
for key, data in person.iteritems():
	print "{} : {}".format(key, data)
	# print key, "=", data


# You may also come across Nested dictionaries


nested_dict = {
	questions: [
		{"id": 1, "content": "What time is it?"}
		{"id": 2, "content": "What did you cook today?"}
		{"id": 3, "content": "Are you hungry?"}
	]
}
# Use the nested for loop to iterate over a nested dictionary.
for key, data in nested_dict.items():
	for val in data:
		print "Question #{}: {}".format(val["id"], val["content"])


# Lists from Dictionaries
# Create lists from a dictionary with methods such as .items(), .values() and .keys()
print person.items() # Generate a list with (key, value) tuple pairs
print person.values() # Generate a list with values from a dict
print person.keys() # Generate a list with keys from a dict


# Dictionaries from Lists
# You can also generate a dictionary from a list using methods such as .zip() and dict()
dishes = ["pizza", "sauerkraut", "paella", "hamburger"] 
countries = ["Italy", "Germany", "Spain", "USA"] 

countries_food = zip(countries, dishes)
print countries_food

# Make the above a real dictionary
new_countries_dishes = dict(countries_food)
print new_countries_dishes



