from random import randint

# This function says hello to the user and asks for his/her name
def salutation():	
	userName = input("\nHello friend! What is your name? ")
	print ("Hello ",userName,"\nWelcome to Sayings game!\n")
	explanation(userName)

# This function shows a brief explanation of how the game works
def explanation(userName):
	gameExplanation = """this game consists of the following:\n
You will be given a saying with blank spaces for you to fill in.
In order to win the game, you need to guess all blanks correctly!
You will have 3 attempts to complete each level. Good luck!\n"""
	print (userName,",", gameExplanation)

# This function enables the user to choose the level of difficulty
# and returns the level
def difficulty():
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

# This function returns a question corresponding to the chosen level of
# difficulty
def questions(level):
	easy = [["The ___1___ is always ___2___ on the ___3___ side of the ___4___.",["grass","greener","other","hill"]],
			["You can ___1___ a horse to ___2___, but you can't ___3___ him ___4___.",["lead","water","make","drink"]],
			["If you want ___1___ done ___2___, you ___3___ to do it ___4___.",["something","right","have","yourself"]]
			]
	
	medium = [["When the ___1___ gets ___2___, the ___2___ get ___1___.",["going","tough"]],
			["___1___ who live in ___2___ houses ___3___ not throw ___4___.",["People","glass","should","stones"]],
			["___1___ for the ___2___, but ___3___ for the ___4___.",["Hope","best","prepare","worst"]]
			]

	hard = [["A ___1___ is ___2___ a ___3___ ___4___.",["picture","worth","thousand","words"]],
			["Never ___1___ a gift ___2___ in ___3___ ___4___.",["look","horse","the","mouth"]],
			["You can't ___1___ an ___2___ without ___3___ a few ___4___.",["make","omelet","breaking","eggs"]]
			]

	questions = [easy, medium, hard]

	return questions[level][randint(0,2)]

# This function checks if a guess made by the user is right or not
# and returns True if it is right and False if it isn't
def checkSolution(question,number,answer):
	questionAnswer = question[1][number]
	if questionAnswer.lower() == answer.lower():
		return True
	return False

# This function modifies the question text to include the correct
# answer informed by the user and returns it.
def informAnswer(question,number):
	space = "___"+str(number+1)+"___"
	new_question = question[0].replace(space,question[1][number])
	print (new_question)
	return question[0].replace(space,question[1][number])

# This function enables the user to choose the amount of attempts
# for the game. It returns the amount of attempts indicated by the user.
def chooseAttempts():
	validAnswer = False
	while not validAnswer:
		attempts = input("How many attempts do you want to have?\n")
		if attempts.isdigit():
			validAnswer = True
		else:
			print ("\nSorry, your answer contains letters, it should only be numbers\n")
	return int(attempts)

# This function includes the main part of the game, prompting
# the user for answers and managing the user responses
# It returns True if the user has completed the game or False
# if the user commited too many mistakes.
def play():
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

# This function manages the beginning and ending of the game
def game():
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