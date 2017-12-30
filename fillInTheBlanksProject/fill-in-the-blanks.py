from random import randint

def salutation():
	userName = raw_input("Hello friend! What is your name? ")
	print ("Hello ",userName,"\nWelcome to Sayings game!")
	return userName

def explanation(userName):
	gameExplanation = """this game consists of the following:\n
	You willbe given a saying with blank spaces for you to fill in.\n
	In order to win the game, you need to guess all blanks correctly!\n
	You will have 3 attempts to complete each level. Good luck!"""
	print (userName,", ", gameExplanation)

def difficulty():
	easy = "easy"
	medium = "medium"
	hard = "hard"
	informed = False
	level=0
	while not informed:
		selectionMessage="Please choose the difficulty level from the following"
		text = raw_input(selectionMessage,": ",easy,"/",medium,"/",hard)
		if text.lower() == easy.lower():
			print ("Ok! You chose easy!")
			informed = True
			level = 0
		elif text.lower() == medium.lower():
			print ("Ok! You chose medium!")
			informed = True
			level = 1
		elif text.lower() == hard.lower():
			print ("Ok! You chose hard!")
			informed = True
			level = 2
		else:
			print ("Sorry, ",text," is not one of the options.")
	return level

def questions(level):
	easy = [["Two wrongs don't make a ___1___.",["right"]],
			["The pen is mightier than the ___1___.",["sword"]],
			["No man is an ___1___.",["island"]]
			]
	
	medium = [["When the ___1___ gets ___2___, the ___2___ get ___1___.",["going","tough"]],
			["People who live in ___1___ houses should not throw ___2___.",["glass","stones"]],
			["Hope for the ___1___, but prepare for the ___2___.",["best","worst"]]
			]

	hard = [["A ___1___ is worth a ___2___ ___3___.",["picture","thousand","words"]],
			["Never ___1___ a gift ___2___ in the ___3___.",["look","horse","mouth"]],
			["You can't make an ___1___ without ___2___ a few ___3___.",["omelet","breaking","eggs"]]
			]

	questions = [easy, medium, hard]

	return questions[level][randint(0,2)]

def checkSolution(question,number,answer):
	questionAnswer = question[1][number]
	if questionAnswer.lower() == answer.lower():
		return True
	return False

def informAnswer(question,number):
	space = "__"+str(number)+"___"
	return question[0].replace(space,q[1][number])

def play():
	salutation()
	explanation()
	level = difficulty()
	question = questions(level)
	print ("Alright, let's begin playing! The saying you need to guess is: ", 
		question[0])
	counter = 0
	mistakes = 0
	completed = False
	print ("Let's begin with word ",counter+1)
	
	while not completed or mistakes < 3:
		guess = raw_input("Go ahead! Make a guess: ")
		if checkSolution(question,counter,guess):
			print("Hurrah! that was right!")
			question[0]=informAnswer(question,counter)
			counter+=1
			if counter >= len(question[1]):
				completed = True
		else:
			mistakes += 1
			print("Sorry, that answer wasn't correct.")
			if mistakes < 3:
				print ("So far you have made ",mistakes," mistakes")
				print ("But you can still try again!")

	return completed

def game():
	keep_playing = True
	while keep_playing:
		completed = play()
		
		if completed:
			print ("Hurrah! You made it! Well done!!")
		else:
			print ("Sorry you couldn't make it. No worries, you can always keep playing!")

		validAnswer = False
		while not validAnswer:
			answer = raw_input("Do you want to play again? (Y/N): ")
			if answer.lower() == "n" or answer.lower() == "no": 
				validAnswer = True
				keep_playing = False
			elif answer.lower() == "y" or answer.lower() == "yes":
				validAnswer = True
			else:
				print ("I'm afraid that is not a valid answer.\nYou need to write Y for yes or N for no")
	print ("Thank you for playing! Hope you enjoyed it! :D")

game()
# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?
