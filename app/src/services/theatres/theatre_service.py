from ...models import Theatre
from ...models import Movie

class TheatreService:
    def __init__(self):
        self.theatres = {}
        self.movies = {}
    def create_theatre(self, location: str, total_rows: int, total_columns: int) -> Theatre:
        if location in self.theatres:
            return "Duplicate theatre found"
        
        theatre = Theatre(location, total_rows, total_columns)
        self.theatres[theatre.location] = theatre    
        return theatre
    
    def create_movie(self, title: str, duration: int) -> Movie:
        '''
        Movies with the same title is allowed to be added
        '''
        movie = Movie(title, duration)

        if movie in self.movies.values():
            return "Duplicate movie found"
        self.movies[movie.title] = movie
        return movie
    
    def get_movies(self):
        return list(self.movies.values())
    
    def get_theatres(self):
        return list(self.theatres.values())