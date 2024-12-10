from app.src.services import (
    ShowtimeService,
    UserService,
    ReservationService
)

from app.src.models import (
    Movie,
    Theatre,
)

from app.src.utilities.utilities import Utilities
from datetime import datetime

''' Initializing Service '''
user_service = UserService()
showtime_service = ShowtimeService()
reservation_service = ReservationService(user_service)
utilities = Utilities()

''' Initializing Dummy Data '''
pirates_movie = Movie("Pirates of the Caribbean", 128)

demo_user = user_service.register_user("demo@demo.org")

raspi_theatre = Theatre(
    location="1",
    total_rows= 10,
    total_columns= 5
)

pirates_showtime = showtime_service.create_showtime(
    movie = pirates_movie,
    theatre = raspi_theatre,
    showtime = datetime.now()
)

result = reservation_service.create_reservation(
    email = demo_user.email,
    showtime = pirates_showtime,
    seat_name = "A4",
)

result = reservation_service.create_reservation(
    email = demo_user.email,
    showtime = pirates_showtime,
    seat_name = "AAA",
)

utilities.display_seats_for_showtime(showtime = pirates_showtime)

result = showtime_service.search_movie_title("Pirates of the Caribbean")
print(result)
