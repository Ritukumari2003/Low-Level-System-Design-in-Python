
class PhoneDisplay:
    def update_temp(self, new_temp):
        print("Phone Display Temperature is: ", new_temp)

class TabDisplay:
    def update_temp(self, new_temp):
        print("Tab Display Temperature is: ", new_temp)


class WeatherStation:
    def __init__(self):
        self.__temperature = 0
        self.__phone_display = PhoneDisplay()
        # Need to modify the existing code to add new display device : Bad Practice
        self.__tab_display = TabDisplay()

    def update_temp(self, new_temp):
        self.__temperature = new_temp
        self.notify_display()

    def notify_display(self):
        self.__phone_display.update_temp(self.__temperature)
        self.__tab_display.update_temp(self.__temperature)

ws = WeatherStation()
ws.update_temp(30)
        