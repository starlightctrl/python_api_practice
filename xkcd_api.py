import requests
import random
import json

def get_comic():
    latest_comic = requests.get("https://xkcd.com/info.0.json").json()
    latest_id = latest_comic['num']
    id = random.randint(1, latest_id)

    comic = requests.get("https://xkcd.com/{id}/info.0.json").json()
    return comic