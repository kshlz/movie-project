import fresh_tomatoes
import media

drive = media.Movie("Drive",
                    "https://vignette.wikia.nocookie.net/hotline-miami/images/c/c6/Drive-movie-poster-2011-1010745541.jpg/revision/latest?cb=20161117200920",
                    "https://www.youtube.com/watch?v=KBiOF3y1W0Y")

the_godfather = media.Movie("The Godfather",
                            "https://i.pinimg.com/736x/a0/c0/50/a0c050d68a619f501fb3f3a44e4aeba8--the-godfather-movie-godfather-part-.jpg",
                            "https://www.youtube.com/watch?v=sY1S34973zA")

scarface = media.Movie("Scarface",
                       "https://mvpo.us/img/P4988.jpg",
                       "https://www.youtube.com/watch?v=7pQQHnqBa2E")

moonlight = media.Movie("Moonlight",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BNzQxNTIyODAxMV5BMl5BanBnXkFtZTgwNzQyMDA3OTE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                        "https://www.youtube.com/watch?v=9NJj12tJzqc")

belly = media.Movie("Belly",
                    "https://i.ytimg.com/vi/1m_m5AKYT-s/movieposter.jpg",
                    "https://www.youtube.com/watch?v=WDqPxUTbWnY")

requiem_for_a_dream = media.Movie("Requiem for a Dream",
                                  "https://images-na.ssl-images-amazon.com/images/I/81w-bqfpe1L._RI_.jpg",
                                  "https://www.youtube.com/watch?v=0nU7dC9bIDg")

movies = [drive, the_godfather, scarface, moonlight, belly, requiem_for_a_dream]
fresh_tomatoes.open_movies_page(movies)
