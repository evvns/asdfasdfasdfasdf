import time
from instagrapi import Client
import random
USERNAME = "asdf"
PASSWORD = "ohio"

PICTURE_PATHS = ["e.jpg", "E3.jpeg", "E2.jpg", "ceo.jpg", "dog.jpg", "xd.jpg"]

cl = Client()

cl.login(USERNAME, PASSWORD)

while True:
    for picture_path in PICTURE_PATHS:
        cl.account_change_picture(picture_path)
        print(f"Changed profile picture to {picture_path}")

        time.sleep(random.randint(15, 25))