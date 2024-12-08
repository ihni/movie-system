class User:
    def __init__(self, email):
        self.email = email
        self.reservations = []
    
    def add_reservation(self, reservation):
        self.reservations.append(reservation)