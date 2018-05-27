from classes.movies_pb2 import MovieList, Movie
from datetime import datetime

movie_list = MovieList()
movie_list.ParseFromString(b'\n\xb7\x01\n\x08Deadpool\x118\xf5\xe9\x0fu\xc2\xd6A\x1alWisecracking mercenary Deadpool battles the evil and powerful Cable and other bad guys to save a boy\'s life."\x11\n\rRyan Reynolds\x10\x00"\x10\n\x0cDavid Leitch\x10\x02"\x0f\n\x0bRhett Reese\x10\x01')

for movie in movie_list.movies:
    print("Movie name:",movie.name)
    print("Release date:", datetime.fromtimestamp(movie.releaseDate))
    print("Overview:", movie.overview)
    print("Featured Crew:")
    for person in movie.featuredCrew:
        print("  Name:",person.name)
        if person.role == Movie.CHARACTER:
            print("  Role: Character")
        if person.role == Movie.SCREENPLAY:
            print("  Role: Screenplay")
        if person.role == Movie.DIRECTOR:
            print("  Role: Director")         