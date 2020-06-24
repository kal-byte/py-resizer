from decouple import config
from pyimgur import Imgur
from PIL import Image
import requests

CLIENT_ID = config("CLIENT_ID")
imgur = Imgur(CLIENT_ID)


def resize_image(image, size):
    im = Image.open(image)
    im = im.resize(size, Image.ANTIALIAS)
    im.save("output.png")

    upload_image = imgur.upload_image("output.png")

    return upload_image


def resize_url(url, size):
    go_from_url = url

    with open("picture.png", "wb") as handler:
        response = requests.get(url, stream=True)

        if not response.ok:
            print(response)
        for block in response.iter_content(1024):
            if not block:
                break
            handler.write(block)

    im = Image.open("picture.png")
    im = im.resize(size, Image.ANTIALIAS)
    im.save("picture.png")

    upload_image = imgur.upload_image("picture.png")

    return upload_image
