import requests
import os
import random

# ENV VARIABLES (from GitHub Secrets)
PAGE_ID = os.getenv("FB_PAGE_ID")
ACCESS_TOKEN = os.getenv("FB_ACCESS_TOKEN")
PEXELS_API = os.getenv("PEXELS_API")

# STEP 1: GET IMAGE FROM PEXELS
def get_image():
    url = "https://api.pexels.com/v1/search?query=sri lanka nature&per_page=10"
    headers = {"Authorization": PEXELS_API}

    res = requests.get(url, headers=headers).json()
    photos = res.get("photos", [])

    if not photos:
        return None

    return random.choice(photos)["src"]["original"]

# STEP 2: GENERATE CAPTION
def generate_caption():
    captions = [
        "🌿 Discover the beauty of Sri Lanka 🇱🇰",
        "🏝️ Nature at its finest in Sri Lanka 🌅",
        "🌄 Paradise found in Sri Lanka 🍃",
        "🌊 Feel the calm of Sri Lanka nature 🌴",
        "🌺 Explore untouched beauty 🇱🇰 #Nature"
    ]
    return random.choice(captions)

# STEP 3: POST TO FACEBOOK
def post_to_facebook(image_url, caption):
    url = f"https://graph.facebook.com/{PAGE_ID}/photos"

    payload = {
        "url": image_url,
        "caption": caption,
        "access_token": ACCESS_TOKEN
    }

    res = requests.post(url, data=payload)
    print(res.json())

# RUN
image = get_image()

if image:
    caption = generate_caption()
    post_to_facebook(image, caption)
else:
    print("No image found")
