import requests
import os
from dotenv import load_dotenv

load_dotenv()

def read_image(image):
    response = requests.post(
    url="https://api.ocr.space/parse/image",
    headers={
        "apikey": os.getenv("OCR_SPACE_API_KEY")
    },
    data={
        "url": image,
        "language": "eng",
        "detectOrientation": "true",
    }
    )
    return response.json()

if __name__ == "__main__":
    response = read_image("https://i.imghippo.com/files/ngMbQ1724048156.png")
    print(response['ParsedResults'][0]['ParsedText'])