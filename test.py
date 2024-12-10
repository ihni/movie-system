'''
Currently combining the initialization of demo data and the first concepts of the CLi
'''

from app.src.services import (
    ShowtimeService,
    UserService,
    ReservationService,
    TheatreService,
)

from app.src.models import (
    Movie,
)

from app.src.utilities.utilities import Utilities, COLOR
from datetime import datetime
from time import sleep
import os

from app.config.config import ASCII_LOGO

class Test:

    DUMMY_EMAILS = [
        "root@arc.org", "2023-2-01010@school.edu", "rupter.129@yahoo.com", "johnstone@dane.com"
    ]

    DUMMY_THEATRES = {
        "Raspberry" : [rows := 7,  columns := 5],
        "Mango" : [rows := 5, columns := 10],
    }

    DUMMY_MOVIES = {    # key is the title and value is the duration in minutes
        "Pirates of the Caribbean" : 128,
        "Transformers 1" : 127,
        "Moana 2" : 78
    }

    def __init__(self):
        self.user_service = UserService()
        self.showtime_service = ShowtimeService()
        self.reservation_service = ReservationService(self.user_service)
        self.theatre_service = TheatreService()
        self.utilities = Utilities()

    def initialize_users(self):
        print("Initializing users...")
        for email in Test.DUMMY_EMAILS:
            self.user_service.register_user(email)
        
        if len(self.user_service.get_users()) == len(Test.DUMMY_EMAILS):
            print(f"{COLOR['GREEN']}Finished initializing users!{COLOR['ENDC']}")
            return 0
        else:
            print(f"{COLOR['RED']}An error occured with the user initialization process{COLOR['ENDC']}")
            return -1
        
    def initialize_theatres(self):
        print("Initializing theatres...")
        for key, value in Test.DUMMY_THEATRES.items():
            theatre = self.theatre_service.create_theatre(
                location = key,
                total_rows = value[0],
                total_columns = value[1]
            )
            print(f"Created theatre: {theatre}")
        
        if len(self.theatre_service.get_theatres()) == len(Test.DUMMY_THEATRES):
            print(f"{COLOR['GREEN']}Finished initializing theatres{COLOR['ENDC']}")
            return 0
        else:
            print(f"{COLOR['RED']}An error occured with the theatre initialization process{COLOR['ENDC']}")
            return -1

    def initialize_movies(self):
        print("Initializing movies ...")
        for key, value in Test.DUMMY_MOVIES.items():
            movie = self.theatre_service.create_movie(
                title = key,
                duration = value
            )
            print(f"Created movie: {movie}")

        if len(self.theatre_service.get_movies()) == len(Test.DUMMY_MOVIES):
            print(f"{COLOR['GREEN']}Finished initializing movies{COLOR['ENDC']}")
            return 0
        else:
            print(f"{COLOR['RED']}An error occured with the theatre initialization process{COLOR['ENDC']}")
            return -1
        
    def initialize_showtimes(self):
        movies: list = self.theatre_service.get_movies()
        theatres: list = self.theatre_service.get_theatres()

        print("Initializing showtimes...")
        for movie in movies:
            result = self.showtime_service.create_showtime(
                movie = movie,
                theatre = theatres[0],
                showtime = datetime.now()
            )
            if type(result) == str:
                print(f"{COLOR['RED']}Error creating showtime for Movie: {movie}{COLOR['ENDC']}")
            else:    
                print(f"Created showtime: {result}")
        
        if len(self.showtime_service.get_showtimes()) == len(Test.DUMMY_MOVIES):
            print(f"{COLOR['GREEN']}Finished showtime initialization{COLOR['ENDC']}")
            return 0
        else:
            print(f"{COLOR['RED']}An error occured with the showtime initialization process{COLOR['ENDC']}")
            return -1
        
    def initialize_reservations(self):
        print("Initializing reservations...")
        users = self.user_service.get_users()

        for i, user in enumerate(users):
            self.reservation_service.create_reservation(
                email = user.email,
                showtime = self.showtime_service.get_showtime_by_id(1),
                seat_name = f"A{i+2}"
            )
        print(f"{COLOR['GREEN']}Finished initializing reservations{COLOR['ENDC']}")
        return 0
    
    def welcome(self):
        colored_logo = self.utilities.rainbow_text(ASCII_LOGO)
        print(colored_logo)
        print(f"Welcome to the {COLOR['ORANGE']}Movie Ticket Booking System{COLOR['ENDC']} created for the DSA Finals Project")
        input()
        
    def init(self):
        result = []

        result.append(self.initialize_users())
        sleep(0.1)
        result.append(self.initialize_theatres())
        sleep(0.1)
        result.append(self.initialize_movies())
        sleep(0.1)
        result.append(self.initialize_showtimes())
        sleep(0.1)
        result.append(self.initialize_reservations())

        if sum(result) < 0:
            print(f"{COLOR['RED']}An error occured in the initialization process{COLOR['ENDC']}")
            reinit = input(f"{COLOR['YELLOW']}Would you like to reinitialize? (y/n) > {COLOR['ENDC']}")
            if reinit.lower == 'y':
                self.init()
            else:
                exit()
        else:
            sleep(0.1)
            print(f"{COLOR['GREEN']}The initialization process was successful{COLOR['ENDC']}")
            print(f"Booting up the program...")
            sleep(0.4)
            os.system('cls')
            self.welcome()
        

test = Test()

test.init()