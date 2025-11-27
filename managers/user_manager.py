from models.user import User

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, username, email):
        user_id = len(self.users) + 1
        user = User(user_id, username, email)
        self.users.append(user)
        return user

    def delete_user(self, user_id):
        self.users = [u for u in self.users if u.user_id != user_id]

    def get_user_by_id(self, user_id):
        for u in self.users:
            if u.user_id == user_id:
                return u
        return None

    def get_user_by_name(self, username):
        for u in self.users:
            if u.username == username:
                return u
        return None
