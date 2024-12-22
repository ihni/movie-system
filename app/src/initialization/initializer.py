from ..utilities.utilities import Utilities, COLOR
from datetime import datetime, timedelta
from time import sleep
import os

from ...config.config import ASCII_LOGO

import random

class Initializer:
    DUMMY_EMAILS = [
        "root@arc.org", "2023-2-01010@school.edu", "rupter.129@yahoo.com", "johnstone@dane.com",
        "emma.watson@example.com", "bruce.wayne@waynecorp.com", "peter.parker@dailybugle.net",
        "tony.stark@starkindustries.com", "diana.prince@amazon.com", "clark.kent@dailyplanet.com",
        "susan.storm@fantasticfour.org", "reed.richards@baxter.edu", "johnny.blaze@hellcycle.net",
        "steve.rogers@avengers.org", "natasha.romanoff@shield.gov", "sam.wilson@usaf.mil",
        "bucky.barnes@wintershield.org", "wanda.maximoff@magic.edu", "vision@synthezoid.net",
        "tchalla@wakanda.com", "shuri@wakandatech.org", "okoye@dora.mil",
        "scott.lang@quantum.net", "hope.vandyne@pymtech.com", "bruce.banner@avengers.org",
        "stephen.strange@sorcery.org", "peter.quill@guardians.galaxy", "gamora@guardians.galaxy",
        "rocket.raccoon@guardians.galaxy", "groot@guardians.galaxy", "drax@guardians.galaxy",
        "thor.odinson@asgard.com", "loki@asgard.com", "valkyrie@asgard.com",
        "carol.danvers@spaceforce.org", "nick.fury@shield.gov", "maria.hill@shield.gov",
        "phil.coulson@shield.gov", "may@shield.gov", "fitz@shield.gov",
        "simmons@shield.gov", "quake@shield.gov", "mockingbird@shield.gov",
        "elektra@thehand.com", "matt.murdock@hellskitchen.org", "jessica.jones@aliasinvestigations.com",
        "luke.cage@harlemhero.net", "danny.rand@kunlun.org", "frank.castle@punisher.com"
    ]
    DUMMY_THEATRES = {
        "Raspberry": [7, 5],
        "Mango": [5, 10],
        "Pineapple": [10, 15],
        "Blueberry": [8, 8]
    }
    DUMMY_MOVIES = {
        "Pirates of the Caribbean": 128,
        "Transformers": 127,
        "Moana": 78,
        "The Dark Knight": 152,
        "Avengers: Endgame": 181,
        "Frozen": 102,
        "Interstellar": 169,
        "Inception": 148,
        "Coco": 105,
        "The Lion King": 118
    }

    def __init__(self, theatre_service, reservation_service, user_service, showtime_service):
        self.theatre_service = theatre_service
        self.reservation_service = reservation_service
        self.user_service = user_service
        self.showtime_service = showtime_service
        self.utilities = Utilities()

    def initialize_users(self):
        print(f"{COLOR['CYAN']}[ INITIALIZING USERS ]{COLOR['ENDC']} Initializing users...")
        for email in Initializer.DUMMY_EMAILS:
            self.user_service.register_user(email)
            print(f"Created user with email: {email}")
            sleep(0.01)

        total_users = len(self.user_service.get_users())
        if total_users == len(Initializer.DUMMY_EMAILS):
            print(f"{COLOR['GREEN']}[ SUCCESS ] Users initialized successfully! Total: {total_users}{COLOR['ENDC']}")
            return 0
        else:
            print(f"{COLOR['RED']}[ ERROR ] User initialization mismatch!{COLOR['ENDC']}")
            return -1

    def initialize_theatres(self):
        print(f"{COLOR['CYAN']}[ INITIALIZING THEATRES ]{COLOR['ENDC']} Initializing theatres...")
        for location, dimensions in Initializer.DUMMY_THEATRES.items():
            theatre = self.theatre_service.create_theatre(
                location=location,
                total_rows=dimensions[0],
                total_columns=dimensions[1]
            )
            print(f"Created theatre: {theatre}")
            sleep(0.01)

        total_theatres = len(self.theatre_service.get_theatres())
        if total_theatres == len(Initializer.DUMMY_THEATRES):
            print(f"{COLOR['GREEN']}[ SUCCESS ] Theatres initialized successfully! Total: {total_theatres}{COLOR['ENDC']}")
            return 0
        else:
            print(f"{COLOR['RED']}[ ERROR ] Theatre initialization mismatch!{COLOR['ENDC']}")
            return -1

    def initialize_movies(self):
        print(f"{COLOR['CYAN']}[ INITIALIZING MOVIES ]{COLOR['ENDC']} Initializing movies...")
        for title, duration in Initializer.DUMMY_MOVIES.items():
            movie = self.theatre_service.create_movie(
                title=title,
                duration=duration
            )
            print(f"Created movie: {movie}")
            sleep(0.01)

        total_movies = len(self.theatre_service.get_movies())
        if total_movies == len(Initializer.DUMMY_MOVIES):
            print(f"{COLOR['GREEN']}[ SUCCESS ] Movies initialized successfully! Total: {total_movies}{COLOR['ENDC']}")
            return 0
        else:
            print(f"{COLOR['RED']}[ ERROR ] Movie initialization mismatch!{COLOR['ENDC']}")
            return -1

    def initialize_showtimes(self):
        print(f"{COLOR['CYAN']}[ INITIALIZING SHOWTIMES ]{COLOR['ENDC']} Initializing showtimes...")
        movies = self.theatre_service.get_movies()
        theatres = self.theatre_service.get_theatres()
        base_time = datetime.now()

        for i, movie in enumerate(movies):
            showtime_time = base_time + timedelta(hours=i * 2)
            theatre = theatres[i % len(theatres)]
            result = self.showtime_service.create_showtime(
                movie=movie,
                theatre=theatre,
                showtime=showtime_time
            )
            if isinstance(result, str):
                print(f"{COLOR['RED']}[ ERROR ] Error creating showtime for {movie}: {result}{COLOR['ENDC']}")
            else:
                print(f"Created showtime: {result}")
            sleep(0.01)

        total_showtimes = len(self.showtime_service.get_showtimes())
        if total_showtimes == len(Initializer.DUMMY_MOVIES):
            print(f"{COLOR['GREEN']}[ SUCCESS ] Showtimes initialized successfully! Total: {total_showtimes}{COLOR['ENDC']}")
            return 0
        else:
            print(f"{COLOR['RED']}[ ERROR ] Showtime initialization mismatch!{COLOR['ENDC']}")
            return -1

    def initialize_reservations(self):
        print(f"{COLOR['CYAN']}[ INITIALIZING RESERVATIONS ]{COLOR['ENDC']} Initializing reservations...")
        users = self.user_service.get_users()
        showtimes = self.showtime_service.get_showtimes()
        theatres = self.theatre_service.get_theatres()

        for user in users:
            random_showtime = random.choice(showtimes)
            theatre = random_showtime.theatre
            rows, cols = theatre.total_rows, theatre.total_columns

            # Generate a random seat within bounds
            row = chr(random.randint(65, 65 + rows - 1))  # A to max row
            col = random.randint(1, cols)  # 1 to max column
            seat_name = f"{row}{col}"

            self.reservation_service.create_reservation(
                email=user.email,
                showtime=random_showtime,
                seat_name=seat_name
            )
            print(f"Created reservation for {user.email}: {seat_name} at {random_showtime}")
            sleep(0.01)

        print(f"{COLOR['GREEN']}[ SUCCESS ] Reservations initialized successfully!{COLOR['ENDC']}")
        return 0

    def welcome(self):
        colored_logo = self.utilities.rainbow_text(ASCII_LOGO)
        print(colored_logo)
        print(f"Welcome to the {COLOR['ORANGE']}Movie Ticket Booking System{COLOR['ENDC']}")
        print("• Explore movies and theatres in a simulated environment.")
        print(f"• Please note: {COLOR['YELLOW']}Data is not saved in this demo{COLOR['ENDC']}.")
        input(f"{COLOR['CYAN']}Press Enter to continue...{COLOR['ENDC']}")
        self.utilities.clear()

    def init(self):
        result = [
            self.initialize_users(),
            self.initialize_theatres(),
            self.initialize_movies(),
            self.initialize_showtimes(),
            self.initialize_reservations()
        ]

        if any(r < 0 for r in result):
            print(f"{COLOR['RED']}Initialization failed. Would you like to retry? (y/n){COLOR['ENDC']}")
            if input().lower() == 'y':
                self.init()
            else:
                exit()
        else:
            print(f"{COLOR['GREEN']}Initialization successful! Booting up...{COLOR['ENDC']}")
            sleep(0.5)
            self.utilities.clear()
            self.welcome()