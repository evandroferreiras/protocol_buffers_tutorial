from classes.movies_pb2 import MovieList, Movie
from datetime import datetime

movie_json = {
    "name" : "Deadpool",
    "releaseDate" : datetime.now().timestamp(),
    "overview" : "Wisecracking mercenary Deadpool battles the evil and powerful Cable and other bad guys to save a boy's life.",
    "featuredCrew" : [
        {
            "name" : "Ryan Reynolds",
            "role" : "character"
        },
        {
            "name" : "David Leitch",
            "role" : "director"
        },
        {
            "name" : "Rhett Reese",
            "role" : "screenplay"
        }                
    ]
}

movie_list = MovieList()
movie = movie_list.movies.add()
movie.name = movie_json["name"]
movie.overview = movie_json["overview"]
movie.releaseDate = movie_json["releaseDate"]

for person_json in movie_json["featuredCrew"]:
    
    person = movie.featuredCrew.add()
    person.name = person_json["name"]
    if person_json["role"] == "character":
        person.role = Movie.CHARACTER
    if person_json["role"] == "screenplay":
        person.role = Movie.SCREENPLAY
    if person_json["role"] == "director":
        person.role = Movie.DIRECTOR

print(movie_list.SerializeToString())