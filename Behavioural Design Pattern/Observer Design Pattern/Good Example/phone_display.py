from observer import Observer

class PhoneDisplay(Observer):
    def update(self, temp):
        print(f"Phone temperature updated to {temp}")