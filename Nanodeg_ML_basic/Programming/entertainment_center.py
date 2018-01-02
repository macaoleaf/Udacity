import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikimedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

engineering_failure = media.Movie("engineering_failure",
                                  "The worst test",
                                  "whatever",
                                  "https://www.youtube.com/watch?v=ro3EPPYbn44")
print(toy_story.storyline)
movies = [toy_story, engineering_failure]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
