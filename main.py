import requests

api_key = "31f32b440c5d4341a2f1bf5e54f71c13"

url = "https://newsapi.org/v2/everything?q=tesla&from=2023-02-23&sortBy=publishedAt&apiKey=31f32b440c5d4341a2f1bf5e54f71c13"

request = requests.get(url)
content = request.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"])
