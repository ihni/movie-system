class Showtime:
    def __init__(self, movie: object, theatre: object, showtime: object):
        """
        Initialize the Showtime object.
        
        :param movie: Movie object
        :param theatre: Theatre object
        :param showtime: Datetime object when the movie is shown
        """
        self.movie:      object = movie
        self.theatre:    object = theatre
        self.showtime:   object = showtime # **this is an object from the datetime class**
        self.booked_seats:  set = set()
        self.seat_details: dict = {}

        for row in self.theatre.seats:
            for seat in row:
                self.seat_details[seat.name] = {
                    "is_available": True,
                    "seat_obj": seat
                }


    def is_fully_booked(self) -> bool:
        return len(self.booked_seats) >= self.theatre.total_seats
    
    def check_seat_availability(self, seat_name: str) -> str:
        """
        Checks the availability of a specific seat in the theatre.

        :param seat_name: The name of the seat (e.g., 'A1')
        :return: Availability status message
        """

        if seat_name not in self.seat_details:
            return "This seat does not exist"

        seat_info: object = self.seat_details[seat_name]

        return "This is seat is available" if seat_info["is_available"] else "This seat is not available"

    def reserve_seat(self, seat_name: str) -> str:
        """
        Reserves a specific seat for a customer if it's available.

        :param seat_name: The name of the seat (e.g., 'A1')
        :return: Booking status message
        """
        if seat_name not in self.seat_details:
            return "This seat does not exist"
        
        if seat_name in self.booked_seats:
            return "This seat is already booked"
        
        seat_info = self.seat_details[seat_name]

        if seat_info['is_available']:
            seat_info['seat_obj'].reserve()
            self.booked_seats.add(seat_name)
            seat_info['is_available'] = False
            return "Seat has been booked"
        else:
            return "This seat is already booked"
    
    def release_seat(self, seat_name: str) -> str:
        """
        Releases a previously booked seat.

        :param seat_name: The name of the seat (e.g., 'A1')
        :return: Release status message
        """
        if seat_name not in self.seat_details:
            return "Seat does not exist"
        
        if seat_name not in self.booked_seats:
            return "Cannot release seat, it is not booked"
        
        self.booked_seats.remove(seat_name)

        seat_info: object = self.seat_details[seat_name]
        seat_info["seat_obj"].release()
        seat_info["is_available"] = True
        return "This seat has been released"
    
    '''
    '
    '   Getters
    '   get_movie() -> returns the movie of the showtime  
    '   get_theatre() -> returns the theatre that the showtime belongs to
    '   get_seating_matrix () -> returns a matrix of seat objects according to the theatre seating configuration
    '   get_showtime_info() -> returns a dictionary of info
    '                       - movie, showtime, total_seats, booked_seats, available_seats, is_fully_booked, status, movie_duration
    '
    '''

    def get_movie(self) -> object:
        return self.movie
    
    def get_theatre(self) -> object:
        return self.theatre

    def get_showtime_info(self) -> dict:
        booked_seats = len(self.booked_seats)
        available_seats = self.theatre.total_seats - booked_seats
        return {
            'movie'           : self.movie.title,
            'showtime'        : self.showtime.strftime("%Y-%m-%d %H:%M:%S"),
            'total_seats'     : self.theatre.total_seats,
            'booked_seats'    : booked_seats,
            'available_seats' : available_seats,
            'movie_duration'  : self.movie.duration_in_minutes,
            'status'          : "Fully booked" if self.is_fully_booked() else "{available_seats} available seats",
            'is_fully_booked' : self.is_fully_booked(),
        }
    
    def get_seating_matrix(self) -> list[list]:
        seats = []
        seating_matrix = []
        
        for key, _ in self.seat_details.items():
           seat = self.seat_details[key]["seat_obj"]
           seats.append(seat) # this is appending the seat object from the value list
        rows = self.theatre.total_rows
        columns = self.theatre.total_columns

        counter = 0
        for _ in range(rows):
            seat_row = []
            for _ in range(columns):
                if counter > len(seats)-1:
                    return "Error, Overflow of seats"
                seat_row.append(seats[counter])
                counter += 1
            seating_matrix.append(seat_row)
        return seating_matrix

    def display_for_user(self):
        return (
            f"Showtime for {self.movie.title} at {self.showtime.strftime('%Y-%m-%d %H:%M:%S')}"
        )

    def __str__(self):
        booked = len(self.booked_seats)
        available = self.theatre.total_seats - booked
        return (f"Showtime for {self.movie.title} at {self.showtime.strftime('%Y-%m-%d %H:%M:%S')} "
                f"({available} available seats, {booked} booked seats)")