from user import User
from userRepository import UserRepository

user_obj = User("Ritu", 23, "abc@gmail.com")
user_obj.get_user_info()
user_repo = UserRepository("userdb", "root", "root")
user_repo.save_to_database(user_obj)