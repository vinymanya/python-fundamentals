# Import the random module to help generate a random integer
import random

# Scores and grades
# Generate a random number between 60 and 100
random_num = random.randint(60, 100)

score = random_num;
grades = ("A", "B", "C", "D")

# Write a program that generates a single random score everytime.
def scores_grades():
	print "\tScores and Grades"
	if score is 60 or score <= 69:
		print "Score: {}; Your grade is {}".format(score, grades[-1])
	elif score is 70 or score <= 79:
		print "Score: {}; Your grade is {}".format(score, grades[2])
	elif score is 80 or score <= 89:
		print "Score: {}; Your grade is {}".format(score, grades[1])
	elif score is 90 or score <= 100:
		print "Score: {}; Your grade is {}".format(score, grades[0])

	print "End of the program. Bye!"


# scores_grades()


# Write a program that generates 10 scores at the same time
def score_grades(repo):
	print "\n"
	print "\tScores and Grades"
	print "\t_________________\n"
	for x in range(0, repo):
		Score = random.randint(60, 101)
		if Score >= 60 and Score <= 69:
			print "Score:", Score,"; Your grade is D"
		elif Score >= 70 and Score <= 79:
			print "Score:", Score, "; Your grade is C"
		elif Score >= 80 and Score <= 89:
			print "Score:", Score, "; Your grade is B"
		elif Score >= 90 and Score <= 100:
			print "Score:", Score, "; Your grade is A"
	print "End of the semester. Bye!!!"
score_grades(10)


