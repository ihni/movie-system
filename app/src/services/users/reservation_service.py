from library import LinkedList
from models import Reservation

class ReservationService:
    def __init__(self, user_service):
        self.reservation_history = {}  # stores all reservations by id
        self.user_service = user_service
        self.id = 1

    def create_reservation(self, email: str, showtime: object, seat_name: str):
        """
        Create a reservation for a user.
        
        :param email: User's email
        :param showtime: Showtime object
        :param seat_name: The name of the seat (e.g., 'A1')
        :return: Reservation or error message
        """
        user = self.user_service.get_user(email)
        if not user:
            return "User not found."

        availability_status = showtime.check_seat_availability(seat_name)
        if "not available" in availability_status:
            return availability_status
        
        reservation = Reservation(
            id=self.id,
            user=user,
            seat_name=seat_name,
            showtime=showtime,
        )

        self.reservation_history[self.id] = reservation
        self.id += 1

        user.reservation_history.insert_to_end(reservation)
        showtime.reserve_seat(seat_name)
        return reservation

    def cancel_reservation(self, email: str, reservation_id: int) -> str:
        """
        Cancel a reservation.
        
        :param email: User's email
        :param reservation_id: Unique reservation ID
        :return: Success or error message
        """
        user = self.user_service.get_user(email)
        if not user:
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

    def get_user_reservation_history(self, email: str) -> LinkedList:
        """
        Retrieves the reservation history for a user.

        :param email: User's email
        :return: Linked List of reservations
        """
        user = self.user_service.get_user(email)
        if not user:
            return "User not found."
        
        return user.reservation_history
    
    def write_reservation_to_file(self, reservation: object):
        pass

    def load_reservations_from_file(self):
        pass