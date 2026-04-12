from weather_station import WeatherStation
from observer import Observer
from tv_display import TVDisplay
from phone_display import PhoneDisplay

ws = WeatherStation()
tv_display = TVDisplay()
ws.add_observer(tv_display)

phone_display = PhoneDisplay()
ws.add_observer(phone_display)

ws.update_display(30)


