import cmd
from ..utilities import Utilities
from datetime import datetime
from tabulate import tabulate
import os
import re
from ..initialization.initializer import Initializer

GREY = '\033[90m'         # Grey for unavailable seats
WHITE = '\033[97m'        # White for available seats
BLUE = '\033[34m'
RED = '\033[31m'          # Red for error messages
YELLOW = '\033[33m'       # Yellow for information messages
RESET = '\033[0m'         # Reset color
LIGHT_CYAN = "\033[1;36m"
GREEN = "\033[92m"

class MovieSystemCLI(cmd.Cmd):
    intro = f"{GREEN}Welcome to the Movie Reservation System! Type help or ? to list commands.{RESET}"
    prompt = (f"╭─{WHITE}developer@{LIGHT_CYAN}movie-reservation{RESET}\n╰─ {LIGHT_CYAN}~{RESET} ")

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

        if not movie_title:
            print(f"{YELLOW}Enter a movie title: reserve <movie_title>\nFeel free to type <list_movies> to search for movies to reserve{RESET}")
            return

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

        if seat_name not in selected_showtime.seat_details:
            print(f"{RED}You entered an invalid seat name.{RESET}")
            return
        elif seat_name in selected_showtime.booked_seats:
            print(f"{YELLOW}Cannot book {seat_name}, Already taken.")
            return

        # Step 6: Input email
        email = input(f"{BLUE}Enter your email: {RESET}").strip()

        if not self.is_valid_email(email):
            print(f"{RED}You entered an invalid email type.{RESET}")
            return

        user = self.user_service.get_user(email)
        if not user:
            print(f"{YELLOW}No account found for {email}. Creating a new account...{RESET}")
            user = self.user_service.register_user(email)
        # Step 7: Attempt reservation
        result = self.reservation_service.create_reservation(user.email, selected_showtime, seat_name)
        if type(result) == str:
            print(f"{GREY}Could not reserve the seat: {result}{RESET}")
        else:
            print(f"{GREEN}Seat {seat_name} reserved successfully for {movie_title} at {selected_showtime.showtime}.{RESET}")

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
            seen_movies = set()
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
        if not email:
            print(f"{YELLOW}Enter an email to view the reservations: view_reservations <email>{RESET}")
            return
        
        user = self.user_service.get_user(email)
        if not user:
            print(f"{RED}User with email '{email}' not found.{RESET}")
            return
        
        reservations = user.reservation_history
        if type(reservations) != str:
            reservation_iter = iter(reservations)
            print(f"{GREEN}Reservations for {email}:{RESET}")
            data = [["ID", "Movie", "Theatre", "Seat", "Showtime"]]
            for reservation in reservation_iter:
                movie_title = reservation.showtime.movie.title
                theatre_location = reservation.showtime.theatre.location
                showtime = reservation.showtime.showtime
                data.append([reservation.id, movie_title, theatre_location, reservation.seat_name, showtime])
            print(tabulate(data, headers="firstrow", tablefmt="grid"))
        else:
            print(f"{GREY}No reservations found for {email}.{RESET}")

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

    def is_valid_email(self, email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(email_regex, email))
