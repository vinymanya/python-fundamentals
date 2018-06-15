
# Write a program that converts two lists into a dictionary
# The first list contains keys and the second list contains values.

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dophins", "llamas", "licarne", "bataillon"]


def make_dict(list1, list2):
	new_list = zip(list1, list2)
	new_dict = dict(new_list)
	return new_dict

# my_dict = make_dict(name, favorite_animal)
# print my_dict


# Hacker challenge
def dict_from_lists(list1, list2):
	# compare the length of both lists
	if len(list1) > len(list2):
		new_list = zip(list1, list2)
		new_dict = dict(new_list)
	else: # List2 should be used for the keys
		new_list = zip(list2, list1)
		new_dict = dict(new_list)
	return new_dict

my_dict = dict_from_lists(name, favorite_animal)
print my_dict



