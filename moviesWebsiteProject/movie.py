
import webbrowser

class Movie():
	""" This class provides a way to store a movie related information"""

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		"""
		Initialize the movie instance.
		Arguments:
		movie_title: title of the movie
		movie_storyline: brief description of the movie
		poster_image: image of the movie poster
		trailer_youtube: youtube trailer url
		…
		Returns: 
		None
		"""
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
