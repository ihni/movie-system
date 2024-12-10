from app.src.services import (
    ShowtimeService,
    UserService,
    ReservationService
)

from app.src.models import (
    Movie,
    Theatre,
)

from datetime import datetime

''' Initializing Service '''
showtime_service = ShowtimeService()
user_service = UserService()
reservation_service = ReservationService()

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
reservation = reservation_service.create_reservation(
    email = demo_user.email,
    showtime = pirates_showtime,
    seat_name = "A4",
)