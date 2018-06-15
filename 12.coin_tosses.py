# Import random module for generating a random integer
import random


# Coin Toss assignment
def coin_toss(repo):
	attempt_count = 1
	head_count = 0
	tail_count = 0
	for x in range(1,repo):
		new_toss = random.randint(0,1)
		if new_toss == 1:
			head_count += 1
			result = "head"
			print "Attempt #", attempt_count, ": Throwing a coin... It's a ", result, "! Got ", head_count, "head(s) so far and", tail_count, "tail(s) so far"
		else:
			tail_count += 1
			result = "tail"
			print "Attempt #", attempt_count, ": Throwing a coin... It's a ", result, "! Got ", head_count, "head(s) so far and", tail_count, "tail(s) so far"
			# Increment 'attempt_count' for every iteration
        	attempt_count += 1

	print "Ending the program, thank you!"
coin_toss(5001) 