# List of dictionaries
# Part 1: Print names of students from the list
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def student_names(std_list):
	for obj in std_list:
		print "{} {}".format(obj["first_name"], obj["last_name"])

student_names(students)


# Part 2: Print out names of students and and instructors
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
}

def users_data(users):
	# Loop through the dictionary
	for group in users:
		# Initializing 'counter' variable counting the number of items for every category
		counter = 0
		print "\t",group
		print "\t__________\n"
		# Loop through the list for each category of users
		for each in users[group]: # This will give us the value of each category which the each list.
			counter += 1
			first_name = each["first_name"].upper()
			last_name = each["last_name"].upper()
			length = len(first_name) + len(last_name)
			# Print out values in the specified order
			print "{} - {} {} - {}".format(counter, first_name, last_name, length)
			print "\n"
users_data(users)



