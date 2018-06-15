# Basic Dictionary data manipulation
my_dict = {
	"name": "Terranova",
	"age": 30,
	"country": "Cyprus",
	"favorite_language": "JavaScript"
}

def print_dict_data(data):
	
	print "My name is {}".format(data["name"])
	print "My age is {}".format(data["age"])
	print "My country of birth is {}".format(data["country"])
	print "My favorite language is {}".format(data["favorite_language"])

print_dict_data(my_dict)


# Write a function that can print out any dictionary keys and values:
person = {
	"name": "John",
	"age": 35,
	"occupation": "Developer"
}

def print_dict(my_dict):
	print ("\n")
	for key in my_dict:
		print "{} : {}".format(key, my_dict[key])

print_dict(person)

