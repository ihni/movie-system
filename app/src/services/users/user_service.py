from models import User

class UserService:
    def __init__(self):
        self.users = {}

    def register_user(self, email: str) -> object:
        user = User(email)