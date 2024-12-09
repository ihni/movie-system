from library import LinkedList

class User:
    def __init__(self, email: str):
        self.email = email
        self.reservation_history = LinkedList()