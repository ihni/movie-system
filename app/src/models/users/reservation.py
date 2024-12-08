from datetime import datetime

class Reservation:
    def __init__(self, uid: int, seat_name: str, user: object, showtime: object):
        self.uid:         int = uid
        self.seat_name:   str = seat_name
        self.user:     object = user
        self.showtime: object = showtime
        self.timestamp:   str = datetime.now()

    def __str__(self):
        return f"Reservation({self.id}, {self.seat_name}, {self.customer_name}, {self.showtime}, {self.timestamp})"