import requests
from pprint import pprint

class wea:
	def __init__(self):
		pass
	def find_data(self):
		url = "http://api.open-notify.org/iss-now.json"
		data = requests.get(url).json()
		lat=data["iss_position"]["latitude"]
		lon=data["iss_position"]["longitude"]		
		return(lon,lat)
