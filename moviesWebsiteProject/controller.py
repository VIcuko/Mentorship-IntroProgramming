import fresh_tomatoes
import movie

matrix = movie.Movie("The Matrix",
					 "Neo believes that Morpheus, an elusive figure considered to be the most dangerous man alive, can answer his question",
					 "https://images-na.ssl-images-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,665,1000_AL_.jpg",
					 "https://youtu.be/vKQi3bBA1y8")

forrest_gump = movie.Movie("Forrest Gump",
					 "The presidencies of Kennedy and Johnson, Vietnam, Watergate, and other history unfold through the perspective of an Alabama man with an IQ of 75.",
					 "https://images-na.ssl-images-amazon.com/images/M/MV5BNWIwODRlZTUtY2U3ZS00Yzg1LWJhNzYtMmZiYmEyNmU1NjMzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
					 "https://youtu.be/uPIEn0M8su0")

gladiator = movie.Movie("Gladiator",
					 "When a Roman General is betrayed, and his family murdered by an emperor's corrupt son, he comes to Rome as a gladiator to seek revenge.",
					 "https://images-na.ssl-images-amazon.com/images/M/MV5BMDliMmNhNDEtODUyOS00MjNlLTgxODEtN2U3NzIxMGVkZTA1L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
					 "https://youtu.be/owK1qxDselE")

indiana_jones_raiders = movie.Movie("Raiders of the Lost Ark",
					 "Archaeologist and adventurer Indiana Jones is hired by the U.S. government to find the Ark of the Covenant before the Nazis.",
					 "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA0ODEzMTc1Nl5BMl5BanBnXkFtZTcwODM2MjAxNA@@._V1_SY1000_CR0,0,664,1000_AL_.jpg",
					 "https://youtu.be/XkkzKHCx154")

good_will_hunting = movie.Movie("Good Will Hunting",
					 "Will Hunting, a janitor at M.I.T., has a gift for mathematics, but needs help from a psychologist to find direction in his life.",
					 "https://images-na.ssl-images-amazon.com/images/M/MV5BOTI0MzcxMTYtZDVkMy00NjY1LTgyMTYtZmUxN2M3NmQ2NWJhXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,655,1000_AL_.jpg",
					 "https://youtu.be/nH9LZOXBMUE")

star_wars_iv = movie.Movie("Star Wars: Episode IV - A New Hope",
					 "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a Wookiee and two droids to save the galaxy from the Empire's world-destroying battle-station while also attempting to rescue Princess Leia from the evil Darth Vader.",
					 "https://images-na.ssl-images-amazon.com/images/M/MV5BNzVlY2MwMjktM2E4OS00Y2Y3LWE3ZjctYzhkZGM3YzA1ZWM2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY1000_CR0,0,643,1000_AL_.jpg",
					 "https://youtu.be/vZ734NWnAHA")

movies = [matrix, forrest_gump, gladiator, indiana_jones_raiders, good_will_hunting, star_wars_iv]

fresh_tomatoes.open_movies_page(movies)