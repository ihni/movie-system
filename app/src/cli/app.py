import cmd
from ..utilities import Utilities
from datetime import datetime
import os
from ..initialization.initializer import Initializer

GREY = '\033[90m'         # Grey for unavailable seats
WHITE = '\033[97m'        # White for available seats
GREEN = '\033[32m'        # Green for success messages and reserved seat
BLUE = '\033[34m'         # Blue for prompts
RED = '\033[31m'          # Red for error messages
YELLOW = '\033[33m'       # Yellow for information messages
RESET = '\033[0m'         # Reset color

class MovieSystemCLI(cmd.Cmd):
    intro = f"{GREEN}Welcome to the Movie Reservation System! Type help or ? to list commands.{RESET}"
    prompt = f"{BLUE}(movie-reservation) > {RESET}"

    def __init__(self, theatre_service, reservation_service, user_service, showtime_service):
        super().__init__()
        self.theatre_service = theatre_service
        self.reservation_service = reservation_service
        self.user_service = user_service
        self.showtime_service = showtime_service
        self.utilities = Utilities()
        self.initializer = Initializer(theatre_service, reservation_service, user_service, showtime_service)
        self.initializer.init()

    def do_reserve(self, arg):
        """
        Reserve a seat for a movie: reserve <movie_title>
        """
        movie_title = arg.strip()

        # Step 1: Find the movie showtimes (not the movie directly)
        showtimes = self.showtime_service.get_showtimes_by_movie_title(movie_title)
        if not showtimes:
            print(f"{RED}Movie '{movie_title}' not found.{RESET}")
            return

        # Step 2: Show available showtimes for the movie
        print(f"{GREEN}Available showtimes for {movie_title}:{RESET}")
        for idx, showtime in enumerate(showtimes, start=1):
            print(f"{idx}. {showtime.showtime} - Theatre: {showtime.theatre.location}")

        # Step 3: Showtime selection
        try:
            choice = int(input(f"{BLUE}Select a showtime (enter number): {RESET}"))
            selected_showtime = showtimes[choice - 1]
        except (IndexError, ValueError):
            print(f"{RED}Invalid showtime selection.{RESET}")
            return

        # Step 4: Display seat matrix for the selected showtime
        self._display_seat_matrix(selected_showtime)

        # Step 5: Input seat name
        seat_name = input(f"{BLUE}Enter seat name (e.g., A4): {RESET}").strip()

        # Step 6: Input email
        email = input(f"{BLUE}Enter your email: {RESET}").strip()
        user = self.user_service.find_user_by_email(email)
        if not user:
            print(f"{YELLOW}No account found for {email}. Creating a new account...{RESET}")
            user = self.user_service.create_user(email)

        # Step 7: Attempt reservation
        if self.reservation_service.is_seat_available(selected_showtime, seat_name):
            self.reservation_service.create_reservation(selected_showtime.movie, selected_showtime, seat_name, user)
            print(f"{GREEN}Seat {seat_name} reserved successfully for {movie_title} at {selected_showtime.time}.{RESET}")
        else:
            print(f"{GREY}Seat {seat_name} is already reserved.{RESET}")

    def do_list_movies(self, arg):
        """
        List all available movies alphabetically or by showtime.
        """
        sort_by = arg.strip().lower() or 'alphabetically'
        showtimes = []

        if sort_by == 'alphabetically':
            showtimes = self.showtime_service.get_showtimes_alphabetically()
        elif sort_by == 'showtime':
            showtimes = self.showtime_service.get_showtimes_showtime_latest()
        else:
            print(f"{RED}Invalid option. Please choose 'alphabetically' or 'showtime'.{RESET}")
            return

        if showtimes:
            print(f"{GREEN}Available Movies ({sort_by}):{RESET}")
            seen_movies = set()  # To avoid printing duplicate movie titles
            for showtime in showtimes:
                movie_title = showtime.movie.title
                if movie_title not in seen_movies:
                    seen_movies.add(movie_title)
                    print(f"- {movie_title} ({showtime.movie.duration} min)")
        else:
            print(f"{RED}No movies available.{RESET}")

    def do_view_reservations(self, arg):
        """
        View all reservations for a specific email: view_reservations <email>
        """
        email = arg.strip()
        user = self.user_service.find_user_by_email(email)
        if user:
            reservations = self.reservation_service.get_reservations_for_user(user)
            if reservations:
                print(f"{GREEN}Reservations for {email}:{RESET}")
                for idx, reservation in enumerate(reservations, start=1):
                    print(f"{idx}. Movie: {reservation.movie.title}, Theatre: {reservation.showtime.theatre.location}, Showtime: {reservation.showtime.time}, Seat: {reservation.seat_name}")
            else:
                print(f"{GREY}No reservations found for {email}.{RESET}")
        else:
            print(f"{RED}User with email '{email}' not found.{RESET}")

    def do_exit(self, arg):
        """
        Exit the movie reservation system.
        """
        print(f"{GREEN}Thank you for using the Movie Reservation System!{RESET}")
        return True

    def _display_seat_matrix(self, showtime):
        """
        Display the seat matrix for a showtime.
        """
        seat_matrix = showtime.get_seat_matrix()
        print(f"{GREEN}Available Seats:{RESET}")
        for row in seat_matrix:
            row_display = ' '.join(
                f"{WHITE}{seat.name}{RESET}" if seat.is_available else f"{GREY}{seat.name}{RESET}"
                for seat in row
            )
            print(row_display)
