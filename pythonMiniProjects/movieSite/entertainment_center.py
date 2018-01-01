import media

toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life",
						"https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
						"https://youtu.be/KYz2wyBy3kc")

avatar = media.Movie("Avatar",
					 "A marine on an alien plantet",
					 "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
					 "https://youtu.be/5PSNL1qE6VY")

matrix = media.Movie("The Matrix",
					 "Neo believes that Morpheus, an elusive figure considered to be the most dangerous man alive, can answer his question",
					 "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
					 "https://youtu.be/vKQi3bBA1y8")

print (toy_story.storyline)
print (avatar.storyline)

avatar.show_trailer()
print (matrix.storyline)
matrix.show_trailer()
