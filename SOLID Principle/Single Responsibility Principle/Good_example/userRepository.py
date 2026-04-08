from user import User

class UserRepository:
    def __init__(self, db, user, password):
        self.db = db
        self.user = user
        self.password = password

    def save_to_database(self, user: "User"):
        print(f"{user.name} Data has been saved sucessfully")

    def delete_from_database(self, user: "User"):
        print(f"{user.name} Data has been deleted sucessfully.")