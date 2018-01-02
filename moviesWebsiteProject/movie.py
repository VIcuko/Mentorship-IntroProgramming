import webbrowser

class Movie():
	""" This class provides a way to store a movie related information"""

	# This method initializes a Movie instance with the corresponding content saved as instance variables
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
