from app.src.services import (
    ShowtimeService,
    UserService,
    ReservationService,
    TheatreService
)

#from app.src.cli.app import MovieSystemCLI
from app.src.initialization import Initializer

def main():
    user_service = UserService()
    showtime_service = ShowtimeService()
    reservation_service = ReservationService(user_service)
    theatre_service = TheatreService()

    init = Initializer(theatre_service,reservation_service,user_service,showtime_service)
    init.init()

    #cli = MovieSystemCLI(theatre_service, reservation_service, user_service, showtime_service)
    #cli.cmdloop()

if __name__ == "__main__":
    main()