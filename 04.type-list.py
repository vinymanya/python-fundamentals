
# Print the type of each item in the list
# Test Cases:
ls = ['magical unicorns',19,'hello',98.98,'world']
lx = [ 2, 3, 1, 7, 4, 12 ]
lc = ['magical','unicorns']
my_List = [1.5, 2017, 6+4l, 'suspicious', (6, 8), [1,2,3,5,6,7,8,12],{"make":'BMW', "model":'X5'}]

case_tester = lc
sumList = 0
new_str = ""
arr = ""
# Interger:

if isinstance(case_tester, int):
	arr = "int"
# string:
elif isinstance(case_tester, str):
    arr = "str"
    
# Mixed:
else:
	arr = "mixed"

for i in range(0, len(case_tester)):
	if type(case_tester[i]) is int or type(case_tester[i]) is float:
		sumList += case_tester[i]
	elif type(case_tester[i]) is str:
		new_str = new_str + " " + case_tester[i]

if arr == "int":
	print "The array you entered is of integer type"
	print "Sum:", sumList 
elif arr == "str":
	print "The array you entered is of string type"
	print "String:", new_str
elif arr == "mixed":
	print "The array you entered is of mixed type"
	print "String:", new_str
	print "Sum:", sumList


