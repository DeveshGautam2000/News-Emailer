import requests


url = "https://youtu.be/EdftT8GMU1U"

response = requests.get(url)

with open("image.mkv", "wb") as file:
    file.write(response.content)