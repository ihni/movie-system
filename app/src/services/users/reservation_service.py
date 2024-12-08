from library import LinkedList
from models import Reservation

class ReservationService:
    def __init__(self):
        self.reservation_history = {} # stores all reservations by id
        self.users = {}
        self.id = 1

    def add_user(self, user: object) -> str:
        if user.email in self.users:
            return "Cannot add user, duplicate email found"

        self.users[user.email] =  {"reservation_history" : LinkedList(), 
                                    "user_obj" : user}
        return "User was added successfully"

    def create_reservation(self, user: object, showtime: object, seat_name: str):
        """
        Create a reservation for a user.
        
        :param user: User object
        :param showtime: Showtime object
        :param seat_name: The name of the seat (e.g., 'A1')
        :return: Reservation or error message
        """
        if user.email not in self.users:
            return "User not found."

        availability_status = showtime.check_seat_availability(seat_name)
        if "not available" in availability_status:
            return availability_status
        
        reservation = Reservation(
            id = self.id,
            user = user,
            seat_name = seat_name,
            showtime = showtime,
        )

        self.reservation_history[self.id] = reservation # for fast look up based on uid of the reservation
        self.id += 1

        self.users[user.email]["reservation_history"].insert_to_end(reservation)
        showtime.reserve_seat(seat_name) # reserving the seat in the actual showtime

        return reservation
    
    def cancel_reservation(self, user: object, reservation_id: int) -> str:
        """
        Cancel a reservation.
        
        :param user: User object
        :param reservation_id: Unique reservation ID
        :return: Success or error message
        """
        if user.email not in self.users:
            return "User not found"
        
        reservation = self.reservation_history.get(reservation_id)

        if not reservation:
            return "Reservation not found"
        
        if reservation.user != user:
            return "This reservation does not belong to the user."
        
        reservation.cancel()

        showtime = reservation.showtime
        showtime.release_seat(reservation.seat_name)

        return f"Reservation {reservation_id} has been canceled."
    
    def get_user_reservation_history(self, user: object):
        """
        Retrieves the reservation history for a user.

        :param user: User object
        :return: Linked List of reservations
        """
        if user.email not in self.users:
            return "User not found."
        
        user_reservations = self.users[user.email]["reservation_history"]
        return user_reservations