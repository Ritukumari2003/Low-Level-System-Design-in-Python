

class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def get_user_info(self):
        print(f"Name: {self.name}. Age: {self.age}")
    
    def is_adult(self):
        return self.age > 18
    
    def save_to_database(self):
        print("Data has been saved sucessfully")

    def delete_from_database(self):
        print("Data has been deleted sucessfully.")