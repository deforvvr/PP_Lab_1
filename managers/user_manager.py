from models.user import User

class UserManager:

    def __init__(self):
        self.users = []

    def add_user(self, user: User):
        self.users.append(user)
        print(f"Пользователь '{user.username}' добавлен.")

    def remove_user(self, user_id: int):
        user = self.get_user_by_id(user_id)
        if user:
            self.users.remove(user)
            print(f"Пользователь '{user.username}' удалён.")
        else:
            print("Пользователь не найден.")

    def list_users(self):
        if not self.users:
            print("Список пользователей пуст.")
            return
        for user in self.users:
            print(f"{user.user_id}: {user.username} ({user.email})")

    def get_user_by_id(self, user_id: int):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None
