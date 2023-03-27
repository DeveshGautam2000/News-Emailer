import requests
from sendMail import send_email

api_key = "31f32b440c5d4341a2f1bf5e54f71c13"

url = "https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=31f32b440c5d4341a2f1bf5e54f71c13&language=en"

request = requests.get(url)
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's News" + "\n" +body + article["title"] + "\n" + str(article["description"]) \
        + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)