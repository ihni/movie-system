from datetime import datetime

class Reservation:
    def __init__(self, id: int, user: object, seat_name: str, showtime: object):
        self.id:          int = id
        self.user:     object = user
        self.seat_name:   str = seat_name
        self.showtime: object = showtime
        self.timestamp:   str = datetime.now()
        self.status:      str = "Boooked"

    def cancel(self):
        self.status = "Cancelled"  # Change status to Cancelled

    def complete(self):
        self.status = "Completed"  # Change status to Completed (when the user uses the reservation)

    def __str__(self):
        return (
            f"Reservation (ID-{self.id}):\n"
            f"{self.seat_name}, {self.user.email}, {self.showtime.display_for_user()}\n"
            f"Status: {self.status} - {self.timestamp}"
        )