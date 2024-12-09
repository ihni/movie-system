from models import User

class UserService:
    def __init__(self):
        self.users = {}

    def register_user(self, email: str) -> object:
        if email in self.users:
            return "User already exists"
        
        user = User(email)
        self.users[email] = user
        return user
    
    def get_user(self, email: str) -> object:
        return self.users.get(email)