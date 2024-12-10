from app.src.services import (
    ShowtimeService,
    UserService,
    ReservationService,
    TheatreService,
)

from app.src.models import (
    Movie,
)

from app.src.utilities.utilities import Utilities
from datetime import datetime

class Test:

    DUMMY_EMAILS = [
        "root@arc.org", "2023-2-01010@school.edu", "rupter.129@yahoo.com", "johnstone@dane.com"
    ]

    DUMMY_THEATRES = {
        "Raspberry" : [rows := 7,  columns := 5],
        "Mango" : [rows := 5, columns := 10],
    }

    DUMMY_MOVIES = {
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
        self.user_service.register(email for email in Test.DUMMY_EMAILS)
        
        if len(self.user_service.get_users()) == len(Test.DUMMY_EMAILS):
            print("Finished initializing users!")
            return 0
        else:
            print("An error occured with the user initialization process")
            return -1
        
    def initialize_theatres(self):
        print("Initializing theatres...")
        for key, value in Test.DUMMY_THEATRE_LOCATIONS.items():
            theatre = self.theatre_service.create_theatre(
                location = key,
                total_rows = value[0],
                total_columns = value[2]
            )
            print(f"Created theatre: {theatre}")
        
        if len(self.theatre_service.get_theatres()) == len(Test.DUMMY_THEATRES):
            print("Finished initializing theatres")
            return 0
        else:
            print("An error occured with the theatre initialization process")

    def initialize_dummy_data(self):
        raspi_theatre = Theatre(
            location="1",
            total_rows= 10,
            total_columns= 5
        )

        pirates_movie = Movie("Pirates of the Caribbean", 128)
        
        self.showtime_service.create_showtime(
            movie = pirates_movie,
            theatre = raspi_theatre,
            showtime = datetime.now()
        )

        self.user_service.register_user("demo@demo.org")

        result = self.reservation_service.create_reservation(
            email = "demo@demo.org",
            showtime = self.showtime_service.get_showtime_by_id(1),
            seat_name = "A4",
        )

        self.utilities.display_seats_for_showtime(
            self.showtime_service.get_showtime_by_id(1)
        )

        if type(result) == str:
            return result
        else:
            return "Successfully registered"


test = Test()

test.initialize_dummy_data()