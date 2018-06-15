# Find and replace

words = "It's thanksgiving day. It's my birthday, too!"

print words.find("day")	# 18
# Replace the first instance of 'day' with 'month'
print words.replace("day", "month", 1) 


# Min and Max
x1_list = [2, 54, -2, 7, 12, 98]
print "The lowest number is", min(x1_list) # Returns the lowest value in a sequence
print "The highest number is", max(x1_list) # Returns the highest value in a sequence


# Find first and last value in a list
x2_list = ["hello", 2, 54, -2, 7, 12, 98, "world"]
first = x2_list[0]
last = x2_list[-1] # or x2_list[len(x2_list)-1]
new_list = [first, last]

print new_list

# New sorted list
x3_list = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]

x3_list.sort() # Sort the list above
print x3_list
# Extract first half of the list starting from zero index
first_half = x3_list[:len(x3_list)/2]
# Extract the second half
second_half = x3_list[len(x3_list)/2:]

# Insert the first_half into the second_half at the first index
second_half.insert(0, first_half)
print second_half











