import fresh_tomatoes
import media

matrix = media.Movie("The Matrix",
					 "Neo believes that Morpheus, an elusive figure considered to be the most dangerous man alive, can answer his question",
					 "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
					 "https://youtu.be/vKQi3bBA1y8")

movies = [toy_story,avatar,matrix]

# Print the class documentation string:
print (media.Movie.__doc__)

# Print the name of the class:
print (media.Movie.__name__)

# Print the name of the module in which this class was defined:
print (media.Movie.__module__)