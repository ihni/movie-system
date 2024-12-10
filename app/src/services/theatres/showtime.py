from ...models import Showtime
from ...library import MergeSort, BinarySearch

class ShowtimeService:
    def __init__(self):
        self.showtimes = {}
        self.id = 1
        self.sort_function = MergeSort().merge_sort
        self.search_function = BinarySearch().search

    def create_showtime(self, movie: object, theatre: object, showtime: object) -> Showtime:
        """
        Creates a showtime for a movie at a movie including its showtime(datetime object)
        and stores it inside the showtimes dictionary

        :param movie: Movie object
        :param theatre: Theatre object
        :param showtime: Datetime object
        :return Showtime object
        """
        showtime = Showtime(
            movie = movie,
            theatre = theatre,
            showtime = showtime
        )
        self.showtimes[self.id] = showtime
        self.id += 1
        return showtime
    
    def delete_showtime(self, showtime_id: int):
        result = self.showtimes[showtime_id].get()

        if result:
            del self.showtimes[showtime_id]
            return "Successfully deleted the showtime"
        return "Could not delete the showtime"

    def search_movie_title(self, search: str) -> object:
        movie_titles = []
        title_to_movie = {}
        showtimes = self.get_showtimes_alphabetically()
        for showtime in showtimes:
            movie = showtime.movie
            movie_titles.append(movie.title)
            title_to_movie[movie.title] = movie

        result, _ = self.search_function(movie_titles, search)
        if result:
            return title_to_movie[result]
        return "Could not find movie"

    def get_showtimes_alphabetically(self) -> list:
        '''
        Creates a dictionary to store the title of the movie with the showtime object
        Then stores all movie titles(which are unsorted) in an array, then pass it to merge sort
        With a sorted array of movie titles, It's mapped back to its showtime and appeneded to another list
        '''
        title_to_showtime = {}
        unsorted_movie_titles = []
        for showtime in self.showtimes.values():
            movie_title = showtime.movie.title
            title_to_showtime[movie_title] = showtime
            unsorted_movie_titles.append(movie_title)

        sorted_movie_titles = self.sort_function(unsorted_movie_titles)

        sorted_showtimes_alphabetically = []
        for sorted_title in sorted_movie_titles:
            sorted_showtimes_alphabetically.append(title_to_showtime[sorted_title])
        
        return sorted_showtimes_alphabetically

    def get_showtimes_showtime_latest(self):
        datetime_to_showtime = {}
        unsorted_datetimes = []
        for showtime in self.showtimes.values():
            datetime = showtime.showtime
            datetime_to_showtime[datetime] = showtime
            unsorted_datetimes.append(datetime)

        sorted_datetimes = self.sort_function(unsorted_datetimes)

        sorted_datetimes = []
        for sorted_datetime in sorted_datetimes:
            sorted_datetimes.append(datetime_to_showtime[sorted_datetime])
        
        return sorted_datetimes

    def get_showtimes(self):
        return list(self.showtimes.values())
        