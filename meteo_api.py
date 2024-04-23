import requests
import json
from pprint import pprint

base_url = "https://api.open-meteo.com"
path = "/v1/forecast"

url = base_url + path

params = {
    "latitude":"44.43", #"44.24",
    "longitude": "26.11",   #"26.5",
    "hourly": ["temperature_2m", "apparent_temperature"],
    "daily": ["temperature_2m_max","temperature_2m_min"],
    "timezone":"EET",
    "past_days":"2",
    "forecast_days":2,

}

response = requests.get( url, params=params)
print(response.status_code)

print(response.request.url)

# print(response.content)

json_response = json.loads(response.content)
pprint(json_response)

print(type(json_response))

with open("temperaturi.txt", "w") as fwrite:
    hourly = json_response["hourly"]

    for i in range(len(hourly["time"])):
        fwrite.write(f'{hourly["time"][i]}, {hourly["temperature_2m"][i]},  {hourly["apparent_temperature"][i]}\n ')
