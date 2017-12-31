import urllib.request as ulib

def read_text():
	quotes = open ("./movie_quotes.txt")
	file_content = quotes.read()
	print (file_content)
	quotes.close()
	check_profanity(file_content)

def check_profanity(text_to_check):
	connection = ulib.urlopen("http://www.wdylike.appspot.com/?q="+"text")
	output = connection.read()
	print(output)
	connection.close()

read_text()
