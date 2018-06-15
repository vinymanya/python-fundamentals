
# Create a program that prints a multiplication table to the console.
# Create a nested for loop to generate a multiplication table
print ("\t\t\tMultiplication Tables\n")
for i in range(1, 13):
	for j in range(1, 13):
		z = i*j
		print ("{} x {} = {}".format(i, j, z))
	print "-"*20



# Properly formated multiplication table
# for x in range(1, 11):
#         for y in range(1, 11):
#             z = x * y
#             print(z, end="\t")
#         print() #creates the space after the loop


# Properly formated multiplication table using python 3
# 3 tabs, title and a line break (\n)

# print ("\t\t\tMultiplication Tables\n")
# # Loop through numbers
# for i in range(1,13):
# 	print (i, end="\t")
# # Print vertical space
# print ()
# print ("_______________________________________________________________\n")
# for j in range(1,13):
# 	for k in range(1, 13):
# 		print (j*k, end="\t")
# 	print ("\n")
    



for i in range(1, 11):
	# variable to hold onto the results
	j = 6 * i
	# print ("6 x {} = {}".format(i, j)) 