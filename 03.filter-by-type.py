# Filter by type

# Testing cases:
sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']


# Create a variable that hold the value of the above cases
case_tester = lL

# Variable to contain the data type
data_type = type(case_tester)
# Test for Interger
if data_type is int:
	if data_type >= 100:
		print "That's a big number!"
	else:
		print "That's a small number!"


# Test for string
elif data_type is str:
	if len(case_tester) >= 50:
		print "Long sentence!"
	else:
		print "Short sentence!"


# Test for list
elif isinstance(case_tester, list):
	if len(case_tester) >= 10:
		print " Big List!"
	else:
		print "Short List!"


# Note: It is recommended to use 'isinstance' over 'type' function when testing for an object's typee.