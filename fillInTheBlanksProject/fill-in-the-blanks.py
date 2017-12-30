from random import randint

def salutation():
	# This function says hello to the user and asks for his/her name
	userName = input("\nHello friend! What is your name? ")
	print ("Hello ",userName,"\nWelcome to Sayings game!\n")
	explanation(userName)

def explanation(userName):
	# This function shows a brief explanation of how the game works
	gameExplanation = """this game consists of the following:\n
You will be given a saying with blank spaces for you to fill in.
In order to win the game, you need to guess all blanks correctly!
You will have 3 attempts to complete each level. Good luck!\n"""
	print (userName,",", gameExplanation)

def difficulty():
	# This function enables the user to choose the level of difficulty
	# and returns the level
	informed = False
	level=-1
	while level < 0:
		selectionMessage = "Please choose the difficulty level from the following: easy / medium / hard: "
		text = input(selectionMessage)
		if text.lower() == "easy":
			print ("\nOk! You chose easy!\n")
			level = 0
		elif text.lower() == "medium":
			print ("\nOk! You chose medium!\n")
			level = 1
		elif text.lower() == "hard":
			print ("\nOk! You chose hard!\n")
			level = 2
		else:
			print ("\nSorry, ",text," is not one of the options.\n")
	return level

def questions(level):
	# This function returns a question corresponding to the chosen level of
	# difficulty
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
	# This function checks if a guess made by the user is right or not
	# and returns True if it is right and False if it isn't
	questionAnswer = question[1][number]
	if questionAnswer.lower() == answer.lower():
		return True
	return False

def informAnswer(question,number):
	# This function modifies the question text to include the correct
	# answer informed by the user and returns it.
	space = "__"+str(number)+"___"
	return question[0].replace(space,question[1][number])

def chooseAttempts():
	# This function enables the user to choose the amount of attempts
	# for the game. It returns the amount of attempts indicated by the user.
	attempts = input("How many attempts do you want to have?\n")
	return int(attempts)

def play():
	# This function includes the main part of the game, prompting
	# the user for answers and managing the user responses
	# It returns True if the user has completed the game or False
	# if the user commited too many mistakes.
	level = difficulty()
	question = questions(level)
	counter, mistakes, attempts = 0, 0, chooseAttempts()
	print ("\nAlright, let's begin playing! The saying you need to guess is:\n", question[0],"\n\nLet's begin with word ",counter+1)
	while not counter >= len(question[1]) and mistakes < attempts:
		guess = input("Go ahead! Make a guess: ")
		if checkSolution(question,counter,guess):
			print("\nHurrah! that was right!")
			question[0] = informAnswer(question,counter)
			counter += 1
			if counter < len(question[1]):
				print ("\nLet's continue with word ",counter+1)
		else:
			mistakes += 1
			print("\nThat answer wasn't correct.")
			if mistakes < attempts:
				print ("So far you have made ",mistakes," mistakes.\nBut you can still try again!\n")
	return counter >= len(question[1])

def game():
	# This function manages the beginning and ending of the game
	salutation()
	keep_playing = True
	while keep_playing:
		completed = play()
		if completed:
			print ("\nYou made it! Well done!!")
		else:
			print ("\nSorry you couldn't make it. No worries, you can always keep playing!")
		validAnswer = False
		while not validAnswer:
			answer = input("\nDo you want to play again? (Y/N): ")
			if answer.lower() == "n" or answer.lower() == "no": 
				validAnswer, keep_playing = True, False
			elif answer.lower() == "y" or answer.lower() == "yes":
				validAnswer = True
			else:
				print ("I'm afraid that is not a valid answer.\nYou need to write Y for yes or N for no")
	print ("\nThank you for playing! Hope you enjoyed it! :D")

game()