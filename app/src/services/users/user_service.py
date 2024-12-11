from ...models import User
import re
class UserService:
    def __init__(self):
        self.users = {}

    def register_user(self, email: str) -> object:
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return "Invalid email format"
        
        user = User(email)
        self.users[email] = user
        return user
    
    '''
    Getting all users
    '''
    def get_user(self, email: str) -> object:
        user = self.users.get(email)
        if user:
            return user
        return None
    
    def get_users(self) -> list:
        users = list(self.users.values())
        return users if users else "No users found."